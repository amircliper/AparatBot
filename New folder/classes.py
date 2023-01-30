import requests
import json
import glob, os, os.path

myDir = os.getcwd().replace('\\', '\\\\')


def clearStr(string):
    string2 = string.replace("📍 @JafarAbad 📍", "")
    string2 = string2.replace("🇯‌🇴‌🇮‌🇳 ↯", "")
    string2 = string2.replace("#ترفند", "")
    string2 = string2.replace("@RedLineTel 🚩", "")
    string2 = string2.replace("Join 🔜 ", "")
    string2 = string2.replace("@khandbazar20💯", "")
    string2 = string2.replace("🌐 @KHANDBAZAR20 🔚", "")
    return string2
    string2 = str(string).split(" ")
    for a in string2:
        if "@" in a:
            string2 = str(string).replace(a, "@TimRstun")
            break


def ReadNumber():
    with open("Number.txt", 'r') as file:
        number = int(file.read())
    with open("Number.txt", 'w') as file:
        file.write(str(number + 1))
    return str(number)


def ChangeUrlMode():
    with open("UrlMode.txt", 'r') as file:
        number = int(file.read())
    number = 1 - number
    with open("UrlMode.txt", 'w') as file:
        file.write(str(number))
    return str(number)


def ChangeHashatgMode():
    with open("HashtagMode.txt", 'r') as file:
        number = int(file.read())
    if number == 2:
        number = 0
    else:
        number += 1
    with open("HashtagMode.txt", 'w') as file:
        file.write(str(number))
    return str(number)

def ChangeCategoryMode():
    with open("CategoryMode.txt", 'r') as file:
        number = int(file.read())
    number = 1 - number
    with open("CategoryMode.txt", 'w') as file:
        file.write(str(number))
    return str(number)

def ChangeUploadMode():
    with open("UploadMode.txt", 'r') as file:
        number = int(file.read())
    number = 1 - number
    with open("UploadMode.txt", 'w') as file:
        file.write(str(number))
    return str(number)

def ReadUrlMode():
    with open("UrlMode.txt", 'r') as file:
        number = int(file.read())
    return str(number)

def ReadUploadMode():
    with open("UploadMode.txt", 'r') as file:
        number = int(file.read())
    return str(number)


def ReadHashtagMode():
    with open("HashtagMode.txt", 'r') as file:
        number = int(file.read())
    return str(number)

def ReadCategoryMode():
    with open("CategoryMode.txt", 'r') as file:
        number = int(file.read())
    return str(number)


def GetUrl(url, number):
    a = requests.get(url)
    geted = json.loads(a.text)
    geted2 = geted['uploadform']
    # file = open ("send.html" , 'r+')
    # readall = file.read()
    # readall2 = readall.split()
    # a = readall.replace(readall2[3] , "action=\"" + geted2['formAction'] + "\"")
    # file.close()
    # file = open(f"{str(number)}send.html" , 'w')
    # file.write(a)
    # file.close()
    return (geted2)


def OpenDriver(UploadUrl, caption, number, hashtagMode , category):
    url = UploadUrl['formAction']
    if hashtagMode == "0":
        hashtag = "طنز-خنده دار-بخند-خنده-کمدی"
    elif hashtagMode == "1":
        hashtag = "طنز-خنده دار-بخند-امیرکلیپر-amircliepr"
    elif hashtagMode == "2":
        hashtag = "موسیقی-آهنگ-سینا محمدی-sina mohammadi-موزیک"

    if category == "0":
        category = "2"
    elif category == "1":
        category = "7"
    payload = {'data[category]': category,
               'data[title]': caption,
               'data[tags]': hashtag,
               # 'data[tags]': 'گوشی موبایل-موبایل-آریا مارکت-آریامارکت-سامسونگ',
               'data[descr]': "ببین چه کلیپای باحالی میزارم ، فالو کن دیگه :(",
               # 'data[descr]': '✅ فروش انواع گوشی و تبلت با بهترین قیمت ✅ فروشگاه آریامارکت پیج اینستاگرام ما : @www_aria_store سایت ما : https://www.ariamarket.ir تلفن ما : 021-91311913',
               'frm-id': UploadUrl['frm-id']}
    files = [
        (
            'video', (f'{number}.mp4', open(f'{myDir}\\{number}.mp4', 'rb'),
                      'application/octet-stream'))
    ]

    response = requests.request("POST", url, data=payload, files=files)

    print(response.text)
    return response.text
    # driver = webdriver.Firefox()
    # driver.get(f"file:///D:/AparatTelegramBot/{str(number)}send.html")
    # print(UploadUrl['frm-id'])
    # print(UploadUrl['formAction'])
    # driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(
    #     f"D:\\AparatTelegramBot\\{number}.mp4")
    # driver.find_element_by_xpath('/html/body/form/input[2]').send_keys(UploadUrl['frm-id'])  # frmid
    # driver.find_element_by_xpath('/html/body/form/input[3]').send_keys(caption)  # title
    # driver.find_element_by_xpath('/html/body/form/input[4]').send_keys(2)  # IdTabagheBandi
    # # driver.find_element_by_xpath('/html/body/form/input[5]').send_keys("amircliper - امیرکلیپر - امیر کلیپر - amir cliper - خنده دار")  # tags
    # # driver.find_element_by_xpath('/html/body/form/input[5]').send_keys("موزیک - اهنگ - موسیقی - آهنگ جدید - موزیک جدید")  # tags
    # driver.find_element_by_xpath('/html/body/form/input[5]').send_keys("خنده - خنده دار - بخند - طنز - کمدی")  # tags
    # driver.find_element_by_xpath('/html/body/form/input[6]').send_keys(
    #     "ببین چه کلیپای باحالی میزارم دنبالمون کن دیگه :(")  # tozihat
    # driver.find_element_by_xpath('/html/body/form/input[7]').send_keys(Keys.ENTER)


