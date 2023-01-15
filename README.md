# dockerized-elasticsearch

Example showing how to create an index in containerized Elasticsearch using the Python client and searching using the Kibana Dev Tools. Everything (Kibana, ElasticSearch & indexer.py) runs as a container

Run with:
$docker-compose build
$docker-compose up

Lucene Index is persisted using Docker Volumes. The index can be located at $PROJECT_ROOT_DIRECTORY/esdata/nodes/0/_state

A Kibana container helps to navigate the indexed dataset. The index is accessible at <http://localhost:9200/laptops>

Kibana can be accessed at http://localhost:5601/app/home#/

The index settings & mappings configurations is at location $PROJECT_ROOT_DIRECTORY/indexer/config

Once the containers are running, the index can be searched using REST APIs. Kibana provides Dev Tools to search the index - http://localhost:5601/app/dev_tools#/console

A typical search query (utilizing the ngram analyzer):

GET laptops/_search
{
  "query": {
    "match": {
      "name.ngrams": "mac"
    }
  }
}

***** ELASTIC SEARCH CONFIGURATION FILES & STRUCTURE *****

Elasticsearch has three configuration files:

elasticsearch.yml for configuring Elasticsearch
jvm.options for configuring Elasticsearch JVM settings
log4j2.properties for configuring Elasticsearch logging

The running container can be inspected by the following command (On a *Nix system):
$docker exec -it {CONTAINER_ID} /bin/sh

The {CONTAINER_ID} can be obtained by docker ps command

Once inside the container shell/terminal, the elasticsearch configuration files are located at /usr/share/elasticsearch/config

The Lucene index is stored at /usr/share/elasticsearch/data/nodes/0/_state

The relevant search libs (lucene analyzers, query parsers, core, highlighter etc.) are located at /usr/share/elasticsearch/lib

The extra plugins (say the search results clustering) can be stored in /usr/share/elasticsearch/plugins
