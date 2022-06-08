# ICDAR 2013 Evaluation Script

This directory contains the evaluation script, which was employed in our experiment performed on the [ICDAR 2013 benchmark](https://roundtrippdf.com/en/data-extraction/icdar-2013-table-competition/) (see §5.5 in our paper).
In the following, we describe the steps that are required to run our evaluation script.

# Quick Start

## Dependencies
We employ the command-line tool written in Java that enables us to perform evaluation on individual files. 
Our script collects the results from all files in the benchmark data set and calculate the cummulative scores.

The aforementioned tool can be downloaded from [here](https://roundtrippdf.com/en/data-extraction/table-recognition-dataset-tools/). 
After downloading, please rename the JAR file to **tool.jar** and place it in the directory where the **eval.py** script is located.

## Data Set Download and Setup
Please download the **Competition dataset of EU and US documents** from [here](https://roundtrippdf.com/en/downloads/).
Next, extract all PDF files to a separate directory, e.g., *PDF_FILES*. Similarly, place all XML files in another directory, e.g., *REF_XML*.

## Setting Up the Reconition Results
The result XML files from your method need to be placed in another directory, e.g., *RES_XML*. Please note that the files need to follow the name pattern supported by the script, i.e., **[filename]-str-result.xml**, where **[filename]** is the basename of the corresponding PDF file.

## Executing the Script
Finally, the evaluation can be performed by calling:
```
python3 eval.py --pdf-dir PDF_FILES --gt-dir REF_XML --res-dir RES_XML
```
At the end of the output produced by the script, the cummulative scores are displayed, e.g.:
```
********************************************************************************
Per document average scores
Precision: 0.8714227705826723; Recall: 0.8467831413095247; F1: 0.8589262858140391
********************************************************************************
Average scores
Num of GT: 25319; DET: 24097; CORR: 22722
Precision: 0.942938955056646; Recall: 0.8974288084047554; F1: 0.9196211753278292
```

