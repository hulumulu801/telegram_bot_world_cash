#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import pickle
import requests
from datetime import datetime
from finance_rambler_ru_currencies import get_AMD
from finance_rambler_ru_currencies import get_AUD
from finance_rambler_ru_currencies import get_AZN
from finance_rambler_ru_currencies import get_BGN
from finance_rambler_ru_currencies import get_BRL
from finance_rambler_ru_currencies import get_BYN
from finance_rambler_ru_currencies import get_CAD
from finance_rambler_ru_currencies import get_CHF
from finance_rambler_ru_currencies import get_CNY
from finance_rambler_ru_currencies import get_CZK
from finance_rambler_ru_currencies import get_DKK
from finance_rambler_ru_currencies import get_EUR
from finance_rambler_ru_currencies import get_GBR
from finance_rambler_ru_currencies import get_HUF
from finance_rambler_ru_currencies import get_INR
from finance_rambler_ru_currencies import get_JPY
from finance_rambler_ru_currencies import get_KGS
from finance_rambler_ru_currencies import get_KRW
from finance_rambler_ru_currencies import get_KZT
from finance_rambler_ru_currencies import get_MDL
from finance_rambler_ru_currencies import get_NOK
from finance_rambler_ru_currencies import get_PLN
from finance_rambler_ru_currencies import get_RON
from finance_rambler_ru_currencies import get_SEK
from finance_rambler_ru_currencies import get_SGD
from finance_rambler_ru_currencies import get_TJS
from finance_rambler_ru_currencies import get_TMT
from finance_rambler_ru_currencies import get_TRY
from finance_rambler_ru_currencies import get_UAH
from finance_rambler_ru_currencies import get_USD
from finance_rambler_ru_currencies import get_UZS
from finance_rambler_ru_currencies import get_XDR
from finance_rambler_ru_currencies import get_ZAR
global update_id_last
update_id_last = 0
#############################################################################################################################################################################################################################################
def write_token(token):
    path_token_folder = "./" + "token.pickle"
    with open(path_token_folder, "wb") as f:
        pickle.dump(token, f)
    abs_path_token_folder = os.path.abspath(path_token_folder)
    return abs_path_token_folder
#############################################################################################################################################################################################################################################
def read_and_return_token(tn):
    if not os.path.exists(tn):
        print("Файл с токеном отсутствует! \nПовторите попытку!")
    else:
        with open(str(tn), "rb") as f_1:
            data_token = pickle.load(f_1)
            return str(data_token)
#############################################################################################################################################################################################################################################
def get_updates(URL, bot_token):
    url = URL + str(bot_token) + "/getUpdates"
    r = requests.get(url)
    return r.json()
#############################################################################################################################################################################################################################################
def get_user_id_chat_id_text(updates):
    current_update_id = updates["result"][-1]["update_id"]
    global update_id_last
    if update_id_last != current_update_id:
        update_id_last = current_update_id

        user_id = updates["result"][-1]["message"]["chat"]["id"]
        text = updates["result"][-1]["message"]["text"]

        message = {
                    "user_id": user_id,
                    "current_update_id": current_update_id,
                    "text": text
        }
        return message
    return None
#############################################################################################################################################################################################################################################
def get_updates_ava(URL, bot_token, user_id):
    url = URL + str(bot_token) + "/getUserProfilePhotos?user_id=" + str(user_id)
    r = requests.get(url)
    json = r.json()
    total_count = json["result"]["total_count"]
    if total_count >= 1:
        links = []
        files_id = json["result"]["photos"]
        for file_id in files_id:
            for f_d in file_id:
                id_file = f_d["file_id"]
                links.append(id_file)
        return links
    else:
        print("У пользователя с id: " + str(user_id) + " нет аватарки!")
        return total_count
#############################################################################################################################################################################################################################################
def save_ava(user_id, get_file):
    folder = "./jpg/" + str(user_id)
    name_file = str(get_file).split("/")[-1]
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.abspath(folder)
    abs_path = path + "/" + name_file
    download_file = requests.get(get_file, allow_redirects = True)
    with open(abs_path, "wb") as f:
        for chunk in download_file.iter_content(8192):
            f.write(chunk)
#############################################################################################################################################################################################################################################
def get_file_ava(URL, bot_token, files_id, user_id):
    if not files_id == 0:
        for file_id in files_id:
            url = URL + bot_token + "/getFile?file_id=" + str(file_id)
            r_1 = requests.get(url)
            r = r_1.json()
            file_path = r["result"]["file_path"]
            get_file = "https://api.telegram.org/file/bot" + bot_token + "/" + file_path
            save_ava(user_id, get_file)
