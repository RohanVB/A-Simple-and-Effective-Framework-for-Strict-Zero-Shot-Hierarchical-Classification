# A Simple and Effective Framework for Strict Zero-Shot Hierarchical Classification
Official code for the paper titled "A Simple and Effective Framework for Strict Zero-Shot Hierarchical Classification" published at ACL 2023.

ABSTRACT: In recent years, large language models (LLMs) have achieved strong performance on benchmark tasks, especially in zero or few-shot settings. However, these benchmarks often do not adequately address the challenges posed in the real-world, such as that of hierarchical classification. In order to address this challenge, we propose refactoring conventional tasks on hierarchical datasets into a more indicative long-tail prediction task. We observe LLMs are more prone to failure in these cases. To address these limitations, we propose the use of entailment-contradiction prediction in conjunction with LLMs, which allows for strong performance in a strict zero-shot setting. Importantly, our method does not require any parameter updates, a resource-intensive process and achieves strong performance across multiple datasets.

# Contents:

This repository contains 3 files:

1. Dataloaders.py: Used for loading and formatting YELP, WOS, and Amazon Beauty Datasets
2. Models.py: Used for model prediction using BART, T0pp, and nested BART-T0pp, BART-T0pp-BART models
3. Evaluate.py: Used for accuracy and macro F1 calculations 

Scripts may need to be modified to ensure consistency with file paths. Required permissions to download datasets from corresponding vendors (Yelp, WOS, Amazon Beauty) may be required to be attained. This repository only contains code to be able to replicate all results in our paper.

# Citation

Please consider citing our work if you found it useful in your research:

```
@inproceedings{bhambhoria-etal-2023-simple,
    title = "A Simple and Effective Framework for Strict Zero-Shot Hierarchical Classification",
    author = "Bhambhoria, Rohan  and
      Chen, Lei  and
      Zhu, Xiaodan",
    editor = "Rogers, Anna  and
      Boyd-Graber, Jordan  and
      Okazaki, Naoaki",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-short.152",
    doi = "10.18653/v1/2023.acl-short.152",
    pages = "1782--1792",
    abstract = "In recent years, large language models (LLMs) have achieved strong performance on benchmark tasks, especially in zero or few-shot settings. However, these benchmarks often do not adequately address the challenges posed in the real-world, such as that of hierarchical classification. In order to address this challenge, we propose refactoring conventional tasks on hierarchical datasets into a more indicative long-tail prediction task. We observe LLMs are more prone to failure in these cases. To address these limitations, we propose the use of entailment-contradiction prediction in conjunction with LLMs, which allows for strong performance in a strict zero-shot setting. Importantly, our method does not require any parameter updates, a resource-intensive process and achieves strong performance across multiple datasets.",
}
```
##### For any queries about this work, please contact: Rohan Bhambhoria at <r.bhambhoria@queensu.ca>
