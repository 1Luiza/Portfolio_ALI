import telebot
import requests

API_URL = 'https://7012.deeppavlov.ai/model'

API_TOKEN = '7060507984:AAGqsFHUVrUMSdLKYCRhCI4M_ebeSEmraqw'
bot = telebot.TeleBot(API_TOKEN)


def calculate_future_value(PV, i, n):
    """
    Функция для рассчета будущей стоимости денег с учетом инфляции
    :param PV: стоимость денег в настоящем времени
    :param i: ставка инфляции
    :param n: количество лет до достижения желаемой суммы
    :return:
    """
    FV = PV * ((1 + i) ** n)
    return FV


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Привет! Этот бот поможет вам рассчитать будущую стоимость денег с учетом инфляции.")
    bot.send_message(message.chat.id, "Введите начальную сумму (PV):")
    bot.register_next_step_handler(message, ask_PV)


def ask_PV(message):
    try:
        PV = float(message.text)
        bot.send_message(message.chat.id,
                         "Введите годовую процентную ставку инфляции в долях:")
        bot.register_next_step_handler(message, ask_interest_rate, PV)
    except ValueError:
        bot.send_message(message.chat.id,
                         "Начальная сумма должна быть числом. Попробуйте еще раз.")


def ask_interest_rate(message, PV):
    try:
        i = float(message.text)
        bot.send_message(message.chat.id,
                         "Введите количество лет:")
        bot.register_next_step_handler(message, send_future_value, PV, i)
    except ValueError:
        bot.send_message(message.chat.id,
                         "Процентная ставка должна быть числом. Попробуйте еще раз.")


def send_future_value(message, PV, i):
    try:
        n = int(message.text)
        future_value = calculate_future_value(PV, i, n)
        bot.send_message(message.chat.id,
                         f"Будущая стоимость: {future_value:.2f}")
    except ValueError:
        bot.send_message(message.chat.id,
                         "Количество периодов должно быть целым числом. Попробуйте еще раз.")


@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = " ".join(quest)
    data = {'question_raw': [qq]}
    try:
        res = requests.post(API_URL, json=data, verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Что-то я ничего не нашел :-(")


bot.polling()
