import telebot
from telebot import types
from const import WELCOME_MESS, ABOUT

bot = telebot.TeleBot()


def main():
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Заполнить анкету', callback_data='questionnaire')
        btn2 = types.InlineKeyboardButton('Узнать подробнее о чат-боте', callback_data='about')
        btn3 = types.InlineKeyboardButton('Карьерные социальные сети ГК "Росатом"', callback_data="network_career")
        btn4 = types.InlineKeyboardButton('Ближайшие карьерные мероприятия ГК "Росатом"', callback_data="career_events")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text=WELCOME_MESS, reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.message:
            if call.data == 'questionnaire':
                bot.send_message(call.message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
            elif call.data == 'about':
                bot.send_message(call.message.chat.id, text=ABOUT)

    bot.polling()


if __name__ == '__main__':
    main()
