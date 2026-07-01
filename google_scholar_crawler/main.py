from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import time

# Google Scholar blocks GitHub Actions runner IPs and serves a robot page,
# which breaks parsing (missing #gsc_prf_in). Route requests through free
# proxies and retry a few times to improve the chance of a clean fetch.
scholar_id = os.environ['GOOGLE_SCHOLAR_ID']

author = None
max_attempts = 5
for attempt in range(1, max_attempts + 1):
    try:
        pg = ProxyGenerator()
        if pg.FreeProxies():
            scholarly.use_proxy(pg)
        author = scholarly.search_author_id(scholar_id)
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        break
    except Exception as e:
        print(f"Attempt {attempt}/{max_attempts} failed: {e}")
        author = None
        time.sleep(5)

if author is None:
    raise RuntimeError("Failed to fetch Google Scholar data after retries (likely blocked).")

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
