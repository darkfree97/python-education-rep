import re
from fileProcessor import *


def search(reg, words):
    arr = []
    for word in words:
        reg_exp = re.search(reg, word, flags=0)
        if reg_exp is not None:
            arr.append(reg_exp.group())
    return arr


def textProcessor(text):
    words = text.split(" ")
    names_write(search("[A-Z][a-z]{1,15}|[А-ЯІЇЄ][а-яіїє]{1,15}", words))
    dates_write(search("\d\d\.\d\d\.\d\d\d\d|\d\d\/\d\d\/\d\d\d\d", words))
    mails_write(search("[A-z\.\_0-9]*@[A-z0-9]*\.[A-z0-9]*", words))
    phone_write(search("\+\d{5,13}|\d{5,13}", words))
