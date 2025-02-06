# premiere verfication de lenvironement:
docker-compose exec logstash bin/logstash --config.test_and_exit -f /usr/share/logstash/pipeline/logstash.conf

# pour télécharger les ficheir csv:
wget https://gist.githubusercontent.com/bdallard/d4a3e247e8a739a329fd518c0860f8a8/raw/82fb43adc5ce022797a5df21eb06dd8e755145ea/data.csv

wget https://gist.githubusercontent.com/bdallard/d4a3e247e8a739a329fd518c0860f8a8/raw/82fb43adc5ce022797a5df21eb06dd8e755145ea/data-json.csv

# redémarrez l’architecture ELK, vous pouvez maintenant voir notre index en exécutant cette commande dans votre terminal :
curl -X GET "0.0.0.0:9200/csv-data/_search?q=*" | jq


