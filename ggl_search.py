#!/usr/bin/env python3
"""
Webdriver test
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

    def openBrowser(self):
        bot = self.bot
        bot.get('https://google.com/')
        time.sleep(3)

    def search(self, key):
        bot = self.bot
        bot.get('https://google.com/')
        time.sleep(3)
        searchField = bot.find_element_by_class_name('gLFyf')
        #searchField.clear()
        searchField.send_keys(key)
        searchField.send_keys(Keys.RETURN)
        time.sleep(3)


callObj = selBot()
#callObj.openBrowser()
if(len(sys.argv)>1):
    callObj.search(str(sys.argv[1]))
else:
    callObj.search("tada")
    