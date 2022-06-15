import telebot
from telebot import types, formatting

import random

bot = telebot.TeleBot('5471647024:AAHgIm0VhslMs4gVcIU47EBNBYnNoisl4Uo')

# массив с вариантами для путешествий, чтобы осуществить рандомный выбор места
travels = [
    (0, "Соловки", "./images/Solovki.jpeg", "Соловки"),
    (1, "Сахалин", "./images/Sahalin.jpeg", "Сахалин"),
    (2, "Башкирия", "./images/Bashkiria.jpeg", "Башкирия"),
    (3, "Украина/Молдавия", "./images/UkraineMoldovia.jpeg", "Украина/Молдавия"),
    (4, "Сербия", "./images/Serbia.jpeg", "Сербия"),
    (5, "Босния и Герцоговина", "./images/BosniaGerzog.jpeg", "Босния и Герцоговина"),
    (6, "Грузия", "./images/Georgia.jpeg", "Грузия"),
    (7, "Грузия", "./images/GeorgiaGastronom.jpeg", "Грузия"),
    (8, "Израиль", "./images/Israel.jpeg", "Израиль"),
    (9, "Турция", "./images/Turkey.jpeg", "Турция")
]


def main_menu_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row(types.KeyboardButton('Отправиться в путешествие!'))
    markup.row(types.KeyboardButton('Информация'), types.KeyboardButton('Помощь'))
    return markup


def go_travel():
    keyboard = [
        [types.InlineKeyboardButton('Регионы', callback_data='regions')],
        [types.InlineKeyboardButton('Вид отдыха', callback_data='type_travel')],
        [types.InlineKeyboardButton('Реши за меня', callback_data='random_travel')],
        [types.InlineKeyboardButton('Главное меню', callback_data='main_menu')]]
    mark = types.InlineKeyboardMarkup(keyboard)
    return mark


def regions():
    keyboard = [
        [types.InlineKeyboardButton('Россия', callback_data='russia')],
        [types.InlineKeyboardButton('Европа', callback_data='europe')],
        [types.InlineKeyboardButton('Азия', callback_data='asia')],
        [types.InlineKeyboardButton('Главное меню', callback_data='main_menu')]]
    mark = types.InlineKeyboardMarkup(keyboard)
    return mark


def russia():
    keyboard = [
        [types.InlineKeyboardButton('Соловки', callback_data='solovki')],
        [types.InlineKeyboardButton('Сахалин', callback_data='sahalin')],
        [types.InlineKeyboardButton('Башкирия', callback_data='bashkiria')],
        [types.InlineKeyboardButton('⬅️Назад', callback_data='regions')]]
    mark = types.InlineKeyboardMarkup(keyboard)
    return mark


def europe():
    keyboard = [
        [types.InlineKeyboardButton('Украина/Молдавия', callback_data='ukrainMoldavia')],
        [types.InlineKeyboardButton('Сербия', callback_data='serbia')],
        [types.InlineKeyboardButton('Босния и Герцоговина', callback_data='bosniaGerzogovina')],
        [types.InlineKeyboardButton('⬅️Назад', callback_data='regions')]]
    mark = types.InlineKeyboardMarkup(keyboard)
    return mark


def asia():
    keyboard = [
        [types.InlineKeyboardButton('Грузия', callback_data='georgia')],
        [types.InlineKeyboardButton('Израиль', callback_data='israel')],
        [types.InlineKeyboardButton('Турция', callback_data='turkey')],
        [types.InlineKeyboardButton('⬅️Назад', callback_data='regions')]]
    mark = types.InlineKeyboardMarkup(keyboard)
    return mark


def type_travel():
    keyboard = [
        [types.InlineKeyboardButton('Активный', callback_data='activ_travel')],
        [types.InlineKeyboardButton('Культурный', callback_data='cultural_travel')],
        [types.InlineKeyboardButton('Гастрономический', callback_data='gastronomic_travel')],
        [types.InlineKeyboardButton('Главное меню', callback_data='main_menu')]]
    mark = types.InlineKeyboardMarkup(keyboard)
    return mark


def activ_travel():
    keyboard = [
        [types.InlineKeyboardButton('Грузия', callback_data='georgia')],
        [types.InlineKeyboardButton('Соловки', callback_data='solovki')],
        [types.InlineKeyboardButton('Израиль', callback_data='israel')],
        [types.InlineKeyboardButton('⬅️Назад', callback_data='type_travel')]]
    mark = types.InlineKeyboardMarkup(keyboard)
    return mark


def cultural_travel():
    keyboard = [
        [types.InlineKeyboardButton('Англия', callback_data='england')],
        [types.InlineKeyboardButton('Турция', callback_data='turkey')],
        [types.InlineKeyboardButton('Украина/Молдавия', callback_data='ukrainMoldavia')],
        [types.InlineKeyboardButton('⬅️Назад', callback_data='type_travel')]]
    mark = types.InlineKeyboardMarkup(keyboard)
    return mark


