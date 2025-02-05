# Créer un index et insérer des données:
curl -XPUT 'http://localhost:9200/cities' -H 'Content-Type: application/json' -d '
{
  "settings": {
    "number_of_shards": 2,
    "number_of_replicas": 2
  }
}'

# Pour récupérer l’index et vérifier ses paramètres :
curl -XGET 'http://localhost:9200/my_index/_settings' | jq

# Remplissons maintenant cet index en créant notre premier document en courant dans notre terminal :
curl -XPOST 'http://localhost:9200/cities/_doc' -H 'Content-Type: application/json' -d '
{
  "city": "London",
  "country": "England"
}'

# pour vérifier en exécutant cette commande :
curl -XGET 'http://localhost:9200/cities/_doc/{document_id}'


# Indexation des données dans Elasticsearch:
# Créer un index à partir d’un fichierjson:
# remarque sur cette partie, j'ai télécharger les ficheirs json et j'ai exécuté ces commandes:
curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/receipe/_bulk --data-binary "@receipe.json" &&\
printf "\n✅ Insertion receipe index to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/accounts/docs/_bulk --data-binary "@accounts.json"
printf "\n✅ Insertion accounts index to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/movies/_bulk --data-binary "@movies.json"
printf "\n✅ Insertion movies index to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/products/_bulk --data-binary "@products.json"
printf "\n✅ Insertion products index to elastic node OK ✅ "

