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


# La partie neo4j:
docker run \
    --name my_neo4j \
    -p 7474:7474 -p 7687:7687 \
    -v ~/neo4j_data:/data \
    -e NEO4J_AUTH=neo4j/password \
    -d neo4j
# utiliser le pilote Python officiel de Neo4j appelé « neo4j »:
    pip install neo4j