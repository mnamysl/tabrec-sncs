import subprocess
import glob as glob
import os
import re
import csv
import argparse


def process_file(pdf_path_):

    fdir, fname = os.path.split(pdf_path_)
    
    print("*" * 80)
    print(f"Processing '{fname}'")

    fbasename, fext = os.path.splitext(fname)

    loop_cnt = 1
    if fbasename.endswith("a"):
        # alternative ground-truth annotations available => process twice using both variants
        loop_cnt = 2
    
    lst_gt, lst_det, lst_corr, lst_precision, lst_recall, lst_f1 = [], [], [], [], [], []

    for loop in range(loop_cnt):
        gt_fname = os.path.join(args.gt_dir, f"{fbasename}-str.xml")
        res_fname = os.path.join(args.res_dir, f"{fbasename}-str-result.xml")

        if loop > 0:
            # use an alternative ground-truth file
            gt_fname = os.path.join("gt", f"{fbasename[:-1]}b-str.xml")

        print("." * 30)
        print(f"Running evaluation for GT='{gt_fname}'; RES='{res_fname}' (loop={loop})")
        
        out = subprocess.Popen(['java', '-jar', 'tool.jar','-str', gt_fname, res_fname, pdf_path_], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)	
        stdout,stderr = out.communicate()
        
        print("v" * 30)
        print(stdout.decode())

        if stderr is not None:
            print("STDERR:", stderr.decode())
        print("^" * 30)

        num_gt, num_corr, num_det = 0, 0, 0

        if stderr is not None:
            lst_gt.append(num_gt)
            lst_det.append(num_det)
            lst_corr.append(num_corr)
            lst_precision.append(0.0)
            lst_recall.append(0.0)
            lst_f1.append(0.0)
            continue
    
        stdout = stdout.decode()

        lines = stdout.split('\n')    

        table_lines = [line for line in lines if line.startswith("Table")]        
        
        for line in table_lines:
            m = re.search(r"^Table (\d+):  GT size: (\d+) corrDet: (\d+) detected: (\d+)  Precision: \d+ \/ \d+ = (\d+.\d+)  Recall: \d+ \/ \d+ = (\d+.\d+)", line)
            if m:
                print(f"Table: {m.group(1)} GT: {m.group(2)} CORR: {m.group(3)} DET: {m.group(4)} Prec: {m.group(5)} Recall: {m.group(6)}")
                num_gt += int(m.group(2))
                num_corr += int(m.group(3))
                num_det += int(m.group(4))                

        fp_table_lines = [line for line in lines if line.startswith("FP table")]

        for line in fp_table_lines:
            m = re.search(r"^FP table with (\d+) adjacency relations", line)        
            if m:
                print("FP table with ", m.group(1), " adj. relations found")
                num_det += int(m.group(1))

        lst_gt.append(num_gt)
        lst_det.append(num_det)
        lst_corr.append(num_corr)

        precision = float(num_corr) / float(num_det) if num_det != 0 else 0.0
        recall = float(num_corr) / float(num_gt) if num_gt != 0 else 0.0
        f1 = (2.0 * precision * recall) / (precision+recall) if precision+recall > 0 else 0.0

        lst_precision.append(precision)
        lst_recall.append(recall)
        lst_f1.append(f1)

        print(f"[{fbasename}] PRECISION: {precision:.2f}; RECALL: {recall:.2f}; F1: {f1:.2f}")

    if loop_cnt > 1:
        if lst_f1[0] > lst_f1[1]:
            print(f"Selecting result 'a' {lst_f1[0]} vs. {lst_f1[1]}")
            precision = lst_precision[0]
            recall = lst_recall[0]
            f1 = lst_f1[0]
            num_gt = lst_gt[0]
            num_det = lst_det[0]
            num_corr = lst_corr[0]
        else:
            print(f"Selecting result 'b' {lst_f1[0]} vs. {lst_f1[1]}")            


    return fbasename, precision, recall, f1, num_gt, num_det, num_corr


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--pdf-dir', dest="pdf_dir", type=str, help='Path to the directory with PDF files', default="pdf")
    parser.add_argument('--res-dir', dest="res_dir", type=str, help='Path to the directory with result XML files', default="res")
    parser.add_argument('--gt-dir', dest="gt_dir", type=str, help='Path to the directory with ground-truth XML files', default="gt")
    args = parser.parse_args()
    
    total_gt, total_det, total_corr = 0, 0, 0
    perdoc_precision, perdoc_recall = 0.0, 0.0
    num_docs = 0

    doc_rows = []

    
    # Calculate precision/recall for each document separately, then average the scores

    pdf_files = glob.glob(os.path.join(args.pdf_dir, "*.pdf"))
    for pdf_path in sorted(pdf_files):

        output = process_file(pdf_path)
                
        fbasename, precision, recall, f1, num_gt, num_det, num_corr = output

        doc_rows.append([fbasename, precision, recall, f1])

        perdoc_precision += precision
        perdoc_recall += recall
        total_gt += num_gt
        total_det += num_det
        total_corr += num_corr
        num_docs += 1
        

    with open('details.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["PDF", "PRECISION", "RECALL", "F1"])
        for row in doc_rows:
            csv_writer.writerow(row)

    print("*" * 80)

    Precision = float(perdoc_precision) / float(num_docs)
    Recall = float(perdoc_recall) / float(num_docs)
    F1 = (2.0 * Precision * Recall)/(Precision+Recall)

    print("Per document average scores")
    print(f"Precision: {Precision}; Recall: {Recall}; F1: {F1}")
    print("*" * 80)

    Precision = float(total_corr) / float(total_det)
    Recall = float(total_corr) / float(total_gt)
    F1 = (2.0 * Precision * Recall)/(Precision+Recall)

    print("Average scores")
    print(f"Num of GT: {total_gt}; DET: {total_det}; CORR: {total_corr}")
    print(f"Precision: {Precision}; Recall: {Recall}; F1: {F1}")


