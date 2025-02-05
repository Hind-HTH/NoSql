
# Connexion de Python à Neo4j
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"

user = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(user, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return list(result)

# Création de nœuds
person1 = "CREATE (p:Person {name: 'Alice', age: 30})"
person2 = "CREATE (p:Person {name: 'Bob', age: 25})"
person3 = "CREATE (p:Person {name: 'Charlie', age: 35})"

run_query(person1)
run_query(person2)
run_query(person3)


# Créer des relations:
relationship1 = "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'}) CREATE (a)-[:FRIEND]->(b)"
relationship2 = "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)"
relationship3 = "MATCH (a:Person {name: 'Bob'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)"

run_query(relationship1)
run_query(relationship2)
run_query(relationship3)

# Interrogation de la base de données Neo4j avec Python:
# Récupérer tous les nœuds Personne:
query_all_persons = "MATCH (p:Person) RETURN p.name, p.age"

results = run_query(query_all_persons)

print("\n🔍 Liste des personnes enregistrées :")
for record in results:
    print(f"Name: {record['p.name']}, Age: {record['p.age']}")


# Trouver les amis d’une personne spécifique:
def get_friends(name):
    query = f"MATCH (p:Person {{name: '{name}'}})-[:FRIEND]->(friend) RETURN friend.name, friend.age"
    results = run_query(query)
    return results

name = "Alice"
friends = get_friends(name)

print(f"Friends of {name}:")
for record in friends:
    print(f"Name: {record['friend.name']}, Age: {record['friend.age']}")

# Supprimer tous les nœuds et relations:
delete_nodes_and_relationships = "MATCH (n) DETACH DELETE n"
resultat = run_query(delete_nodes_and_relationships)

# print le resulatat de suppression:
print("\n🛑 Nœuds après suppression :")
if not resultat:
    print("✅ Tous les nœuds ont été supprimés.")
else:
    for record in resultat:
        print(record["n"])



# Exemple : un système simple de recommandation de films
# Créer les nœuds et les relations dans Neo4j:
actors = [
    "CREATE (a:Actor {name: 'Tom Hanks'})",
    "CREATE (a:Actor {name: 'Meryl Streep'})",
    "CREATE (a:Actor {name: 'Tom Cruise'})",
    "CREATE (a:Actor {name: 'Julia Roberts'})",
]

print("\n🚀 Ajout des acteurs...")
for actor in actors:
    print(f"🟢 Exécution : {actor}")
    run_query(actor)


movies = [
    "CREATE (m:Movie {title: 'Forrest Gump', year: 1994})",
    "CREATE (m:Movie {title: 'The Post', year: 2017})",
    "CREATE (m:Movie {title: 'Top Gun', year: 1986})",
    "CREATE (m:Movie {title: 'Pretty Woman', year: 1990})",
]

print("\n🎬 Ajout des films...")
for movie in movies:
    print(f"🟢 Exécution : {movie}")
    run_query(movie)

# for actor in actors:
#     run_query(actor)

# for movie in movies:
#     run_query(movie)

relationships = [
    "MATCH (a:Actor {name: 'Tom Hanks'}), (m:Movie {title: 'Forrest Gump'}) CREATE (a)-[:ACTED_IN]->(m)",
    "MATCH (a:Actor {name: 'Tom Hanks'}), (m:Movie {title: 'The Post'}) CREATE (a)-[:ACTED_IN]->(m)",
    "MATCH (a:Actor {name: 'Meryl Streep'}), (m:Movie {title: 'The Post'}) CREATE (a)-[:ACTED_IN]->(m)",
    "MATCH (a:Actor {name: 'Tom Cruise'}), (m:Movie {title: 'Top Gun'}) CREATE (a)-[:ACTED_IN]->(m)",
    "MATCH (a:Actor {name: 'Julia Roberts'}), (m:Movie {title: 'Pretty Woman'}) CREATE (a)-[:ACTED_IN]->(m)",
]

print("\n🔗 Ajout des relations Acted_In...")
for relationship in relationships:
    print(f"🟢 Exécution : {relationship}")
    run_query(relationship)

# for relationship in relationships:
#     run_query(relationship)


# Créer la fonction de recommandation de film:
def recommend_movies(liked_actor_name):
    query = f"""
    MATCH (liked_actor:Actor {{name: '{liked_actor_name}'}})-[:ACTED_IN]->(liked_movie:Movie)
    MATCH (other_actor:Actor)-[:ACTED_IN]->(liked_movie)
    MATCH (other_actor)-[:ACTED_IN]->(recommended_movie:Movie)
    WHERE NOT (liked_actor)-[:ACTED_IN]->(recommended_movie)
    RETURN DISTINCT recommended_movie.title AS title, recommended_movie.year AS year
    ORDER BY year DESC
    """

    results = run_query(query)
    return results

# Obtenir des recommandations de films:
liked_actor_name = "Tom Hanks"
recommended_movies = recommend_movies(liked_actor_name)

# print(f"Movie recommendations based on liking {liked_actor_name}:")
# for record in recommended_movies:
#     print(f"{record['title']} ({record['year']})")

print(f"\n🎥 Films recommandés basés sur {liked_actor_name} :")
if recommended_movies:
    for record in recommended_movies:
        print(f"✅ {record['title']} ({record['year']})")
else:
    print("🚫 Aucune recommandation trouvée.")

