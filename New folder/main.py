from email import message
import json
import time

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram
import classes
import glob, os, os.path

updater = Updater('1824433646:AAH3Ib1ZOPYDit2AUkXCFPyvPPQ2Jfk6gl8', use_context=True)
adminChatId = 188775642
myDir = os.getcwd().replace('\\', '\\\\')


def start(update, context):
    if update.message.chat_id == adminChatId:
        context.bot.send_message(chat_id=adminChatId, text='Hi This Is Clara Speaking , Welcome Back Grand MASTER .')
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text='Hi And Welcome To APARAT BOT . ')
        context.bot.send_message(chat_id=update.adminChatId,
                                 text=f"Has Been Started Bot : {str(update.message.chat_id)}")
        print("Has Been Started Bot : ", str(update.message.chat_id))


def restart(update, context):
    if update.message.chat_id == adminChatId:
        with open("Number.txt", 'w') as file:
            file.write("1")
        filelist = glob.glob(os.path.join(myDir, "*.mp4"))
        for f in filelist:
            os.remove(f)
        context.bot.send_message(chat_id=adminChatId, text='🟢 اعداد ویدیو ها ریستارت شد .\n🟢 همه ویدیو ها پاک شدند .')
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text='You Are Not Admin , Cant Change Number .')


def changeurlmode(update, context):
    if update.message.chat_id == adminChatId:
        number = classes.ChangeUrlMode()
        if number == "1":
            context.bot.send_message(chat_id=adminChatId, text='🟢 حالت ارسال تغییر کرد به ALL')
        if number == "0":
            context.bot.send_message(chat_id=adminChatId, text='🟢 حالت ارسال تغییر کرد به DIGITALIOS')
    else:
        context.bot.send_message(chat_id=adminChatId, text='You Are Not Admin . ')


def changehashtagmode(update, context):
    if update.message.chat_id == adminChatId:
        number = classes.ChangeHashatgMode()
        if number == "1":
            context.bot.send_message(chat_id=adminChatId, text='🟢 حالت هشتگ ها تغییر کرد به AMIRCLIPER')
        if number == "0":
            context.bot.send_message(chat_id=adminChatId, text='🟢 حالت هشتگ ها تغییر کرد به COMODY')
        if number == "2":
            context.bot.send_message(chat_id=adminChatId, text='🟢 حالت هشتگ ها تغییر کرد به SINA MOHAMMADI')
    else:
        context.bot.send_message(chat_id=adminChatId, text='You Are Not Admin . ')


def changecategorymode(update, context):
    if update.message.chat_id == adminChatId:
        number = classes.ChangeCategoryMode()
        if number == "1":
            context.bot.send_message(chat_id=adminChatId, text='🟢 طبقه بندی انتشار ویدیو ها تغییر کرد به MUSIC')
        if number == "0":
            context.bot.send_message(chat_id=adminChatId, text='🟢 طبقه بندی انتشار ویدیو ها تغییر کرد به TANZ')
    else:
        context.bot.send_message(chat_id=adminChatId, text='You Are Not Admin . ')


def changeuploadmode(update, context):
    if update.message.chat_id == adminChatId:
        number = classes.ChangeUploadMode()
        if number == "1":
            context.bot.send_message(chat_id=adminChatId, text='🟢 نحوه ارسال ویدیو ها تغییر کرد به SUPER')
        if number == "0":
            context.bot.send_message(chat_id=adminChatId, text='🟢 نحوه ارسال ویدیو ها تغییر کرد به NORMAL')
    else:
        context.bot.send_message(chat_id=adminChatId, text='You Are Not Admin . ')


def downloader(update, context):
    if classes.ReadUploadMode() == "0":
        caption = (str(classes.clearStr(update.message.caption)))
        print(caption)
        number = classes.ReadNumber()

        chat_id = update.message.chat_id

        context.bot.get_file(update.message.video).download(f"{str(number)}.mp4")

        log = open("log.txt", 'r+')

        context.bot.send_message(chat_id=chat_id, text=f'{str(number)}دریافت شد')
        urlModeNumber = classes.ReadUrlMode()
        if urlModeNumber == "0":
            fileName = "digitalios.txt"
        elif urlModeNumber == "1":
            fileName = "URLS.txt"

        with open(file=fileName, mode='r') as file:
            with open("log.txt", 'a+') as log:
                while (True):
                    url = file.readline()
                    if url == "end":
                        break
                    uploadform = classes.GetUrl(url, str(number))
                    a = classes.OpenDriver(uploadform, caption, number, classes.ReadHashtagMode(),
                                           classes.ReadCategoryMode())
                    context.bot.send_message(chat_id=chat_id, text=f"{a} : {url.split('/')[7]}")
                    try:
                        a2 = json.loads(a)
                        a4 = a2['uploadpost']
                        a3 = a4['uid']
                        log.write(f"https://www.aparat.com/v/{a3}\n")
                    except:
                        context.bot.send_message(chat_id=chat_id, text=f"مشکلی پیش آمد .")
            context.bot.send_message(chat_id=chat_id, text=f"آپلود به اتمام رسید")
            time.sleep(10)
    else:
        caption = (str(classes.clearStr(update.message.caption))).replace("\n", "")
        print(caption)
        chat_id = update.message.chat_id

        context.bot.get_file(update.message.video).download(f"{str(caption)}.mp4")
        context.bot.send_message(chat_id=chat_id, text=f'🟢 ویدیو با نام {str(caption)} ذخیره شد')


