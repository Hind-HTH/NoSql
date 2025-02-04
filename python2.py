#Présentation du regroupement de connexions
import redis
from redis import ConnectionPool
import threading

#Voici un exemple de création d’un pool de connexions avec des options de configuration personnalisées :
pool = ConnectionPool(
    host='localhost',
    port=6379,
    db=0,
    max_connections=10,
    socket_connect_timeout=3,
    socket_keepalive=True
)
r = redis.Redis(connection_pool=pool)

# Créer un pool de connexions Redis
#pool = ConnectionPool(host='localhost', port=6379, db=0)

# Tester la connexion
try:
    r = redis.Redis(connection_pool=pool)
    print("Connexion à Redis réussie.")
    print(r.ping())  # Vérifier la connexion
except redis.exceptions.ConnectionError:
    print("Impossible de se connecter à Redis.")
    exit(1)
    
# Créer plusieurs clients Redis utilisant le même pool de connexions
r1 = redis.Redis(connection_pool=pool)
r2 = redis.Redis(connection_pool=pool)

# Utiliser des threads avec le pool de connexions
def worker():
    r = redis.Redis(connection_pool=pool)
    # Perform Redis operations with 'r'
    # Exemple d'opération Redis dans le thread
    r.set(f"user:{threading.current_thread().name}:name", f"User {threading.current_thread().name}")
    print(f"Thread {threading.current_thread().name} a écrit des données.")

# Créer et démarrer plusieurs threads
threads = [threading.Thread(target=worker) for _ in range(10)]

for thread in threads:
    thread.start()

# Attendre que tous les threads finissent
for thread in threads:
    thread.join()