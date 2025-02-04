from pymongo import MongoClient
import pymongo
import json

#Connexion à la base de donnée:
try:
    client = MongoClient('mongodb://localhost:27017/')
    print("Connexion à MongoDB réussie.")
except:
    print("Connexion à MongoDB échoué.")

#Opérations CRUD de base avec PyMongo:
# 1-Creation de bdd et collection:
db = client.mydb
collection = db.mycollection
# 2- CRUD:
# Inserer un document:
document = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

#inserer plusieurs documents:
documents = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "bob@example.com", "age": 35}
]
result = collection.insert_many(documents)
print("Inserted document IDs:", result.inserted_ids)

#Lire :
#lire un seul document d'un collection (méthode find_one):
query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)

# lire plusieurs document d'un collection (méthode find):
query = {"age": {"$gt": 25}}
documents = collection.find(query)

for doc in documents:
    print(doc)


# Mettre à jour:
# mettre à jour un seul document (méthode update_one):
query = {"name": "John Doe"}
update = {"$set": {"age": 31}}
result = collection.update_one(query, update)
print("Modified document count:", result.modified_count)

# Mettre à jour plusieurs documents (méthode update_many):
query = {"age": {"$gt": 25}}
update = {"$inc": {"age": 1}}
result = collection.update_many(query, update)
print("Modified document count:", result.modified_count)

#Delete:
# Supprimer un seul document (méthode delete_one) :
query = {"name": "John Doe"}
result = collection.delete_one(query)
print("Deleted document count:", result.deleted_count)

# Supprimer plusieurs documents (méthode delete_many) :
query = {"age": {"$gt": 25}}
result = collection.delete_many(query)
print("Deleted document count:", result.deleted_count)


#Interrogation et filtrage des données
#Opérateurs logiques: $and$or$not$nor
query = {
    "$and": [
        {"age": {"$gt": 25}},
        {"email": {"$regex": "@example\.com$"}}
    ]
}
documents = collection.find(query)

#cette verification de found (si oui ou non) pour voir si il est trouvé ou pas:
found = False
print("\n🔹 Résultats de la requête $and:")

for doc in documents:
    print(doc)
    found = True
if not found:
    print("Aucun document trouvé pour la requête avec $and.")


#Projection:Limiter les champs affichés
query = {"age": {"$gt": 25}}
projection = {"_id": 0, "name": 1, "email": 1}
documents = collection.find(query, projection)

for doc in documents:
    print(doc)


#Classement: Tri des résultats (classement par ordre alphabétique du nom)
query = {"age": {"$gt": 25}}
documents = collection.find(query).sort("name", pymongo.ASCENDING)

for doc in documents:
    print(doc)



print("Nombre total de documents dans la collection:", collection.count_documents({}))





# Charger des données à partir d’un fichier JSON:

# Charger les données de json:
with open("Data.json", "r") as file:
    data = json.load(file)

# Inserer les donnée dans mongodb: 
result = collection.insert_many(data)
print("Inserted data with the following IDs:", result.inserted_ids)

# Créer un index:
# Créer un index sur la collection de comptes:
index_name = "name_index"
collection.create_index("name", name=index_name)


#Effectuer des requêtes
# Trouvez tous les name spécifique :
name = "Griffin Hardy"
results = collection.find({"name": name})

for result in results:
    print(result)


#Rechercher tous les email contient (@hotmail):
results = collection.find({"email": {"$regex": "hotmail"}})

for result in results:
    print(result)
# remarque cette focntion je lai modifié par rapport à cette exemple de cour:
#Rechercher tous les comptes dont le solde est supérieur à une valeur spécifique
# min_balance = 30000
# results = collection.find({"balance": {"$gt": min_balance}})

# for result in results:
#     print(result)



#Effectuer des agrégations
#Trouver le solde total pour chaque ville
# pipeline = [
#     {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
#     {"$sort": {"total_balance": -1}}
# ]

# results = collection.aggregate(pipeline)

# for result in results:
#     print(f"{result['_id']}: {result['total_balance']}")


#Trouver le nombre d’utilisateurs par domaine d’email
pipeline = [
    {"$group": {"_id": {"$arrayElemAt": [{"$split": ["$email", "@"]}, 1]}, "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(f"{result['_id']}: {result['count']} utilisateurs")


#Indexation et agrégation
#pour crrer un index unique sur un champs, il faut dabord verfier si il y a un doublant dans mongo db:
#create index sur un champ (méthode create_index):
# index_name = collection.create_index("name", unique=True)