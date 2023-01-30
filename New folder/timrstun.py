from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram
import classes
import time

updater = Updater('1824433646:AAH3Ib1ZOPYDit2AUkXCFPyvPPQ2Jfk6gl8', use_context=True)


def start(update, context):
    i = 0
    while True :
        i += 1
        context.bot.send_message(chat_id=update.message.chat_id, text=f'پیام {str(i)}')
        time.sleep(1)
def downloader(update, context):
    caption = (str(classes.clearStr(update.message.caption)))
    # print(caption)
    # with open("Number.txt" , 'r') as file:
    #     number = int(file.read())
    # with open("Number.txt", 'w') as file:
    #     file.write(str(number + 1))
    # chat_id = update.message.chat_id
    print(update.message.video)
    context.bot.get_file(update.message.video).download("1.mp4")
    context.bot.send_message(chat_id=update.message.chat_id, text='Saved')
    # context.bot.send_video(chat_id=update.message.chat_id, video=open('1.mp4', 'rb'), caption=caption,
    #                       supports_streaming=True)
    context.bot.send_video(chat_id="-1001303129652", video=open('1.mp4', 'rb'), caption=caption,
                           supports_streaming=True)
    # context.bot.send_message(chat_id=chat_id, text=f'{str(number)}دریافت شد')
    # uploadform = classes.GetUrl("https://www.aparat.com/etc/api/upload​form/luser/digitalios/ltoken/febc7963946caffeeef87a83dd2675fa" , str(number))
    # a = classes.OpenDriver(uploadform , caption , number)
    # context.bot.send_message(chat_id=chat_id, text=f"آپلود شد {str(number)}")
    context.bot.send_message(chat_id=update.message.chat_id, text='siktir')
def post(update, context):
    caption = (str(classes.clearStr(update.message.text)))
    context.bot.send_message(chat_id=update.message.chat_id, text=caption)
    context.bot.send_message(chat_id="-1001303129652", text=caption)
def photo(update, context):
    caption = (str(classes.clearStr(update.message.caption)))
    # print(caption)
    # with open("Number.txt" , 'r') as file:
    #     number = int(file.read())
    # with open("Number.txt", 'w') as file:
    #     file.write(str(number + 1))
    # chat_id = update.message.chat_id
    print(update.message.photo)
    file_id = update.message.photo[-1].file_id
    context.bot.get_file(file_id = file_id).download("1.jpg")
    # context.bot.send_message(chat_id=update.message.chat_id, text='Saved')
    # context.bot.send_photo(chat_id=update.message.chat_id, photo=open('1.jpg', 'rb') , caption=caption)
    context.bot.send_photo(chat_id="-1001303129652", photo=open('1.jpg', 'rb'), caption=caption)
    # print(str(update.message.chat_id))
    # context.bot.send_message(chat_id=chat_id, text=f'{str(number)}دریافت شد')
    # uploadform = classes.GetUrl("https://www.aparat.com/etc/api/upload​form/luser/digitalios/ltoken/febc7963946caffeeef87a83dd2675fa" , str(number))
    # a = classes.OpenDriver(uploadform , caption , number)
    # context.bot.send_message(chat_id=chat_id, text=f"آپلود شد {str(number)}")
    context.bot.send_message(chat_id=update.message.chat_id, text='siktir')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.video, downloader))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo))
updater.dispatcher.add_handler(MessageHandler(Filters.document, post))
updater.dispatcher.add_handler(MessageHandler(Filters.text, post))

updater.start_polling()
updater.idle()
