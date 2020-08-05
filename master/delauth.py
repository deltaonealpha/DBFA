import requests, time, json, urllib, os
from tqdm import tqdm 
import PySimpleGUI as sgx

global valn
valn = 0
#print(valn)

def telegram_bot_sendtext(bot_message):
    bot_token = '1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis'
    bot_chatID = '680917769'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


global last_update_id
lns = open(r"lastupdateid.txt", "r+")  #Opening / creating (if it doesn't exist already) the .txt record file
last_update_id = (lns.read())

TOKEN = "1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


sgx.theme('DarkBlue')
def Login():
    layout = [  [sgx.Text('Login to authenicate: ')],
                [sgx.Text('Username: '), sgx.InputText()],
                [sgx.Text('Password: '), sgx.InputText()],
                [sgx.Button('Authenicate'), sgx.Button('Cancel')] ]
    window = sgx.Window('deltaAuthenication Service', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
            window.close
            os._exit(0)
            window.close()
            window.close()
            os._exit(1)
        if values[0] == 'ed' and values[1] == 'edd':
            window.close()
            window.close()
            pass
        else:
            sgx.theme('DarkRed')
            Login()


def get_updates(offset=None):
    global updates
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    updates = js
    return updates


def get_last_update_id(updates):
    global last_update_id, valn
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    try:
        last_update_id = max(update_ids)
        lns = open(r"lastupdateid.txt", "r+")  #Opening / creating (if it doesn't exist already) the .txt record file
        lns.truncate(0)
        lns.write('%d'%last_update_id)
    except ValueError:
        lns = open(r"lastupdateid.txt", "r+")  #Opening / creating (if it doesn't exist already) the .txt record file
        last_update_id = int(lns.read())+1
        
        


def echo_all(updates):
    global last_update_id
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        global valn
        #print(valn)
        if valn == 0:
            if text == "ed":
                valn = 1
                send_message("You have authenicated a DBFA Backup & Switch request.\n\nThis allows your installation of DBFA to be backed-up.\n\nIf this wasn't you, contact support and revoke your Telegram bot login at the earliest.\n\nDBFA Security", chat)
                ins = open(r"delauth.txt", "a+")  #Opening / creating (if it doesn't exist already) the .txt record file
                ins.write('%s'%update)
                ins.close()
                get_updates(last_update_id)
                get_last_update_id(updates)
                os.startfile('dbfabackupper.py')
                time.sleep(0.5)
                echo_all(updates)

            else:
                texterx = text + ": That'd be wrong. Please try again."
                send_message(texterx, chat)
        elif valn == 1:
            get_updates(last_update_id)
            get_last_update_id(updates)
            time.sleep(2)
            os._exit(0)
            


def get_last_chat_id_and_text(updates):
    global last_update_id

    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)



def main():
    global last_update_id
    url = URL + "setWebhook?url="
    get_url(url)
    get_updates(last_update_id)
    get_last_update_id(updates)
    while True:
        get_updates(last_update_id)
        
        if len((updates)["result"]) > 0:
            last_update_id += 1
            echo_all(updates)
        time.sleep(0.5)




if __name__ == '__main__':
    Login()
    print("As you're accessing sensitive information, we'll require you to authenicate this request.")
    time.sleep(2)
    print("")
    print("Please open your Telegram application and authenicate the request from the *DBFA Communicator* bot by following the instructions there.")
    time.sleep(0.5)
    for i in tqdm (range (10), desc="Waiting to detect authenication:  "):     
        texter = "This is an authenication request for DBFA Backup and Reset." + "\n\n" + "Please send the passcode to authenicate this request." + "\n\n" + "DBFA Security"
        sender = telegram_bot_sendtext(texter)
        main()