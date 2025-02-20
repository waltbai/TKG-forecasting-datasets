import json
import requests


qid = "Q202735"
query = f"SELECT ?itemLabel WHERE {{ wd:{qid} rdfs:label ?itemLabel . FILTER (LANG(?itemLabel) = 'en') }} "
endpoint = f"https://query.wikidata.org/bigdata/namespace/wdq/sparql"
headers = {"User-Agent": "SearchItemLabelBotForResearch/0.0 (bailong@ict.ac.cn)"}

req = requests.get(endpoint, headers=headers, params={"query": query, "format": "json"})
print(req.text)
result = json.loads(req.text)
print(result)
print(result["results"]["bindings"][0]["itemLabel"]["value"])