import os
import glob, os, os.path
#
# myDir = os.getcwd().replace('\\', '\\\\')
# print(myDir)
#
# filelist = glob.glob(os.path.join(myDir, "*.mp4"))
# for f in filelist:
#     os.remove(f)


# files = glob.glob(os.path.join('.', '*.mp4'))
# for i in files:
#     print(i)



import glob
import os.path
import classes
import json

files = glob.glob(os.path.join('.', '*.mp4'))
for i in files:
    filePath = i
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
                a2 = json.loads(a)
                a4 = a2['uploadpost']
                a3 = a4['uid']
                log.write(f"https://www.aparat.com/v/{a3}\n")
                formUrl = f"https://www.aparat.com/v/{a3}"
                print(f"🟢 ویدیو آپلود شد .\n🟣 نام ویدیو : {i}\n🟡 لینک ویدیو : {formUrl}")
            os.remove(filePath)