def gastronomic_travel():
    keyboard = [
        [types.InlineKeyboardButton('Босния и Герцеговина', callback_data='bosniaGerzogovina')],
        [types.InlineKeyboardButton('Грузия', callback_data='georgia')],
        [types.InlineKeyboardButton('Сахалин', callback_data='sahalin')],
        [types.InlineKeyboardButton('⬅️Назад', callback_data='type_travel')]]
    mark = types.InlineKeyboardMarkup(keyboard)
    return mark


def website():
    keyboard = [
        [types.InlineKeyboardButton('Перейти к индивидуальному туру', url="https://www.sodis.ru")],
        [types.InlineKeyboardButton('Главное меню', callback_data='main_menu')]]
    mark = types.InlineKeyboardMarkup(keyboard)
    return mark


@bot.message_handler(commands=['start'])
def start(message):
    # проверка для невалидных имён
    if message.from_user.last_name is None:
        mess = f'Привет, <b>{message.from_user.first_name}!</b>' \
               f' Давай решим куда ты отправишься'
    else:
        mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}!</b>' \
               f' Давай решим куда ты отправишься'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=main_menu_keyboard())


@bot.message_handler(content_types=['text'])
def send_message(message):
    user_id = message.from_user.id

    if message.text == 'Отправиться в путешествие!':
        bot.send_message(user_id, 'Давай решим куда ты отправишься', reply_markup=go_travel())

    elif message.text == 'Информация':
        info = open("infotext.txt", "r", encoding="utf-8").read()
        bot.send_message(user_id, info, reply_markup=main_menu_keyboard())
        # bot.send_message(user_id, '<b>Информация</b>', parse_mode='html', reply_markup=main_menu_keyboard())

    elif message.text == 'Помощь':
        bot.send_message(user_id, '<b>Помощь</b>', parse_mode='html', reply_markup=main_menu_keyboard())

    elif message.text == 'Вид отдыха':
        pass
    elif message.text == 'Реши за меня':
        pass
    elif message.text == 'Соловки':
        bot.send_message(user_id, formatting.format_text(
            formatting.hbold("Заголовок\n"),
            "описание"
        ), parse_mode='HTML', reply_markup=website())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_id = call.from_user.id

    if call.data == "regions":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='В какую страну отправимся?', reply_markup=regions())

    elif call.data == "type_travel":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Вид отдыха:', reply_markup=type_travel())

    # стоит вынести в отдельную функцию
    elif call.data == "random_travel":
        random_int = random.randrange(start=0, stop=9)
        bingo = travels[random_int]
        photo = open(bingo[2], 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=bingo[3])

    elif call.data == "main_menu":
        bot.send_message(user_id, 'Главное меню:', reply_markup=main_menu_keyboard())

    elif call.data == "russia":
        photo1 = open("./images/Solovki.jpeg", 'rb')
        photo2 = open("./images/Sahalin.jpeg", 'rb')
        photo3 = open("./images/Bashkiria.jpeg", 'rb')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.row(types.KeyboardButton('Соловки'), types.KeyboardButton('Сахалин'),
                   types.KeyboardButton('Башкирия'))
        bot.send_message(user_id, "В какой регион отправимся?", reply_markup=markup)
        # caption = "1" - описание у фото
        bot.send_media_group(chat_id=call.message.chat.id,
                             media=[types.InputMediaPhoto(media=photo1, caption="1"),
                                    types.InputMediaPhoto(media=photo2, caption="2"),
                                    types.InputMediaPhoto(media=photo3, caption="3")])
        #
        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        #                       text='В какой регион отправимся?', reply_markup=russia())

    elif call.data == "europe":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='А в какую страну?', reply_markup=europe())

    elif call.data == "asia":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='А в какую страну?', reply_markup=asia())

    elif call.data == "activ_travel":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Куда отправимся?', reply_markup=activ_travel())

    elif call.data == "cultural_travel":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Куда отправимся?', reply_markup=cultural_travel())

    elif call.data == "gastronomic_travel":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Куда отправимся?', reply_markup=gastronomic_travel())

    elif call.data == "solovki":
        photo = open("./images/Solovki.jpeg", 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="описание")

    elif call.data == "sahalin":
        photo = open("./images/Sahalin.jpeg", 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="описание")

    elif call.data == "bashkiria":
        photo = open("./images/Bashkiria.jpeg", 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="описание")

    elif call.data == "ukrainMoldavia":
        photo = open("./images/UkraineMoldovia.jpeg", 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="описание")

    elif call.data == "serbia":
        photo = open("./images/Serbia.jpeg", 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="описание")

    elif call.data == "bosniaGerzogovina":
        photo = open("./images/BosniaGerzog.jpeg", 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="описание")

    elif call.data == "georgia":
        photo = open("./images/Georgia.jpeg", 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="описание")

    elif call.data == "israel":
        photo = open("./images/Israel.jpeg", 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="описание")

    elif call.data == "turkey":
        photo = open("./images/Turkey.jpeg", 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="описание")

    elif call.data == "england":
        photo = open("./images/Britain.jpeg", 'rb')
        bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="описание")


# TODO: подклеить к каждому описанию
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Перейти к индивидуальному туру", url="https://www.sodis.ru"))
#     bot.send_message(message.chat.id, "", reply_markup=markup)


bot.polling(none_stop=True)
