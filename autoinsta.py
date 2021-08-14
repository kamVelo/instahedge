"""
this file is a test file for the instabot library to attempt to post from python.
"""
file = open("login.txt", "r")
username = file.readline()
password = file.readline()
file.close()
from instabot import Bot
bot = Bot()
bot.login(username=username,password=password)
bot.upload_photo("utopia.jpg", caption="Testing for Utopia")
