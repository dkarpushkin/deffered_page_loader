##### Запуск
docker-compose up --build -d

##### Использование
###### установка задачи
POST http://127.0.0.1:5000/tags/?url=https://www.google.ru/
###### в ответ прийдет
{
    "status": 0,
    "async_task_id": "63cf1a85-c7f3-40c8-8806-f04d526c1500"
}
###### результат
http://127.0.0.1:5000/tags/<async_task_id>