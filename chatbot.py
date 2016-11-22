import telepot
import sys
import time
from pprint import pprint
import requests





bot = telepot.Bot('287024051:AAGXlgHbyEf649jvKjGSz80gaGRAQS3mqSI')



from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Press me', callback_data='press')],
               ])

    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')

# TOKEN = sys.argv[1]  # get token from command-line

# bot = telepot.Bot(TOKEN)
telepot.Bot('287024051:AAGXlgHbyEf649jvKjGSz80gaGRAQS3mqSI')
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query})
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)