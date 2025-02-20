"""
Convert dataset from RE-GCN to standardized format.
"""
import argparse
import json
import os
from typing import List

from pytest import fail
import requests
from tqdm import tqdm
from yaml import load, Loader


def convert_icews14(input_dir: str, output_dir: str):
    """
    Convert ICEWS14 dataset to standardized format.
    """
    # Process entity2id: replace "_" with " "
    in_path = os.path.join(input_dir, "entity2id.txt")
    out_path = os.path.join(output_dir, "entity2id.txt")
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            name, id = line.strip().split("\t")
            name = name.replace("_", " ")
            fout.write(f"{name}\t{id}\n")

    # Process relation2id: replace "_" with " "
    in_path = os.path.join(input_dir, "relation2id.txt")
    out_path = os.path.join(output_dir, "relation2id.txt")
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            name, id = line.strip().split("\t")
            name = name.replace("_", " ")
            fout.write(f"{name}\t{id}\n")

    # Process fact files:
    #   In original ICEWS14, time starts with 1
    for part in ["train", "valid", "test"]:
        in_path = os.path.join(input_dir, f"{part}.txt")
        out_path = os.path.join(output_dir, f"{part}.txt")
        with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
            for line in fin:
                s, p, o, t = line.strip().split("\t")
                t = int(t) - 1
                fout.write(f"{s}\t{p}\t{o}\t{t}\n")


def convert_icews18(input_dir: str, output_dir: str):
    """
    Convert ICEWS18 dataset to standardized format.
    """
    # Process entity2id: replace "_" with " "
    in_path = os.path.join(input_dir, "entity2id.txt")
    out_path = os.path.join(output_dir, "entity2id.txt")
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            name, id = line.strip().split("\t")
            name = name.replace("_", " ")
            fout.write(f"{name}\t{id}\n")

    # Process relation2id: replace "_" with " "
    in_path = os.path.join(input_dir, "relation2id.txt")
    out_path = os.path.join(output_dir, "relation2id.txt")
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            name, id = line.strip().split("\t")
            name = name.replace("_", " ")
            fout.write(f"{name}\t{id}\n")

    # Process fact files:
    #   In original ICEWS18, time increases by 24 hours,
    #   there exists redundant spaces,
    #   and there exists an additional column
    for part in ["train", "valid", "test"]:
        in_path = os.path.join(input_dir, f"{part}.txt")
        out_path = os.path.join(output_dir, f"{part}.txt")
        with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
            for line in fin:
                s, p, o, t = line.strip().split("\t")[:4]
                t = int(t) // 24
                fout.write(f"{s.strip()}\t{p.strip()}\t{o.strip()}\t{t}\n")


def convert_icews05_15(input_dir: str, output_dir: str):
    """
    Convert ICEWS05-15 dataset to standardized format.
    """
    # Process entity2id: replace "_" with " "
    in_path = os.path.join(input_dir, "entity2id.txt")
    out_path = os.path.join(output_dir, "entity2id.txt")
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            name, id = line.strip().split("\t")
            name = name.replace("_", " ")
            fout.write(f"{name}\t{id}\n")

    # Process relation2id: replace "_" with " "
    in_path = os.path.join(input_dir, "relation2id.txt")
    out_path = os.path.join(output_dir, "relation2id.txt")
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            name, id = line.strip().split("\t")
            name = name.replace("_", " ")
            fout.write(f"{name}\t{id}\n")

    # Process fact files: copy original files
    for part in ["train", "valid", "test"]:
        in_path = os.path.join(input_dir, f"{part}.txt")
        out_path = os.path.join(output_dir, f"{part}.txt")
        with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
            for line in fin:
                s, p, o, t = line.strip().split("\t")
                fout.write(f"{s}\t{p}\t{o}\t{t}\n")


