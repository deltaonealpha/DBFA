import json, requests, time, urllib, os
URL = "https://api.telegram.org/bot{}/".format('1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis')

def settingscommonfetch(SettingsType):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("SELECT Value from settings WHERE SettingsType = ?"), (SettingsType,))
    settingsfetch = (settingsx.fetchall()[0][0])
    return settingsfetch

def settingsmodifier(SettingsType, NewValue):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("UPDATE settings SET Value = ? WHERE SettingsType = ?"), (NewValue, SettingsType))
    settings.commit()


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = '680917769'
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, '680917769')
    get_url(url)


def main():
    get_url('https://api.telegram.org/bot/deleteWebhook')
    with open('lastupdateid2.txt', 'a+') as file:
        file.close()
    with open('lastupdateid2.txt', 'r+') as file:
        xid = file.read()
    #print(xid)
    last_update_id = int(xid)+1
    import webbrowser
    updates = get_updates(last_update_id)
    if len(updates["result"]) > 0:
        last_update_id = get_last_update_id(updates)
        for update in updates["result"]:
            if (update["message"]["text"]).replace(" ", "") == "disableDBFA":
                settingsmodifier(9, 0)
                #telegram_bot_sendtext("delta Webhook Services\nUsage permissions have been revoked from your installation of DBFA.\n\nExpect access to be stopped from the next boot/ menu cycle.\nhttps://software.deltaone.tech/servicestatus.html")
                print("A webbrowser window will shortly open ~")
                webbrowser.open('https://software.deltaone.tech/servicestatus.html')
            elif (update["message"]["text"]).replace(" ", "") == "enableDBFA":
                if settingscommonfetch(9) == 0:
                    settingsmodifier(9, 1)
                    #telegram_bot_sendtext("delta Webhook Services\n\nAccess has been re-granted on your installation of DBFA.")
                    print("The administrator of this DBFA installation has re-allowed access to DBFA on this device!")
            else:
                if settingscommonfetch(9) == 0:
                    print("A webbrowser window will shortly open ~")
                    webbrowser.open('https://software.deltaone.tech/servicestatus.html')
                    time.sleep(2)
                    os._exit(0)
                else:
                    pass
        with open('lastupdateid2.txt', 'a+') as file:
            file.close()
        with open('lastupdateid2.txt', 'r+') as file:
            file.truncate(0)
            file.write('%d'%last_update_id)
        #echo_all(updates)
        time.sleep(0.5)
    time.sleep(0.5)

if __name__ == '__main__':
    main()