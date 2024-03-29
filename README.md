# api_yatube
Данный проект является домашней работой в рамках обучения в Яндекс.Практикум, модуль знакомства с API. В функционал входит макет учебного проекта yatube, а так же полноценно работающий CRUD.

Создатель проекта - студент Яндекс.Практикума Дмитрий Филимонов, telegram: @kelpyre

Для того, чтобы развернуть копию проекта, клонируйте его из репозитория, установите виртуальную среду (venv), и установите зависимости из файла requirements.txt

В рамках API доступен следующий функционал:
POST запросы к эндпоинту аутентификации (реализована при помощи TokenAuthentication);
GET, POST, PUT, PATCH, DELETE запросы к эндпоинтам модели Post;
GET, POST, PUT, PATCH, DELETE запросы к эндпоинтам модели Group;
GET запросы к эндпоинтам модели Group.

Примеры запросов и ответов API:

GET http://127.0.0.1:8000/api/v1/posts/ :

{
    "id": 1,
    "text": "Я тестирую API",
    "author": "one",
    "image": null,
    "group": 1,
    "pub_date": "2022-04-06T17:54:32.672085Z"
}

POST http://127.0.0.1:8000/api/v1/posts/ :

{
    "text": "Тестовый пост"
}

{
    "id": 6,
    "text": "Тестовый пост",
    "author": "one",
    "image": null,
    "group": null,
    "pub_date": "2022-04-07T09:17:55.390831Z"
}

GET http://127.0.0.1:8000/api/v1/posts/3/comments/ :

[
    {
        "id": 1,
        "author": "one",
        "post": 3,
        "text": "Первый коммент",
        "created": "2022-04-06T18:23:28.375884Z"
    }
]

PATCH http://127.0.0.1:8000/api/v1/posts/3/comments/1/ :

{
    "text": "Тестовый коммент"
}

{
    "id": 1,
    "author": "one",
    "post": 3,
    "text": "Тестовый коммент",
    "created": "2022-04-06T18:23:28.375884Z"
}
