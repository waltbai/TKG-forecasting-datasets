# TKG-forecasting-datasets

Commonly used datasets for TKG forecasting

## Data format

### entity2id & relation2id

In the entity/relation2id files, each line consists of an entity/relation name and corresponding ID, separated by a TAB:

```text
Name1\tID1
Name2\tID2
...
```

### facts

In the train/valid/test fact files, each line consists of a quadruple (subject, relation, object, timestamp), separated by a TAB:

```text
S1\tR1\tO1\tT1
S2\tR2\tO2\tT2
...
```

## Directories

The processing code for datasets are stored in `tools/`.

The datasets are stored in `ICEWS14/`, `ICEWS18/`, `ICEWS05-15/`, `GDELT/`, `WIKI/`, `YAGO/`, respectively.

## Statistics

| Dataset    | Schema   | Entities | Relations |     Train |   Valid |    Test | Start Time | Granularity |
| :--------- | -------- | -------: | --------: | --------: | ------: | ------: | ---------: | ----------: |
| ICEWS14    | CAMEO    |    7,128 |       230 |    74,845 |   8,514 |   7,371 | 2014-01-01 |       1 day |
| ICEWS18    | CAMEO    |   23,033 |       256 |   373,018 |  45,995 |  49,545 | 2018-01-01 |       1 day |
| ICEWS05-15 | CAMEO    |   10,488 |       251 |   368,868 |  46,302 |  46,159 | 2005-01-01 |       1 day |
| GDELT      | CAMEO    |    7,691 |       240 | 1,734,399 | 238,765 | 305,241 | 2018-01-01 |      15 min |
| YAGO       | YAGO     |   10,623 |        10 |   161,540 |  19,523 |  20,026 | 1786-01-01 |      1 year |
| WIKI       | Wikidata |   12,554 |        24 |   539,286 |  67,538 |  63,110 | 1830-01-01 |      1 year |

## Processing steps

The raw data of ICEWS14, ICEWS18, ICEWS05-15, GDELT, YAGO, and WIKI are from [RE-GCN](https://github.com/Lee-zix/RE-GCN).

The process code refer to `tools/dataset_converter.py`

### ICEWS14

- Underline ("_") are replaced by space (" ").
- Time index are deducted by 1, so that timestamps start from 0.

### ICEWS05-15

- Underline ("_") are replaced by space (" ").

### ICEWS18

- Underline ("_") are replaced by space (" ").
- Time index are diveded by 24, so that the time unit is DAY now.
- The 5-th column is removed.

### GDELT

- Brackets ("()") in entities are removed.
- Tags in entities are removed ("@***" in brackets).
- Entities are converted to Title-format.
- Relation are mapped from CAMEO event code to actual relation name.
- Time index are divided by 15, so that the time unit is 15 minutes now.

### WIKI

- WikiIDs are mapped to actual names, mostly via Wikidata query service.  
Some IDs failed to be automatically mapped (mostly caused by redirections) are manually mapped.  
Entities without names are mapped to its QID.
- The 5-th column is removed.
- entity2id and relation2id sorted by id.

### YAGO

- Brackets ("<>") are removed.
- Underline ("_") are replaced by space (" ").

## Citation

In previous papers, the datasets are cited as follows:

```text
# ICEWS14
@inproceedings{li-etal-2021-temporal,
    author = {Li, Zixuan and Jin, Xiaolong and Li, Wei and Guan, Saiping and Guo, Jiafeng and Shen, Huawei and Wang, Yuanzhuo and Cheng, Xueqi},
    title = {Temporal Knowledge Graph Reasoning Based on Evolutional Representation Learning},
    year = {2021},
    isbn = {9781450380379},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3404835.3462963},
    doi = {10.1145/3404835.3462963},
    booktitle = {Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},
    pages = {408–417},
    numpages = {10},
    keywords = {evolutional representation learning, graph convolution network, temporal knowledge graph},
    location = {Virtual Event, Canada},
    series = {SIGIR '21}
}

# ICEWS05-15
@inproceedings{li-etal-2021-temporal,
    author = {Li, Zixuan and Jin, Xiaolong and Li, Wei and Guan, Saiping and Guo, Jiafeng and Shen, Huawei and Wang, Yuanzhuo and Cheng, Xueqi},
    title = {Temporal Knowledge Graph Reasoning Based on Evolutional Representation Learning},
    year = {2021},
    isbn = {9781450380379},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3404835.3462963},
    doi = {10.1145/3404835.3462963},
    booktitle = {Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},
    pages = {408–417},
    numpages = {10},
    keywords = {evolutional representation learning, graph convolution network, temporal knowledge graph},
    location = {Virtual Event, Canada},
    series = {SIGIR '21}
}

# ICEWS18
@inproceedings{jin-etal-2020-recurrent,
    title = "Recurrent Event Network: Autoregressive Structure Inferenceover Temporal Knowledge Graphs",
    author = "Jin, Woojeong  and
      Qu, Meng  and
      Jin, Xisen  and
      Ren, Xiang",
    editor = "Webber, Bonnie  and
      Cohn, Trevor  and
      He, Yulan  and
      Liu, Yang",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.541/",
    doi = "10.18653/v1/2020.emnlp-main.541",
    pages = "6669--6683",
}

# GDELT
@inproceedings{jin-etal-2020-recurrent,
    title = "Recurrent Event Network: Autoregressive Structure Inferenceover Temporal Knowledge Graphs",
    author = "Jin, Woojeong  and
      Qu, Meng  and
      Jin, Xisen  and
      Ren, Xiang",
    editor = "Webber, Bonnie  and
      Cohn, Trevor  and
      He, Yulan  and
      Liu, Yang",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.541/",
    doi = "10.18653/v1/2020.emnlp-main.541",
    pages = "6669--6683",
}

# WIKI
@inproceedings{leblay-chekol-2018-deriving,
    author = {Leblay, Julien and Chekol, Melisachew Wudage},
    title = {Deriving Validity Time in Knowledge Graph},
    year = {2018},
    isbn = {9781450356404},
    publisher = {International World Wide Web Conferences Steering Committee},
    address = {Republic and Canton of Geneva, CHE},
    url = {https://doi.org/10.1145/3184558.3191639},
    doi = {10.1145/3184558.3191639},
    booktitle = {Companion Proceedings of the The Web Conference 2018},
    pages = {1771–1776},
    numpages = {6},
    keywords = {factorization machines, temporal knowledge graph},
    location = {Lyon, France},
    series = {WWW '18}
}

# YAGO
@inproceedings{mahdisoltani-etal-2013-yago3,
    TITLE = {{YAGO3: A Knowledge Base from Multilingual Wikipedias}},
    AUTHOR = {Mahdisoltani, Farzaneh and Biega, Joanna and Suchanek, Fabian M.},
    URL = {https://imt.hal.science/hal-01699874},
    BOOKTITLE = {{CIDR}},
    ADDRESS = {Asilomar, United States},
    YEAR = {2013},
    MONTH = Jan,
    PDF = {https://imt.hal.science/hal-01699874v1/file/cidr2015.pdf},
    HAL_ID = {hal-01699874},
    HAL_VERSION = {v1},
}
```
