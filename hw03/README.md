## HW03 Основы работы с Kubernetes

### Деплой в minikube
- Запустить minikube:
    ```bash
    minikube start
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
- Создать туннель: 
    ```bash
    minikube tunnel
    ```
- Перейти в браузере по адресу http://arch.homework/health или http://arch.homework/docs (Swagger). Примеры работы приложения представлены в /examples.
