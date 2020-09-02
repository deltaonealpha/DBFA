
import requests, time, json, urllib, os, math, random, sqlite3
from tqdm import tqdm 
import logging, os, time, requests, socket
import telegram_send
from pynput.keyboard import Key, Controller
# Telegram BOT API 2 (FULL)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def telegram_bot_sendtext(bot_message):
    bot_token = '1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis'
    bot_chatID = '680917769'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def start(update, context):
    keyboard = [[InlineKeyboardButton("Validate", callback_data='1'),
                 InlineKeyboardButton("Deny", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("delta 2FA Handler Service\n\n\nValidate login?", reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    inlet = ("{}".format(query.data))
    if inlet in (1, "1"):
        query.edit_message_text(text="delta 2FA approved! \n\nThis allows your installation of the DBFA client, and its data to be accessed. \n\nIf this wasn't you, contact support and revoke your bot login at the earliest.\n\ndelta Security Service")
        with open(r"C:\Users\balaj\OneDrive\Documents\GitHub\delXBRS7\Untitled-1.webp", "rb") as f:
            telegram_send.send(stickers=[f])
            keyboard = Controller()
            print("telegram.ext.updtr_pushreq(deltaonealpha, set.webhook; reset)")
            keyboard.press(Key.ctrl)
            keyboard.press('c')
            keyboard.release('c')
            keyboard.release(Key.ctrl)

    if inlet in (2, "2"):
        query.edit_message_text(text="Denied delta 2FA request.\n\ndelta Security Service")
        with open(r"C:\Users\balaj\OneDrive\Documents\GitHub\delXBRS7\Untitled-1.webp", "rb") as f:
            telegram_send.send(stickers=[f])
        keyboard = Controller()
        print("telegram.ext.updtr_pushreq(deltaonealpha, set.webhook; reset)")
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release(Key.ctrl)
        time.sleep(1)
        print("The login request for this session has been DENIED.")
        time.sleep(1)
        print("DBFA Client will now exit! ")
        os._exit(0)
    if inlet in (3, "3"):
        query.edit_message_text(text="Use */help*")    
    


def help_command(update, context):
    update.message.reply_text("Use /start to use this bot.")


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('auth', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


def settingscommonfetch(SettingsType):
    import sqlite3
    settings = sqlite3.connect(r'dbfasettings.db')
    settingsx = settings.cursor()
    settingsx.execute(("SELECT Value from settings WHERE SettingsType = ?"), (SettingsType,))
    settingsfetch = (settingsx.fetchall()[0][0])
    return settingsfetch

if settingscommonfetch(6) == 1:
    def telegram_bot_sendtext(bot_message):
        bot_token = '1215404401:AAEvVBwzogEhOvBaW5iSpHRbz3Tnc7fCZis'
        bot_chatID = '680917769'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

    os.system('cls')
    print("delta2 Authenication Service")    
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("DBFA 2FA Service")
    time.sleep(1)
    print("")





    print("You have DBFA 2FA activated. Please validate the login from your Telegram account. ")
    for i in tqdm (range (10), desc="Connecting.."):     
        time.sleep(0.00001)    
    if __name__ == '__main__':
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        import platform
        from datetime import datetime  #for reporting the billing time and date
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  #datetime object containing current date and time
        with open(r"C:\Users\balaj\OneDrive\Documents\GitHub\delXBRS7\Untitled-1.webp", "rb") as f:
            telegram_send.send(stickers=[f])
        telegram_bot_sendtext("delta 2FA Handler Service\nA login request has been recieved from your DBFA installation.\n\nRequest time        - " + '%s'%dt_string + f"\nHostname             - {hostname}\n" + f"IP Address             - {ip_address}\n" + "Service Identifier  - "+ platform.system() + platform.release() +"\n\nWARNING:  Do not approve this if this isn't you!\n\nPlease send */auth* to start the validation process: ")
        main()
    os.system('cls')

else:
    print("DBFA 2FA is disabled. We recommend you to turn it on from the settings for a more secure experience with DBFA client.")

