# Яндекс.Практикум

# курс Python-разработчик

## студент  Leonid Slavutin

![](https://avatars.githubusercontent.com/u/86873729?s=400&u=79ca75646b1a1eb2fade4f19d435a8ba65a1fe58&v=4)

## Учебный проект sprint_9.  API для Yatube.

***
Цель работы над проектом - получить навыки работы с **Django REST framework**.
Задание представляет из себя  по заданным правилам поведения АПИ и нескольким достаточно простым моделям со связанными отношениями реализовать логику работы АПИ.
***

Установка.

Клонировать репозиторий и перейти в его папку в командной строке:

```bash
git clone https://github.com/coherentus/api_final_yatube
```

```bash 
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```bash 
python -m venv venv
```

Для *nix-систем:

```bash 
source venv/bin/activate
```

Для windows-систем:

```bash 
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash 
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```bash 
cd yatube_api
python manage.py migrate
```

Создать суперпользователя django:

```bash 
python manage.py createsuperuser
```

Запустить проект:

```bash 
python manage.py runserver
```

Сам проект и админ-панель искать по адресам:

```
http://127.0.0.1:8000

http://127.0.0.1:8000/admin
```

***

Некоторые примеры запросов к API.

**Получение списка сообществ:**

эндпойнт:

```
/api/v1/groups/
```

разрешённые HTTP-методы:

```
GET
```

в ответе:

```python
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
response status code 200
```

**Создание подписки**

эндпойнт:
```
/api/v1/follow/
```

http-метод:
```
POST
```

Payload:
```python
{
  "following": "string"
}
```

Варианты ответов:
* удачное выполнение - статус 201 и созданный экземпляр подписки
```python
{
  "user": "string",
  "following": "string"
}
```

* отклонение запроса - статус 400 - пропущен обязательный параметр
```python
{
  "following": [
    "Обязательное поле."
  ]
}
```

* отклонение запроса - статус 401 - запрос от неаутенфицированного пользователя
```python
{
  "detail": "Учетные данные не были предоставлены."
}
```


Полный перечень запросов АПИ есть в ReDoc по адресу "ht<span>tp://127</span>.0.0.1:8000/redoc/"
