# Flexible, Hybrid Table Recognition and Semantic Interpretation System

This repository contains the resources from our paper: **Flexible, Hybrid Table Recognition and Semantic Interpretation System** that was submitted to a Topical Issue of [SN Computer Science](https://www.springer.com/journal/42979) entitled ‘*Advances on Computer Vision, Imaging and Computer Graphics Theory and Applications*’

## Repository Structure
This repository is structured as follows:

```
.
├── LICENSE
├── README.md
├── evaluation
│   └── ICDAR2013
└── results
    ├── icdar2013
    ├── icdar2019
    └── sanity-check
```
The [evaluation/ICDAR2013](./evaluation/ICDAR2013) directory contains the evaluation script used in the experiment performed on the ICDAR 2013 data set. For a detailed description, see the corresponding [README](./evaluation/ICDAR2013/README.md) file.

Moreover, the [results](/results) directory contains the logs and XML files from the experiments described in our paper that were performed on the [ICDAR 2013](./results/icdar2013) and [ICDAR 2019](./results/icdar2019) benchmarks. Moreover, we also include the results of the [sanity check](./results/sanity-check) that allowed us to locate and fix an issue in the evaluation script employed to perform the evaluation on the ICDAR 2019 benchmark. For more details about this experiment, please see §5.6 in our paper.
