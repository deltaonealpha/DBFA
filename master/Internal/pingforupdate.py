import requests

def telegram_bot_sendtext(bot_message):
    '''
    bot_token = '812114312:AAF8Oy9UTvJflGZDDZPae-Ak-DXo_rvEl_s'
    bot_chatID = '983655055'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    '''

    bot_token = '812114312:AAF8Oy9UTvJflGZDDZPae-Ak-DXo_rvEl_s'
    bot_chatID = '680917769'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    

telethon = ""

telethon += "~ GitHub Notification Bot\n\n"
telethon += "Data recieved from GitHub API follows: \n"
telethon += "---------------------------------------\n"
telethon += "Changes to\ngithub.com/deltaonealpha/drts7/deltaUpdater\nwere auto-pushed to \ngithub.com/deltaonealpha/DBFA\n"
telethon += "\n\nCommit: \n\n"
telethon += "06-09-20 20:22\n"
telethon += "> delta updater framework completed and enabled.\n"
telethon += "> Reworked update-check logic from scratch\n"
telethon += "> Version details are checked from both, local source and server source.\n"
telethon += "> Auto-download update files when told to do so by the user using git\n"
telethon += "> Added instructions for update via a .txt file\n"
telethon += "> A seperate new repository is being maintained to host update files. (OTA; only changed files)\n"
telethon += "> Updater is OTA-based. Only updated files will be hosted.\n\n"
telethon += "\n\nSource from: @GitHubBot\n\n"

telegram_bot_sendtext(telethon)