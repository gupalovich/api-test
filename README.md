
### Установка elasticsearch
```bash
docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.12.0

# старт - создаст новый контейнер и в консоли напишет пароли
docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.12.0

# вынести ssl сертификат
docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .

# менеджмент паролей - elastic/kibana
# пароль нужен для аутентификации в elasticsearch (дефолт логин - elastic)
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
# токен нужен для связи с elasticsearch
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana

# повторный старт/стоп
docker start es01
docker stop es01

# доступ в консоль
docker exec -it es01 /bin/bash
```

### Установка kibana
```bash
docker pull docker.elastic.co/kibana/kibana:8.12.0
docker run --name kib01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.12.0
# после этого нужно ввести токен на порту 5601
```

### Auth basic
- `elastic`
- `WoqiRk7*wzJFICpWmpBC`
