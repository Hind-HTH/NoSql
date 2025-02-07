# installer Docker
# Téléchargez l'image Redis: 
    docker pull redis
# Démarrez un conteneur Redis:
    docker run --name my-redis -d redis
# Vérifiez que le conteneur fonctionne:
    docker ps
# Accédez au conteneur Redis avec redis-cli:
    docker exec -it my-redis redis-cli

# Remarque: J'ai verifié le start et stop de container depuis Docker Desktop.

# Docker mongo:
docker run --name my-mongo -p 27017:27017 -d mongo

# La partie neo4j:
docker run \
    --name my_neo4j \
    -p 7474:7474 -p 7687:7687 \
    -v ~/neo4j_data:/data \
    -e NEO4J_AUTH=neo4j/password \
    -d neo4j
# utiliser le pilote Python officiel de Neo4j appelé « neo4j »:
    pip install neo4j


# Télécharger et exécuter l’image Docker Elasticsearch:
    docker run -p 9200:9200 -p 9300:9300 -d -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.14.0
# Information sur le cluster:
    curl 0.0.0.0:9200/_cluster/health | jq
# Infos sur les nœuds:
    curl -X GET "http://0.0.0.0:9200/_cat/nodes?v"