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

