# TKG-forecasting-datasets

Commonly used datasets for TKG forecasting

## Data format

### entity2id & relation2id

In the entity/relation2id files, each line consists of an entity/relation name and corresponding ID, separated by a TAB:

```text
name1\tID1
name2\tID2
...
```

### facts

In the train/valid/test fact files, each line consists of a quadruple (subject, relation, object, timestamp), separated by a TAB:

```text
s1\tr1\to1\tt1
s2\tr2\to2\tt2
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
