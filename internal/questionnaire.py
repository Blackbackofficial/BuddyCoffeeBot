from psycopg2.errors import UniqueViolation, StringDataRightTruncation
from config.conf import bot, conn
from internal.const import FIRST_NAME, SECOND_NAME, DIRECTION

INSERT_FIRST_NAME = 'INSERT INTO applicant (first_name, tg_id) VALUES (%s, %s);'
INSERT_LAST_NAME = 'UPDATE applicant SET last_name=%s WHERE applicant.tg_id=%s;'


def applicant_questionnaire(message):
    bot.send_message(message.chat.id, text=FIRST_NAME)
    bot.register_next_step_handler(message, check_first_name)


def check_first_name(message):
    cursor = conn.cursor()
    data = (message.text, message.chat.username)
    try:
        cursor.execute(INSERT_FIRST_NAME, data)
        conn.commit()
        bot.send_message(message.chat.id, "Запомнил")
        bot.send_message(message.chat.id, text=SECOND_NAME)
        bot.register_next_step_handler(message, check_last_name)
    except UniqueViolation:
        bot.send_message(message.chat.id, "Уже помню")
        bot.send_message(message.chat.id, text=SECOND_NAME)
        bot.register_next_step_handler(message, check_last_name)
        conn.rollback()
    except StringDataRightTruncation:
        bot.send_message(message.chat.id, "Длинный текст")
        bot.send_message(message.chat.id, text=FIRST_NAME)
        bot.register_next_step_handler(message, check_first_name)
        conn.rollback()


def check_last_name(message):
    cursor = conn.cursor()
    data = (message.text, message.chat.username)
    try:
        cursor.execute(INSERT_LAST_NAME, data)
        conn.commit()
        bot.send_message(message.chat.id, text=DIRECTION)
        bot.register_next_step_handler(message, check_direction)
    except StringDataRightTruncation:
        bot.send_message(message.chat.id, "Длинный текст")
        bot.send_message(message.chat.id, text=SECOND_NAME)
        bot.register_next_step_handler(message, check_last_name)
        conn.rollback()


def check_direction(message):
    check_direction