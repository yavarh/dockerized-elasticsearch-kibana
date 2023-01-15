from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch.exceptions import ConnectionError
import time
import json
from elasticsearch.client import IndicesClient

es = Elasticsearch(hosts=[{"host":'elasticsearch'}], retry_on_timeout = True)

for _ in range(100):
    try:
        # make sure the cluster is available
        es.cluster.health(wait_for_status='yellow')
    except ConnectionError:
        time.sleep(2)

with open('laptop.json') as fp:
	data = json.load(fp)

with open("./config/index_configuration.json") as ic:
	configurations1 = json.load(ic)

es_index_client = IndicesClient(es)
es_index_client.create(index="laptops", body=configurations1)

print("Indexing... (please hold on)")
bulk(es, data, index='laptops', request_timeout=200)
print("Indexing completed....")
