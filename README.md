
# Описание
Это API для социальной сети с возможностью:

- Создания публикаций с текстом и изображениями

- Комментирования публикаций
- Создания сообществ (групп)
- Подписки на других пользователей

# Установка
1. Клонировать репозиторий
2. Создать виртуальное окружение и активировать его
``` 
python -m venv venv
. venv\Scripts\activate
```
3. Скачать зависимости
``` 
python.exe -m pip install --upgrade pip
pip install -r requirements.txt 
```
4. Миграции
```
python manage.py migrate
```
5. Запустить
```
python manage.py runserver
```

# Примеры

1. Аутентификация
Получить токены доступа:

```js
POST /api/v1/auth/jwt/create/
Content-Type: application/json

{
  "username": "ваш_логин",
  "password": "ваш_пароль"
}
```
Ответ:

```
{
  "refresh": "eyJhbGciOiJIUzI1Ni...",
  "access": "eyJhbGciOiJIUzI1Ni..."
}
```

2. Работа с публикациями
Получить список публикаций (с пагинацией):

```js
GET /api/v1/posts/?limit=10&offset=0
Authorization: JWT ваш_токен
```

Создать новую публикацию:

```js
POST /api/v1/posts/
Authorization: JWT ваш_токен
Content-Type: application/json

{
  "text": "Мой первый пост",
  "image": "data:image/png;base64,...",  # опционально
  "group": 1  # опционально
}
```

3. Комментарии
Добавить комментарий:

```js
POST /api/v1/posts/1/comments/
Authorization: JWT ваш_токен
Content-Type: application/json

{
  "text": "Отличный пост!"
}
```
4. Подписки
Подписаться на пользователя:

```js
POST /api/v1/follow/
Authorization: JWT ваш_токен
Content-Type: application/json

{
  "following": "username_автора"
}
```
5. Сообщества
Получить список сообществ:

```js
GET /api/v1/groups/
Authorization: JWT ваш_токен
Примеры ответов
Успешный запрос публикаций (200 OK):

json
{
  "count": 42,
  "next": "http://api.example.org/posts/?limit=10&offset=10",
  "previous": null,
  "results": [
    {
      "id": 1,
      "author": "username",
      "text": "Текст публикации...",
      "pub_date": "2023-01-01T12:00:00Z",
      "image": "/media/posts/image.jpg",
      "group": 1
    }
  ]
}
```
Ошибка аутентификации (401 Unauthorized):

```js
{
  "detail": "Учетные данные не были предоставлены."
}
```js
Ошибка валидации (400 Bad Request):

```js
{
  "text": ["Это поле обязательно."]
}
```
