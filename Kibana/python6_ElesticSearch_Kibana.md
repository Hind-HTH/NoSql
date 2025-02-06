# vérifier tous nos indices en exécutant la commande suivante :
GET /_cat/indices?v


#regler le probleme deimporte des donnés json:
wget https://gist.githubusercontent.com/bdallard/16aa2af027696c4ee4d0bb0db017276a/raw/1632ed761277b52ed6b5296b7f9bf26b6c7f18c9/movies.json
 
wget https://gist.githubusercontent.com/bdallard/16aa2af027696c4ee4d0bb0db017276a/raw/1632ed761277b52ed6b5296b7f9bf26b6c7f18c9/products.json
 
wget https://gist.githubusercontent.com/bdallard/16aa2af027696c4ee4d0bb0db017276a/raw/1632ed761277b52ed6b5296b7f9bf26b6c7f18c9/receipe.json
 
wget https://gist.githubusercontent.com/bdallard/16aa2af027696c4ee4d0bb0db017276a/raw/1632ed761277b52ed6b5296b7f9bf26b6c7f18c9/accounts.json

#mettre les requtte curl:
curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/receipe/_bulk --data-binary "@receipe.json" &&\
printf "\n✅ Insertion receipe index to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/accounts/docs/_bulk --data-binary "@accounts.json"
printf "\n✅ Insertion accounts index to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/movies/_bulk --data-binary "@movies.json"
printf "\n✅ Insertion movies index to elastic node OK ✅ "

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/products/_bulk --data-binary "@products.json"
printf "\n✅ Insertion products index to elastic node OK ✅ "
#capture decran: ./QuatriemePartie/elasticSearch/Correction_créer_index_aprtir_json.png



# Exercices Requettes:
# Requêtes Exercices pour la pratique
# Base de données de films:

# 1- Récupérez tous les films intitulés « Star Wars » réalisés par « George Lucas » à l’aide d’une requête booléenne.

# 1- correction: 
GET movies/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "title": "Star Wars" } },
        { "match": { "actors": "George Lucas" } }
      ]
    }
  }
}

# resultat:
{
  "took" : 4,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  }
}

# Base de données Receipe:
# 1- Récupérez tous les documents de l’index:
# correction:
GET /receipe/_search
{
  "query": {
    "match_all": {}
  }
}

# capture d'ecran : Exercice2-1

# 2- Récupérez tous les documents de l’index dont le champ preparation_time_minutes est supérieur ou égal à 60.
# correction:
GET /receipe/_search
{
  "query": {
    "range": {
      "preparation_time_minutes": {
        "gte": 60
      }
    }
  }
}
# capture d'écran:Exercice2-2

#3- Récupérez tous les documents de l’index qui contiennent un ingrédient portant le nom « sucre ».
#Correction:
GET /receipe/_search
{
  "query": {
    "term": {
      "ingredients.name.keyword": "sucre"
    }
  }
}
# capture decran : Execice3-2

# Base de données de comptes:
# 1- Récupérez tous les documents de l’index dont le champ de solde est supérieur ou égal à 1000.
#Correction:
GET /accounts/_search
{
  "query": {
    "range": {
      "balance": {
        "gte": 1000
      }
    }
  }
}
# Capture d'ecran: Exercice3-1

# 2- Retrieve all documents in the index with a gender field equal to "female".
# Correction:
GET /accounts/_search
{
  "query": {
    "term": {
      "gender.keyword": "F"
    }
  }
}
#Capture decran: Exercice3-2