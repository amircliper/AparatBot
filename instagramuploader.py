from instapy_cli import client
from textwrap import dedent

username = "nayereabedini18"
password = "amir1345"

video = 'D:/amircliepr/E/AparatTelegramBot/AparatTelegramBot/hatami.jpg'

text = "hello welcome home"

with client(username, password) as cli:
    cli.upload(video, text)
