import os
from http import HTTPStatus

import requests
from telebot import TeleBot, types
from dotenv import load_dotenv


load_dotenv()


DOMAIN = 'http://127.0.0.1:8000'
API_VERSION = 'api/v1'
GET_STUDY_LIST_URL = '{domain}/{api_version}/study/'
GET_STUDY_URL = '{domain}/{api_version}/study/{id}/'
GET_CATEGORY_LIST_URL = '{domain}/{api_version}/category/'


START_TEXT = ('Привет, {username}! Я бот проекта KARTStudy \U0001F916!'
              'Меня зовут Луни! \U0001F47B\n'
              'Я буду тебе помогать с поиском информации на нашем сайте! '
              'Наш проект в разработке, поэтому я буду только развиваться!')
GET_STUDY_LIST_TEXT = ('<b>Наши учебные материалы:</b>\n'
                       '\n<i>"Если справа от названия стоит \U00002705, '
                       'то курс готов и ждёт '
                       'своих учеников, а если название помечено '
                       'символом '
                       '\U0000274C, то курс ещё разрабатывается и уже скоро '
                       'будет опубликован!"</i>\n')
STUDY_CARD = ('\n<b>Автор курса:</b> {author}\n'
              '<b>ID:</b> {id}\n'
              '<b>Название курса:</b> {name} {is_published}\n'
              '<b>Слаг курса</b>: {slug}\n'
              '<b>Из категории:</b> {category}\n'
              '<b>Создан:</b> {created}\n')
GET_CATEGORY_LIST_TEXT = ('<b>Наши категории курсов:</b>\n'
                          '\n<i>"Если справа от названия стоит \U00002705, то '
                          ' категория опубликована, а если название помечено '
                          'символом '
                          '\U0000274C, то категория ещё разрабатывается '
                          'и уже скоро будет опубликован!"</i>\n')
CATEGORY_CARD = ('\n<b>Автор категории:</b> {author}\n'
                 '<b>Название категории:</b> {name} {is_published}\n'
                 '<b>Слаг категории</b>: {slug}\n'
                 '<b>Создана:</b> {created}\n')
ERROR_GET_STUDY_TEXT = ('Курса с таким id найдено не было(')
ERROR_GET_CATEGORY_TEXT = ('Невозможно получить категории(')
INFO = ('Это все, что я умею!\n'
        'Напиши: (Курс "<i>id курса</i>") - я выведу полную информацию '
        'об этой программе')
RESPONCE_FOR_VOICE = 'Я пока что не умею обрабатывать голосовые сообщения('
EMPTY_CATEGORY = 'Категория ещё не определена'


def get_date(date):
    return date.split('T')[0]


bot = TeleBot(token=os.getenv('TOKEN'), parse_mode='HTML')


@bot.message_handler(content_types=['voice'])
def response_for_voice(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=RESPONCE_FOR_VOICE
    )


@bot.message_handler(commands=['start'])
def say_hi(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton('/info'),
        types.KeyboardButton('/study_list'),
        types.KeyboardButton('/category_list'),
        types.KeyboardButton('/start'),
        row_width=3
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=START_TEXT.format(username=message.chat.username),
        reply_markup=keyboard
    )


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=INFO
    )


@bot.message_handler(commands=['study_list'])
def get_study_list(message):
    studies = requests.get(GET_STUDY_LIST_URL.format(
            domain=DOMAIN,
            api_version=API_VERSION
        )
    ).json()
    study_list = ''
    category = ''
    is_published = '\U00002705'
    for study in studies:
        if study.get('is_published') is False:
            is_published = '\U0000274C'
        if not study.get('category'):
            category = EMPTY_CATEGORY
        study_list += STUDY_CARD.format(
            author=study.get('author'),
            id=study.get('id'),
            is_published=is_published,
            name=study.get('name'),
            slug=study.get('slug'),
            category=category,
            created=get_date(study.get('created')),
        )
    bot.send_message(
        chat_id=message.chat.id,
        text=(GET_STUDY_LIST_TEXT + study_list),
    )


@bot.message_handler(func=lambda message: 'Курс ' in message.text)
def get_study(message):
    study_id = message.text.split()[1]
    try:
        study = requests.get(GET_STUDY_URL.format(
            domain=DOMAIN,
            api_version=API_VERSION,
            id=study_id
        ))
        if study.status_code != HTTPStatus.OK:
            raise Exception()
        if study.get('category'):
            category = EMPTY_CATEGORY
        study = study.json()
        is_published = '\U00002705'
        if study.get('is_published') is False:
            is_published = '\U0000274C'
        bot.send_message(
            chat_id=message.chat.id,
            text=STUDY_CARD.format(
                author=study.get('author'),
                name=study.get('name'),
                is_published=is_published,
                description=study.get('description'),
                category=category,
                created=get_date(study.get('created'))
            )
        )
    except Exception:
        bot.send_message(
            chat_id=message.chat.id,
            text=ERROR_GET_STUDY_TEXT
        )


@bot.message_handler(commands=['category_list'])
def get_category_list(message):
    try:
        response = requests.get(
            GET_CATEGORY_LIST_URL.format(
                domain=DOMAIN,
                api_version=API_VERSION
            )
        )
        category_list = ''
        if response.status_code == HTTPStatus.OK:
            for category in response.json():
                is_published = '\U00002705'
                if category.get('is_published') is False:
                    is_published = '\U0000274C'
                category_list += CATEGORY_CARD.format(
                    author=category.get('author'),
                    name=category.get('name'),
                    is_published=is_published,
                    slug=category.get('slug'),
                    created=get_date(category.get('created'))
                )
            bot.send_message(
                chat_id=message.chat.id,
                text=(GET_CATEGORY_LIST_TEXT + category_list)
            )
        else:
            raise Exception()
    except Exception:
        bot.send_message(
            chat_id=message.chat.id,
            text=ERROR_GET_CATEGORY_TEXT
        )


def main():
    bot.polling()


if __name__ == '__main__':
    main()
