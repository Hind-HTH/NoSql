import redis

# Se connecter au serveur Redis (par défaut localhost et port 6379)
r = redis.Redis(host='localhost', port=6379, db=0)

# Ajouter des clés avec des valeurs
r.set('user:1:name', 'John Doe')
r.set('user:1:email', 'john.doe@example.com')

# Ajouter une clé avec un délai d'expiration
r.setex('session_key', 3600, 'session_data')

# Récupérer les valeurs des clés
user_name = r.get('user:1:name')
user_email = r.get('user:1:email')

# Décoder les valeurs pour les afficher sous forme de chaîne
user_name = user_name.decode('utf-8')
user_email = user_email.decode('utf-8')

# Afficher les valeurs récupérées
print(f'User Name: {user_name}')
print(f'User Email: {user_email}')

# Récupérer plusieurs clés à la fois
keys = ['user:1:name', 'user:1:email']
values = r.mget(keys)

# Convert byte values to strings
values = [value.decode('utf-8') for value in values]
# Décoder les valeurs
print(f'Multiple values: {values}')
