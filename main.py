import telebot
import quote

bot = telebot.TeleBot('5890431517:AAGJSNiLm15UVt1Q0W5X25BGMUSsuxrdQZQ')

@bot.message_handler(commands=['start'])
def start(message):
    hello_user = f'What\'s UP, {message.from_user.first_name}'
    quote_bot = quote.print_quotes()
    bot.send_message(message.chat.id, hello_user)
    bot.send_message(message.chat.id, quote_bot)


# For my learn
# @bot.message_handler()
# def get_user_text(message):
#     bot.send_message(message.chat.id, message)

bot.polling(none_stop=True)
