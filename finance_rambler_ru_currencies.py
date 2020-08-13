#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
###################################################################################################################
def get_updates_html(url):
    try:
        proxies = {
                    "http": "socks5://localhost:9150",
                    "https": "socks5://localhost:9150"
        }
        headers = {
                    "User-Agent": UserAgent().chrome
        }
        r = requests.get(url, proxies = proxies, headers = headers)
        if r.status_code == 200:
            return r.text
        else:
            print("Ошибка! Ответ сервера: " + str(r.status_code))
    except Exception as e:
        pass
###################################################################################################################
def get_AMD():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/AMD/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_AUD():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/AUD/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_AZN():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/AZN/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_BGN():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/BGN/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_BRL():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/BRL/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_BYN():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/BYN/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_CAD():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/CAD/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_CHF():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/CHF/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_CNY():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/CNY/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_CZK():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/CZK/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_DKK():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/DKK/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_EUR():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/EUR/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_GBR():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/GBP/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_HUF():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/HUF/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_INR():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/INR/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_JPY():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/JPY/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_KGS():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/KGS/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_KRW():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/KRW/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_KZT():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/KZT/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_MDL():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/MDL/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_NOK():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/NOK/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_PLN():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/PLN/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_RON():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/RON/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_SEK():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/SEK/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_SGD():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/SGD/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_TJS():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/TJS/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_TMT():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/TMT/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_TRY():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/TRY/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_UAH():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/UAH/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_USD():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/USD/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_UZS():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/UZS/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_XDR():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/XDR/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
###################################################################################################################
def get_ZAR():
    try:
        url = "https://finance.rambler.ru/currencies/"
        updates_html = get_updates_html(url)
        soup = BeautifulSoup(updates_html, "lxml")
        div = soup.find("div", class_ = "finance-currency-table__body").find("a", href = "/currencies/ZAR/")
        title = div.get("title")
        value_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--value")
        value = re.sub(r"[^0-9.]+", r"", str(value_1))
        nominal_1 = div.find("div", class_ = "finance-currency-table__cell finance-currency-table__cell--denomination")
        nominal = re.sub(r"[^0-9.]+", r"", str(nominal_1))
        return "Цена за " + str(nominal) + " " + str(title) + " = " + str(value) + " рублей"
    except Exception as e:
        pass
