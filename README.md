# IIS
ISCRA Information System</br>
Приложения:
* ~~accounts - авторизация в системе~~
* departments - отделы
* events - мероприятия 
* people - люди
</br>

Фикстуры:
* users.json (пользователь admin, пароль 8Xgex7E6CRCF4wz)

API:
* /api/v1/people/ - список людей
  * /api/v1/people/\<pk:int>/ - человек pk
  * /api/v1/people/\<pk:int>/get_departments - отделы человека pk
  * /api/v1/people/\<pk:int>/get_events - мероприятия человека pk
* /api/v1/events/ - список мероприятий
  * /api/v1/events/\<pk:int>/ - мероприятие pk
* /api/v1/departments/ - список отделов
  * /api/v1/departments/\<pk:int>/ - отдел pk

Для запуска:
* В корне проекта создать файл `.env`
* В `.env` добавить переменные:
  * APP_KEY - секретный ключ приложения
  * DB_PORT - порт подключения в бд
  * DB_USER - имя пользователя бд
  * DB_PASSWORD - пароль от бд
  * DB_NAME - имя бд
* Создать бд (PostgreSQL) с указанными выше параметрами
* Если запускать с докером, то в корне проекта:
  * `docker-compose build`
  * `docker-compose up -d`
* Если запуск без докера, то в корне:
  * `cd IIS`
  * `python manage.py migrate`
  * `python manage.py loaddata fixtures/users.json`