def uploadall(update, context):
    # caption = (str(classes.clearStr(update.message.caption)))
    # print(caption)
    # number = classes.ReadNumber()
    #
    chat_id = update.message.chat_id
    #
    # context.bot.get_file(update.message.video).download(f"{str(number)}.mp4")
    #
    # log = open("log.txt", 'r+')
    #
    # context.bot.send_message(chat_id=chat_id, text=f'{str(number)}دریافت شد')

    files = glob.glob(os.path.join('.', '*.mp4'))
    for i in files:
        i = i.replace(".\\", "").replace(".mp4", "")
        urlModeNumber = classes.ReadUrlMode()
        if urlModeNumber == "0":
            fileName = "digitalios.txt"
        elif urlModeNumber == "1":
            fileName = "URLS.txt"

        with open(file=fileName, mode='r') as file:
            with open("log.txt", 'a+') as log:
                while (True):
                    url = file.readline()
                    if url == "end":
                        break
                    uploadform = classes.GetUrl(url, i)
                    a = classes.OpenDriver(uploadform, i, i, classes.ReadHashtagMode(),
                                           classes.ReadCategoryMode())
                    try:
                        a2 = json.loads(a)
                        a4 = a2['uploadpost']
                        a3 = a4['uid']
                        log.write(f"https://www.aparat.com/v/{a3}\n")
                        formUrl = f"https://www.aparat.com/v/{a3}"
                        context.bot.send_message(chat_id=chat_id, text=f"🟢 ویدیو آپلود شد .\n🟣 نام ویدیو : {i}\n🟡 لینک ویدیو : {formUrl}")
                    except:
                        formUrl = f"https://www.aparat.com/v/"
                        context.bot.send_message(chat_id=chat_id,
                                                 text=f"error")
            context.bot.send_message(chat_id=chat_id, text=f"🟢 ویدیو آپلود شد .\n🟣 نام ویدیو : {i}\n🟡 لینک ویدیو : {formUrl}")


def post(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Cant Understand What Are You Talking About . ")


def photo(update, context):
    caption = (str(classes.clearStr(update.message.caption)))
    # print(caption)
    # with open("Number.txt" , 'r') as file:
    #     number = int(file.read())
    # with open("Number.txt", 'w') as file:
    #     file.write(str(number + 1))
    # chat_id = update.message.chat_id
    context.bot.get_file(update.message.video).download("1.jpg")
    context.bot.send_message(chat_id=update.message.chat_id, text='Saved')
    context.bot.send_photo(chat_id=update.message.chat_id, video=open('1.jpg', 'rb'), caption=caption,
                           supports_streaming=True)
    context.bot.send_photo(chat_id="-1001303129652", video=open('1.jpg', 'rb'), caption=caption,
                           supports_streaming=True)
    print(str(update.message.chat_id))
    # context.bot.send_message(chat_id=chat_id, text=f'{str(number)}دریافت شد')
    # uploadform = classes.GetUrl("https://www.aparat.com/etc/api/upload​form/luser/digitalios/ltoken/febc7963946caffeeef87a83dd2675fa" , str(number))
    # a = classes.OpenDriver(uploadform , caption , number)
    # context.bot.send_message(chat_id=chat_id, text=f"آپلود شد {str(number)}")
    context.bot.send_message(chat_id=update.message.chat_id, text='siktir')


def seeall(update, context):
    videoNumber = 0
    chat_id = update.message.chat_id
    files = glob.glob(os.path.join('.', '*.mp4'))
    for i in files:
        videoNumber += 1
    urlMode = classes.ReadUrlMode()
    if urlMode == "0":
        urlMode = "DIGITALIOS"
    elif urlMode == "1":
        urlMode = "ALL"
    hashtagMode = classes.ReadHashtagMode()
    if hashtagMode == "1":
        hashtagMode = "AMIRCLIPER"
    if hashtagMode == "0":
        hashtagMode = "COMODY"
    if hashtagMode == "2":
        hashtagMode = "SINA MOHAMMADI"
    categoryMode = classes.ReadCategoryMode()
    if categoryMode == "1":
        categoryMode = "MUSIC"
    if categoryMode == "0":
        categoryMode = "TANZ"
    uploadMode = classes.ReadUploadMode()
    if uploadMode == "1":
        uploadMode = "SUPER"
    if uploadMode == "0":
        uploadMode = "NORMAL"
    context.bot.send_message(chat_id=chat_id, text=f'⚪ همه حالت های موجود :\n\n⚪ تعداد ویدیو های موجود : {videoNumber}\n⚪ حالت ارسال : {urlMode}\n⚪ حالت هشتگ ها : {hashtagMode}\n⚪ حالت طبقه بندی انتشار ویدیو ها : {categoryMode}\n⚪ نحوه ارسال ویدیو ها : {uploadMode}')



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('changeurlmode', changeurlmode))
updater.dispatcher.add_handler(CommandHandler('restart', restart))
updater.dispatcher.add_handler(CommandHandler('changehashtagmode', changehashtagmode))
updater.dispatcher.add_handler(CommandHandler('changecategorymode', changecategorymode))
updater.dispatcher.add_handler(CommandHandler('changeuploadmode', changeuploadmode))
updater.dispatcher.add_handler(CommandHandler('uploadall', uploadall))
updater.dispatcher.add_handler(CommandHandler('seeall', seeall))
updater.dispatcher.add_handler(MessageHandler(Filters.video, downloader))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, downloader))

updater.dispatcher.add_handler(MessageHandler(Filters.document, post))
updater.dispatcher.add_handler(MessageHandler(Filters.text, post))

updater.start_polling()
updater.idle()
