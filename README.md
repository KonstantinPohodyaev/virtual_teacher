# Образовательный проект KARTStudy
## Навигация
- [Описание проекта](#description)
- [Техническая документация на API сервера](#API)
- [Как заполнить файл ```.env```](#env)
- [Как запустить проект](#start-project)
- [Техно-стек](#techno-stack)
- [Авторство](#author)


<a id="description">

## Описание проекта

</a>

>__KARTStudy__ - сайт, на котором вы можете подобрать себе образовательный курс для подготовки к экзаменам, вступительным испытаниям или просто для пополнения своих знаний. К сайту прилагается бот в Telegram, с помощью которого так же можно совершать все необходимые операции.

## Техническое описание

>KARTStudy реализован на базе фрэймворка Django и библиотеки pyTelegramBotAPI.  

### Логика

>Проект KARTStudy включает в себя БД, состоящую из таблиц Study, Category, Review, CustomUser, Document. 

#### Курсы - Study

Модель используется для хранения основной информации об образовательном курсе: название, описание и так далее.

#### Категории - Category

Каждый курс принадлежит к своей категории, которые описаны в модели Category. Она используется для построения логики и удобства поиска нужного учебного материала. 

#### Отзывы - Review
Модель используется для возможности написания отзывов к курсам.

#### Пользователь - CustomUser

*Права пользователей*
Любой посетитель сайта (в том числе неавторизованный) может посмотреть список всех курсов и категорий.  

Суперпользователь: 
- доступны все действия.

Преподаватель:
- просматривать неопубликованные материалы,
- редактировать или удалять свои курсы.

Студент:
- просматривать только опубликованные на главной странице курсы,
- просматривать профили преподавателей,
- оставлять отзывы.
  
Неаутентифицированный пользователь:
- просматривать доступные курсы и категории.

<a id="API">

### API

</a>

Документация в разработке

<a id="env">

## Как заполнить файл .env 

</a>

Откройте файл ```.env.example```  
- `APP_TITLE` - название проекта;
- `DATABASE_URL` - строка, формата ```dialect+driver://username:password@host:port/database```;
- `SECRET` - секретный ключ;
- `FIRST_SUPERUSER_EMAIL` - email для суперпользователя
- `FIRST_SUPERUSER_PASSWORD` - пароль  для суперпользователя  
- `TOKEN` - токен Telegram-бота
- `DEBUG` - режим дебага
- `SECRET_KEY` - секретный ключ django
- `DB_NAME` - имя БД
- `EMAIL_BACKEND` - email-backend
- `EMAIL_HOST` - адрес SMTP-сервера, который будет использоваться для отправки электронной почты.
- `EMAIL_PORT` - задаёт номер порта, который будет использоваться для соединения с SMTP-сервером.
- `EMAIL_USE_TLS` - задает отправку через протокол безопасности TLS
- `EMAIL_HOST_USER` - почта для авторизации на SMTP-сервере
- `EMAIL_HOST_PASSWORD` - пароль от почты для авторизации на SMTP-сервере
- `DEFAULT_FROM_EMAIL` - email по умолчанию для отправки почты через SMTP.

<a id="start-project">

## Как запустить проект

</a>  

Вам необходимо установить интепретатор [python](https://www.python.org/downloads/).

_Внимание! Команды ниже приведены для ОС Windows. для Linux вместо команды **python** нужно использовать **python3**_.

### Клонировать репозиторий и перейти в него в командной строке
```
git clone  https://github.com/KonstantinPohodyaev/virtual_teacher

cd virtual_teacher
```
### Создать виртуальное окружение
```
python -m venv venv
```
### Активировать виртуальное окружене
```
source venv/Scripts/activate
```
или
```
. venv/Scripts/activate
```
### Установить зависимости из файла requirements.txt
```
python -m pip install --update pip
pip install -r requirements.txt
```
### Применить миграции
```
python manage.py migrate
```

### Запуск сайта и API
```
python manage.py runserver
```
___
_После выполнения указанных команд вы сможете успешно пользоваться функционалом нашего образовательного сервиса RARTStudy

<a id="techno-stack">

## Техно-стек :bulb:

</a>

### backend
:small_orange_diamond: python  
:small_orange_diamond: django  
:small_orange_diamond: django-rest-framework  
:small_orange_diamond: djoser  
:small_orange_diamond: simple-jwt  
:small_orange_diamond: python-dotenv  
:small_orange_diamond: pyTelegramBotAPI  
:small_orange_diamond: requests  


<a id="author">

## Авторство

</a>

Разработчик: [Konstantin Pohodyaev](https://github.com/KonstantinPohodyaev)  
Телеграм: `kspohodyaev`
