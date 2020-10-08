import requests

def telegram_bot_sendtext(bot_message):
    '''
    bot_token = '812114312:AAGM7PotaKGklGG9yByiG0Wab6P-A3XoEf8'
    bot_chatID = '983655055'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    '''

    bot_token = '812114312:AAGM7PotaKGklGG9yByiG0Wab6P-A3XoEf8'
    bot_chatID = '680917769'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    

telethon = ""

telethon += "Release - DBFA 8.55 Commemorative Edition (Stable)\n\n"
telethon += "*Incremental Security Update\n"
telethon += "Build Highlights:\n"
telethon += "• Presenting DBFA Web Hook Security. The admin can now type 'disableDBFA' in our Telegram bot and DBFA access on related installations will be disabled from the next menu cycle/ boot until re-enabled by the admin. DBFA will exit and display a webpage (https://software.deltaone.tech/servicestatus.html) showing operational status and reasons for exiting.\n\n"
telethon += "Others:\n"
telethon += "• Updated sync details and version ID for updater and MD5 crash detection.\n"
telethon += "• Updated .readme on Git.\n"
telethon += "• Updated GitHub releases with new .zip.\n\n"
telethon += "author @deltaonealpha"

print(telethon)

telegram_bot_sendtext(telethon)

print("EP_1")
