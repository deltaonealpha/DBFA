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

telethon += "This is DBFA's updater bot which pings users when an update is pushed to GitHub."
telethon += "\n\n"
telethon += "Update summary from Git: DBFA 2FA and Sales Grapher"
telethon += "\n\n"
telethon += "Summary of recent changes as per latest GitHib deployment on 30/28/2020:"
telethon += "\n"
telethon += "\n"
telethon += "- Introducing DBFA Two-Factor-Authenication"
telethon += "\n"
telethon += "- 2FA with secure encrypted connection to tg, where the OTP is delivered."
telethon += "\n"
telethon += "- 2FA enable/disable option in settings with prompt if the desired status IS the current service status "
telethon += "\n"
telethon += "- Introducing DBFA Sales Plotter v1 (menu optn 10 + graph in pdf report)"
telethon += "\n"
telethon += "- PDF reporter: Corrected table (dimensions and columns); bold removed from sub-headings."
telethon += "\n"
telethon += "- Re-organised and updated main menu"
telethon += "\n"
telethon += "- Removed bug where *10* had to be entered twice in order to leave DBFA Settings and return to the main menu."
telethon += "\n\n"
telethon += "- Synced upstream"
telethon += "\n\n"
telethon += "View all changes in depth on the DBFA infinity changelog:"
telethon += "\n"
telethon += "https://telegra.ph/DBFA-8-Release-Candidate---1-08-16"
telethon += "\n"
telethon += "\n@deltacommsbot"

telegram_bot_sendtext(telethon)