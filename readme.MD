# Описание приложения
   Api-сервис contacts: адресная книга, которая хранит имя, фамилию, email,
телефон и адрес.

# Требования для запуска

* docker

# Сборка и запуск приложения
```sh
cd contacts-api # Переходим в директорию contacts-api, если вдруг еще не находимся в ней
docker build . -t contacts-api:latest
docker run -d -p 8080:8080 contacts-api:latest
```
После завершения работы с приложением не забываем избавиться от контейнера
```sh
docker ps | grep contacts-api:latest
docker kill {CONTAINER_ID}
```

# Список представленных api-методов

1. GET /api/contacts - список всех контактов
```JSON
[
  {
    "id": 1,
    "email": "some_email@mail.ru",
    "first_name": "Michael",
    "last_name": "Lawson",
    "phone": "+79680000000",
    "country": "Russia",
    "city": "Moscow",
    "address": "125167, Leningradsky prospekt 39 bld. 79"
  },
  {
  "id": 2,
  "email": "adminl@mail.ru",
  "first_name": "Michael",
  "last_name": "Right",
  "phone": "+79680000001",
  "country": "Russia",
  "city": "Moscow",
  "address": "125167, Leningradsky prospekt 39 bld. 79"
  }
]
```

2. POST /api/contacts - добавление контакта 
   Принимает JSON вида, обязательными полями являются first_name и email 
   (email должен быть уникальный):
```JSON
{
  "email": "some_email_3@mail.ru",
  "first_name": "Jake",
  "last_name": "Watson",
  "phone": "+79680000099",
  "country": "United States",
  "city": "New York",
  "address": "125167, Leningradsky prospekt 39 bld. 79"
}
```

3. GET /api/contact/{CONTACT_ID} - просмотр одного контакта
```JSON
{
  "id": 3,
  "email": "some_email@mail.ru",
  "first_name": "Tobias",
  "last_name": "Michael",
  "phone": "+79680000000",
  "country": "Russia",
  "city": "Moscow",
  "address": "125167, Leningradsky prospekt 39 bld. 79"
}
```
4. DELETE /api/contact/{CONTACT_ID} - удаление контакта
4. PUT /api/contact/{CONTACT_ID} - изменение данных контакта
```JSON

{
  "email": "my_awersome_email@mail.ru"
}
```
