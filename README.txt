Лабораторная работа 5
Коновалов Максим Алексеевич, УБВТ2301

Реализовал пять тестов в tests/test_user.py. Добавил сброс базы перед
каждым тестом. Все тесты прошли в Python 3.12. Собрал и запустил образ.

Локальный запуск тестов:
python -m pip install -r requirements.txt -r requirements-test.txt
python -m pytest tests/ -v

Сборка образа:
docker build -t mkonovalov-lab5:local .
docker run --rm -p 8090:8080 mkonovalov-lab5:local

Подготовил .github/workflows/tests.yml и build-and-delivery.yml.
Запуск в GitHub Actions и публикация на Docker Hub пока не выполнены.
Для завершения нужно подключить GitHub-репозиторий, задать переменную
DOCKERHUB_USERNAME и секрет DOCKERHUB_TOKEN в настройках Actions.
После push в dev должны пройти тесты, после слияния в main должны
пройти тесты, сборка и публикация my-app:latest.
Готового отчёта №5 пока нет: нужен фактический результат удалённого запуска.
