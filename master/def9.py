from datetime import datetime
import sqlite3, time, os

def OAuthset():
    now = datetime.now()
    try: #To avoid error when time is 00:00:00
        netr = int(now.strftime("%H"))*3600 + int(now.strftime("%M"))*60 + int(now.strftime("%S"))
    except:
        time.sleep(1)
        netr = int(now.strftime("%H"))*3600 + int(now.strftime("%M"))*60 + int(now.strftime("%S"))
    oauth = sqlite3.connect(r'dbfasettings.db')
    oauthx = oauth.cursor()

    oauthx.execute("SELECT count(*) FROM LoginHandler")
    rows = oauthx.fetchall()
    if (rows[0][0]) > 1:
        print("DBFA Authenticator has been tampered with! DBFA WILL EXIT NOW!")
        time.sleep(2)
        os._exit(0)
    oauthx.execute("SELECT OAuthID FROM LoginHandler")
    try: #To avoid error when there's no data in the table
        maxid = int(oauthx.fetchall()[0][0]) + 1
    except:
        maxid = 1
        oauthx.execute("insert into LoginHandler(OAuthID, Value, TimeMark) values(?, 1, ?)", (maxid, netr))
    oauthx.execute("UPDATE LoginHandler SET OAuthID = ?, Value = 1, TimeMark = ?", (maxid, netr))
    print("Login session dtalgnrt", netr, "-", maxid)
    oauth.commit()
    oauth.close()


def OAuthvalidate():
    from datetime import datetime
    import sqlite3, time, os
    now = datetime.now()
    try: #To avoid error when time is 00:00:00
        netr = int(now.strftime("%H"))*3600 + int(now.strftime("%M"))*60 + int(now.strftime("%S"))
    except:
        time.sleep(1)
        netr = int(now.strftime("%H"))*3600 + int(now.strftime("%M"))*60 + int(now.strftime("%S"))
    oauth = sqlite3.connect(r'dbfasettings.db')
    oauthx = oauth.cursor()
    oauthx.execute("SELECT Value FROM LoginHandler")
    check = oauthx.fetchall()[0][0]
    if check != 1:
        print("Login was bypassed! DBFA will now exit!")
        time.sleep(1)
        os._exit(0)
    oauthx.execute("SELECT count(*) FROM LoginHandler")
    rows = oauthx.fetchall()
    if (rows[0][0]) > 1:
        print("DBFA Authenticator has been tampered with! DBFA WILL EXIT NOW!")
        time.sleep(2)
        os._exit(0)
    oauthx.execute("SELECT TimeMark FROM LoginHandler")
    stamp = oauthx.fetchall()[0][0]
    if int(netr)-int(stamp) > 60:
        print("LOGIN TIMEOUT!")
        print("You must open DBFA immediately after the login process.")
        print("DBFA will now exit!")
        time.sleep(1)
        os._exit
    elif int(netr)-int(stamp) < 60:
        print("- - - Valid login detected - - -")
    else:
        print("Login was bypassed! DBFA will now exit!")
        time.sleep(1)
        os._exit(0)
    
    oauthx.execute("UPDATE LoginHandler SET Value = 0, TimeMark = 0")
    oauth.commit()
    oauth.close()    

OAuthvalidate()