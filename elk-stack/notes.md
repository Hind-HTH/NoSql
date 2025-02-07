# Creer un repertoire:
mkdir elk-stack && cd elk-stack

# creer le fichier
touch filebeat.yml 
touch logstash.conf

# executer le script
python send_logs.py

# verififer cluster élastique est opérationnel :
curl http://0.0.0.0:9200

#  vérifier si l’index de nos données de log python a été créé en exécutant cette commande dans votre terminal 
curl http://0.0.0.0:9200/_cat/indices?v