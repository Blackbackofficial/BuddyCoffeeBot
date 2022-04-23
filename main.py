import telebot
from telebot import types
from const import WELCOME_MESS, ABOUT, NETWORK_CAREER

bot = telebot.TeleBot("")


def main():
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Заполнить анкету', callback_data='questionnaire')
        btn2 = types.InlineKeyboardButton('Узнать подробнее о чат-боте', callback_data='about')
        btn3 = types.InlineKeyboardButton('Карьерные социальные сети ГК "Росатом"', callback_data="network_career")
        markup.row(btn1, btn2)
        markup.row(btn3)
        bot.send_message(message.chat.id, text=WELCOME_MESS, reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.message:
            if call.data == 'questionnaire':
                bot.send_message(call.message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
            elif call.data == 'about':
                bot.send_message(call.message.chat.id, text=ABOUT)
            elif call.data == 'network_career':
                markup = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton('ВКонтакте', url='https://vk.com/rosatomcareer')
                btn2 = types.InlineKeyboardButton('Instagram', url='https://www.instagram.com/rosatom_career/?hl=ru')
                btn3 = types.InlineKeyboardButton('Назад', callback_data="back")
                markup.row(btn1, btn2)
                markup.row(btn3)
                bot.send_message(call.message.chat.id, text=NETWORK_CAREER, reply_markup=markup)
            elif call.data == 'back':
                send_welcome(call.message)
            else:
                bot.send_message(call.message.chat.id, text="Что-то пошло не так.")

    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