def convert_gdelt(input_dir: str, output_dir: str, cameo_path: str):
    """
    Convert GDELT dataset to standardized format.
    """
    # Process entity2id: remove brackets and use title string format
    in_path = os.path.join(input_dir, "entity2id.txt")
    out_path = os.path.join(output_dir, "entity2id.txt")
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            name, id = line.strip().split("\t")
            # In GDELT, the brackets always at the end of an entity name
            try:
                name = name[:name.index("(")].strip()
            except ValueError:
                pass
            name = name.title()
            fout.write(f"{name}\t{id}\n")

    # Process relation2id: convert CAMEO event code to relation name
    in_path = os.path.join(input_dir, "relation2id.txt")
    out_path = os.path.join(output_dir, "relation2id.txt")
    with open(cameo_path, "r") as f:
        cameo = load(f, Loader=Loader)["event_code"]
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            name, id = line.strip().split("\t")
            name = cameo[name]
            fout.write(f"{name}\t{id}\n")

    # Process fact files:
    #   In original GDELT, time increases by 15 minutes,
    #   there exists redundant spaces,
    #   and there exists an additional column
    for part in ["train", "valid", "test"]:
        in_path = os.path.join(input_dir, f"{part}.txt")
        out_path = os.path.join(output_dir, f"{part}.txt")
        with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
            for line in fin:
                s, p, o, t = line.strip().split("\t")[:4]
                t = int(t) // 15
                fout.write(f"{s.strip()}\t{p.strip()}\t{o.strip()}\t{t}\n")


def convert_yago(input_dir: str, output_dir: str):
    """
    Convert YAGO dataset to standardized format.
    """
    # Process entity2id: remove brackets and use title string format
    in_path = os.path.join(input_dir, "entity2id.txt")
    out_path = os.path.join(output_dir, "entity2id.txt")
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            name, id = line.strip().split("\t")[:2]
            # In GDELT, the brackets always at the end of an entity name
            name = name.strip("<>").replace("_", " ")
            fout.write(f"{name}\t{id}\n")

    # Process relation2id: convert CAMEO event code to relation name
    in_path = os.path.join(input_dir, "relation2id.txt")
    out_path = os.path.join(output_dir, "relation2id.txt")
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            name, id = line.strip().split("\t")
            name = name.strip("<>")
            fout.write(f"{name}\t{id}\n")

    # Process fact files:
    #   remove extra columns
    for part in ["train", "valid", "test"]:
        in_path = os.path.join(input_dir, f"{part}.txt")
        out_path = os.path.join(output_dir, f"{part}.txt")
        with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
            for line in fin:
                s, p, o, t = line.strip().split("\t")[:4]
                t = int(t)
                fout.write(f"{s.strip()}\t{p.strip()}\t{o.strip()}\t{t}\n")


def get_wiki_names(wids: List[str], fp: str):
    """
    Get entity names for QIDs in WIKI.
    """
    endpoint = f"https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    headers = {"User-Agent": "SearchItemLabelBotForResearch/0.0 (bailong@ict.ac.cn)"}
    wid2name = {}
    fails = []
    with tqdm(total=len(wids)) as pbar:
        for wid in wids:
            query = f"SELECT ?itemLabel WHERE {{ wd:{wid} rdfs:label ?itemLabel . FILTER (LANG(?itemLabel) = 'en') }} "
            req = requests.get(endpoint, headers=headers, params={"query": query, "format": "json"})
            result = json.loads(req.text)
            try:
                name = result["results"]["bindings"][0]["itemLabel"]["value"]
                wid2name.setdefault(wid, name)
            except:
                fails.append(wid)
            pbar.update(1)
            pbar.set_description(f"Total:{len(wid2name)}, Fail:{len(fails)}")
    with open(fp, "w", encoding="utf-8") as f:
        for wid, name in wid2name.items():
            f.write(f"{wid}\t{name}\n")
    with open(fp+".fail", "w", encoding="utf-8") as f:
        for wid in fails:
            f.write(f"{wid}\n")


