import requests

def test_resume_api():
    url = "http://127.0.0.1:8000/user/get_skills"
    resume_text = """
    Иван Иванов
    Email: ivan.ivanov@example.com
    Телефон: +7 900 123-45-67

    Опыт работы:
    - Backend-разработчик в компании ООО «ТехСтар» (2022-2025)
      Работа с Python, FastAPI, PostgreSQL, Docker.
    - Стажер в компании «ВебСервис» (2021-2022)
      Разработка REST API, работа с Git и Linux.

    Образование:
    - Бакалавр по специальности «Программная инженерия», МГУ, 2018-2022

    Ключевые навыки:
    - Python
    - FastAPI
    - PostgreSQL
    - Docker
    - Git
    - Linux
    - REST API
    - SQL
    - Опыт работы с асинхронным программированием

    Дополнительно:
    - Английский язык — уровень B2
    - Навыки командной работы и коммуникации
    """

    payload = {"text": resume_text}
    response = requests.post(url, json=payload)
    print(response.status_code)
    print(response.json())

# Вызов функции
test_resume_api()