#############################################################################################################################################################################################################################################
def save_history_message(user_id, text):
    folder = "./history_message/" + str(user_id)
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.abspath(folder)
    abs_path = path + "/" + str(user_id) + ".txt"
    with open(str(abs_path), "a+") as f:
        t = "\nВремя: " + str(datetime.now()) + "\nПользователь с id: " + str(user_id) + "\nСообщение: " + str(text) + "\n" + "#" * 50
        f.write(str(t))
#############################################################################################################################################################################################################################################
def send_message(URL, bot_token, user_id, text_message):
    url = URL + bot_token + "/sendMessage?chat_id={}&text={}".format(user_id, text_message)
    requests.get(url)
#############################################################################################################################################################################################################################################
def main():
        try:
            while True:
                URL = "https://api.telegram.org/bot"
                token = sys.argv[1]
                tn = write_token(token)
                bot_token = read_and_return_token(tn)
                updates = get_updates(URL, bot_token)
                answer = get_user_id_chat_id_text(updates)
                if answer != None:
                    user_id = answer["user_id"]
                    text = answer["text"]
                    ava = get_file_ava(URL, bot_token, get_updates_ava(URL, bot_token, user_id), user_id)
                    history_message = save_history_message(user_id, text)
                    if text.upper() == "/AMD":
                        send_message(URL, bot_token, user_id, get_AMD())
                    elif text.upper() == "/AUD":
                        send_message(URL, bot_token, user_id, get_AUD())
                    elif text.upper() == "/AZN":
                        send_message(URL, bot_token, user_id, get_AZN())
                    elif text.upper() == "/BGN":
                        send_message(URL, bot_token, user_id, get_BGN())
                    elif text.upper() == "/BRL":
                        send_message(URL, bot_token, user_id, get_BRL())
                    elif text.upper() == "/BYN":
                        send_message(URL, bot_token, user_id, get_BYN())
                    elif text.upper() == "/CAD":
                        send_message(URL, bot_token, user_id, get_CAD())
                    elif text.upper() == "/CHF":
                        send_message(URL, bot_token, user_id, get_CHF())
                    elif text.upper() == "/CNY":
                        send_message(URL, bot_token, user_id, get_CNY())
                    elif text.upper() == "/CZK":
                        send_message(URL, bot_token, user_id, get_CZK())
                    elif text.upper() == "/DKK":
                        send_message(URL, bot_token, user_id, get_DKK())
                    elif text.upper() == "/EUR":
                        send_message(URL, bot_token, user_id, get_EUR())
                    elif text.upper() == "/GBR":
                        send_message(URL, bot_token, user_id, get_GBR())
                    elif text.upper() == "/HUF":
                        send_message(URL, bot_token, user_id, get_HUF())
                    elif text.upper() == "/INR":
                        send_message(URL, bot_token, user_id, get_INR())
                    elif text.upper() == "/JPY":
                        send_message(URL, bot_token, user_id, get_JPY())
                    elif text.upper() == "/KGS":
                        send_message(URL, bot_token, user_id, get_KGS())
                    elif text.upper() == "/KRW":
                        send_message(URL, bot_token, user_id, get_KRW())
                    elif text.upper() == "/KZT":
                        send_message(URL, bot_token, user_id, get_KZT())
                    elif text.upper() == "/MDL":
                        send_message(URL, bot_token, user_id, get_MDL())
                    elif text.upper() == "/NOK":
                        send_message(URL, bot_token, user_id, get_NOK())
                    elif text.upper() == "/PLN":
                        send_message(URL, bot_token, user_id, get_PLN())
                    elif text.upper() == "/RON":
                        send_message(URL, bot_token, user_id, get_RON())
                    elif text.upper() == "/SEK":
                        send_message(URL, bot_token, user_id, get_SEK())
                    elif text.upper() == "/SGD":
                        send_message(URL, bot_token, user_id, get_SGD())
                    elif text.upper() == "/TJS":
                        send_message(URL, bot_token, user_id, get_TJS())
                    elif text.upper() == "/TMT":
                        send_message(URL, bot_token, user_id, get_TMT())
                    elif text.upper() == "/TRY":
                        send_message(URL, bot_token, user_id, get_TRY())
                    elif text.upper() == "/UAH":
                        send_message(URL, bot_token, user_id, get_UAH())
                    elif text.upper() == "/USD":
                        send_message(URL, bot_token, user_id, get_USD())
                    elif text.upper() == "/UZS":
                        send_message(URL, bot_token, user_id, get_UZS())
                    elif text.upper() == "/XDR":
                        send_message(URL, bot_token, user_id, get_XDR())
                    elif text.upper() == "/ZAR":
                        send_message(URL, bot_token, user_id, get_ZAR())
                else:
                    continue
        except IndexError as e:
            print("Введите токен! \nНапример: python3 bot.py ТУТ_ДОЛЖЕН_БЫТЬ_ТОКЕН_БОТА")
#############################################################################################################################################################################################################################################
if __name__ == "__main__":
    main()
