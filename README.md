# Flexible Hybrid Table Recognition and Semantic Interpretation System

This repository contains the resources from the paper entitled **[Flexible Hybrid Table Recognition and Semantic Interpretation System](https://doi.org/10.1007/s42979-022-01659-z)** published in a Topical Issue of [SN Computer Science](https://www.springer.com/journal/42979) entitled ‘*[Advances on Computer Vision, Imaging and Computer Graphics Theory and Applications](https://link.springer.com/journal/42979/topicalCollection/AC_71872582771df4cac6cab47adc5a19e3)*’

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

## Citing Our Work

Please cite our paper when using the code:

```bib
@Article{Namysl2023,
    author={Namys{\l}, Marcin and Esser, Alexander M. and Behnke, Sven and K{\"o}hler, Joachim},
    title={Flexible Hybrid Table Recognition and Semantic Interpretation System},
    journal={{S}pringer {N}ature {C}omputer {S}cience},
    year={2023},
    month={Mar},
    day={04},
    volume={4},
    number={3},
    pages={246},
    issn={2661-8907},
    doi={10.1007/s42979-022-01659-z},
    url={https://doi.org/10.1007/s42979-022-01659-z}
}
```

## Authors

* Marcin Namysl [ORCID](https://orcid.org/0000-0001-7066-1726), [Google Scholar](https://scholar.google.com/citations?user=JeY8avoAAAAJ&hl=en&oi=sra), [Semantic Scholar](https://www.semanticscholar.org/author/Marcin-Namysl/134442417)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
