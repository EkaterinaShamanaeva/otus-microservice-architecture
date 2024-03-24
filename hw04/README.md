## HW04

### Деплой в minikube
- Запустить minikube:
    ```bash
    minikube start
    ```
- Установить PostgreSQL через Helm и создать БД *postgres* с юзером *postgres* и паролем *pgpass*:
    ```bash
    helm install mypostgresql oci://registry-1.docker.io/bitnamicharts/postgresql --set auth.postgresPassword=pgpass
    ```
- Получить информацию о сервисе: 
    ```bash
    kubectl describe service mypostgresql
    ```
- Настроить nginx ingress контроллер: 
    ```bash
    kubectl create namespace m && helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx/ && helm repo update && helm install nginx ingress-nginx/ingress-nginx --namespace m -f nginx-ingress.yaml
    ```
- Применить манифесты: 
    ```bash
    kubectl apply -f .deployment
    ```
- Получить minikube ip и добавить хост arch.homework в etc/hosts c этим ip:
    ```bash
    minikube ip
    ```
- Перейти в браузере по адресу http://arch.homework/health или http://arch.homework/docs (Swagger). Примеры работы приложения представлены в /examples.

### Примечание
Запуск команды выполнения первоначальных миграций не требуется, так как создание таблицы в БД настроено при запуске сервиса (через SQLAlchemy).

### Возникшие ошибки
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not translate host name "mypostgresql" to address: Temporary failure in name resolution

Временное решение: в db_host использован *Endpoints: 10.244.0.3:5432* из *kubectl describe service mypostgresql*. Минус решения заключается в том, что при перезапуске адрес обновляется.

Решение: ?