def convert_wiki(input_dir: str, output_dir: str):
    """
    Convert WIKI dataset to standard format.
    """
    # Load wid2name, get WikiID2name mappings if files do not exist
    fpath = os.path.join("./wid2name.txt")
    if not os.path.exists(fpath):
        wids = []
        fp = os.path.join(input_dir, f"entity2id.txt")
        with open(fp, "r", encoding="utf-8") as f:
            for line in f:
                qid, _ = line.strip().split("\t")
                wids.append(qid)
        fp = os.path.join(input_dir, "relation2id.txt")
        with open(fp, "r", encoding="utf-8") as f:
            for line in f:
                pid, _ = line.strip().split("\t")
                wids.append(pid)
        get_wiki_names(wids, fpath)
    else:
        pass
    wid2name = {}
    with open(fpath, "r", encoding="utf-8") as f:
        for line in f:
            try:
                wid, name = line.strip().split("\t")
            except:
                raise ValueError(line)
            wid2name.setdefault(wid, name)

    # Process entity2id
    in_path = os.path.join(input_dir, f"entity2id.txt")
    out_path = os.path.join(output_dir, f"entity2id.txt")
    id2entity = {}
    with open(in_path, "r", encoding="utf-8") as fin:
        for line in fin:
            qid, id = line.strip().split("\t")[:2]
            name = wid2name[qid]
            id2entity[int(id)] = name

    with open(out_path, "w", encoding="utf-8") as fout:
        for id in sorted(id2entity.keys()):
            fout.write(f"{id2entity[id]}\t{id}\n")

    # Process relation2id
    in_path = os.path.join(input_dir, f"relation2id.txt")
    out_path = os.path.join(output_dir, f"relation2id.txt")
    id2relation = {}
    with open(in_path, "r", encoding="utf-8") as fin:
        for line in fin:
            pid, id = line.strip().split("\t")[:2]
            name = wid2name[pid]
            id2relation[int(id)] = name

    with open(out_path, "w", encoding="utf-8") as fout:
        for id in sorted(id2relation.keys()):
            fout.write(f"{id2relation[id]}\t{id}\n")

    # Process fact files:
    #   remove extra columns
    for part in ["train", "valid", "test"]:
        in_path = os.path.join(input_dir, f"{part}.txt")
        out_path = os.path.join(output_dir, f"{part}.txt")
        with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
            for line in fin:
                s, p, o, t = line.strip().split("\t")[:4]
                t = int(t)
                fout.write(f"{s.strip()}\t{p.strip()}\t{o.strip()}\t{t}\n")


def guess_dataset(input_dir: str) -> str:
    """
    Guess dataset name by input directory.
    """
    dir_name = os.path.split(input_dir)[-1]
    if dir_name in ["ICEWS14", "ICEWS14s"]:
        guess_name = "ICEWS14"
    else:
        guess_name = dir_name.upper()
    return guess_name


def get_args():
    """
    Get arguments from command line.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str)
    parser.add_argument("--output_dir", type=str, default=".")
    parser.add_argument("--dataset", type=str, default=None)
    parser.add_argument("--cameo_path", type=str, default="cameo.yaml")
    return parser.parse_args()


def main():
    """
    Main function.
    """
    args = get_args()
    if args.dataset is None:
        args.dataset = guess_dataset(args.input_dir)
    else:
        args.dataset = args.dataset.upper()

    input_dir = args.input_dir
    output_dir = os.path.join(args.output_dir, args.dataset)
    os.makedirs(output_dir, exist_ok=True)

    if args.dataset == "ICEWS14":
        convert_icews14(input_dir, output_dir)
    elif args.dataset == "ICEWS18":
        convert_icews18(input_dir, output_dir)
    elif args.dataset == "ICEWS05-15":
        convert_icews05_15(input_dir, output_dir)
    elif args.dataset == "GDELT":
        convert_gdelt(input_dir, output_dir, args.cameo_path)
    elif args.dataset == "YAGO":
        convert_yago(input_dir, output_dir)
    elif args.dataset == "WIKI":
        convert_wiki(input_dir, output_dir)
    else:
        raise ValueError(f"Unknown dataset: {args.dataset}")


if __name__ == "__main__":
    main()
