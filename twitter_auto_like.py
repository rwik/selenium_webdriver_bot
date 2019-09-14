#!/usr/bin/env python3
"""
Webdriver twt liker
"""
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


__author__ = "Rwik"
__version__ = "0.1.0"
__license__ = "MIT"


class selBot:
    def __init__(self):
        self.bot = webdriver.Chrome()

 

    def likeTwts(self, key):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        user = bot.find_element_by_name('session[username_or_email]')
        passW = bot.find_element_by_name('session[password]')
        #user.clear()
        #passW.clear()
        user.send_keys('rwik')
        passW.send_keys('agdumbagdum')
        passW.send_keys(Keys.RETURN)
        time.sleep(3)

callObj = selBot()

if(len(sys.argv)>1):
    callObj.likeTwts(str(sys.argv[1]))
else:
    callObj.likeTwts("india")
    