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
- Настроить nginx ingress контроллер: 
    ```bash
    kubectl create namespace m && helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx/ && helm repo update && helm install nginx ingress-nginx/ingress-nginx --namespace m -f nginx-ingress.yaml
    ```
- Применить манифесты, используя в secrets DB_HOST=mypostgresql.default.svc.cluster.local: 
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
