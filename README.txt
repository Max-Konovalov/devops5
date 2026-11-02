Лабораторная работа 5
Коновалов Максим Алексеевич, УБВТ2301

Дописал тесты API, настроил тестирование, сборку и публикацию образа.
Тесты в dev и main прошли в GitHub Actions. Образ опубликован в Docker Hub.

Репозиторий: https://github.com/Max-Konovalov/devops5
Образ: maxkoyt/devops5:latest (также тег tagname)

Запуск опубликованного образа:
docker pull maxkoyt/devops5:latest
docker run --rm -p 8080:8080 maxkoyt/devops5:latest
Swagger: http://127.0.0.1:8080/docs

Локальные тесты:
python -m pip install -r requirements.txt -r requirements-test.txt
python -m pytest tests/ -v

Тесты запускаются при каждом push. После успешных тестов в main
запускается сборка и публикация. В Actions нужен секрет DOCKERHUB_TOKEN.
Значение токена не хранится в проекте.
