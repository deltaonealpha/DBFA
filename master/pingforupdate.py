import requests

def telegram_bot_sendtext(bot_message):

    bot_token = '812114312:AAF8Oy9UTvJflGZDDZPae-Ak-DXo_rvEl_s'
    bot_chatID = '983655055'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


    bot_token = '812114312:AAF8Oy9UTvJflGZDDZPae-Ak-DXo_rvEl_s'
    bot_chatID = '680917769'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    

telethon = ""

telethon += "This is DBFA's updater bot which pings users when an update is pushed to GitHub."
telethon += "\n\n"
telethon += "Update summary from Git: Improvements and new features for DBFA 8 RC3x"
telethon += "\n\n"
telethon += "Summary of recent changes as per latest GitHib deployment on 28/28/2020:"
telethon += "\n"
telethon += "\n"
telethon += "- Introducing DBFA Sales Plotter v1"
telethon += "\n"
telethon += "- Menu option *10* to view a plot of profit vs date"
telethon += "\n"
telethon += "- PDF reporter now shows the plot too!"
telethon += "\n"
telethon += "- Improved PDF reported: Corrected table dimensions (and useless columns nuked); bold removed from sub-headings."
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