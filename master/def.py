import time, os, sqlite3
from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts

os.system("cls")

def transitionprogress():
    from colorama import init, Fore, Back, Style
    os.system("cls")
    time.sleep(1)
    print(Fore.WHITE+'|'+Fore.RED+'████ OFF |')
    time.sleep(0.3)
    print(Fore.WHITE+'|'+Fore.RED+'███     '+Fore.GREEN+'█|')
    time.sleep(0.3)
    print(Fore.WHITE+'|'+Fore.RED+'██     '+Fore.GREEN+'██|')
    time.sleep(0.3)
    print(Fore.WHITE+'|'+Fore.RED+'█     '+Fore.GREEN+'███|')
    time.sleep(0.3)
    print(Fore.WHITE+'|'+Fore.GREEN+ ' ON  ████|'+Fore.WHITE)
    time.sleep(1.24)
    os.system("cls")


def transitionprogressneg():
    from colorama import init, Fore, Back, Style
    os.system("cls")
    time.sleep(1)
    print(Fore.WHITE+'|'+Fore.GREEN+ ' ON  ████|')
    time.sleep(0.3)
    print(Fore.WHITE+'|'+Fore.RED+'█     '+Fore.GREEN+'███|')
    time.sleep(0.3)
    print(Fore.WHITE+'|'+Fore.RED+'██     '+Fore.GREEN+'██|')
    time.sleep(0.3)
    print(Fore.WHITE+'|'+Fore.RED+'███     '+Fore.GREEN+'█|')
    time.sleep(0.3)
    print(Fore.WHITE+'|'+Fore.RED+'████ OFF |'+Fore.WHITE)
    time.sleep(1.24)
    os.system("cls")


def settingsmenu():
    time.sleep(0.2)
    print("████████████████████████████████████████████████████████████████████████████")
    print(" --------------------------  DBFA Settings  --------------------------    ")
    print(" 1:    Display boot image                               :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      ')
    print(" 2:    Email invoice to registered customers            :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      ')
    print(" 3:    Enable DBFA Music Controls (beta):               :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      ')
    print(" 4:    Open CSV when exported                           :", '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|      ')
    print(" 5:    Enable database encryption                       :", ('|'+Fore.RED+'████'+Fore.WHITE+' OFF|      ')+Fore.RED)
    print(Fore.RED+" 6:    Delete customer records                          :"+Fore.WHITE, '|'+Fore.RED+"██ Proceed > "+Fore.WHITE+"| ")
    print(Fore.RED+" 7:    Delete store records                             :"+Fore.WHITE, '|'+Fore.RED+"██ Proceed > "+Fore.WHITE+"| ")
    print(Fore.MAGENTA+" 8:    Check for updates                                :"+' |'+"██ Proceed > "+Fore.WHITE+"|  " )
    print("                                                                          ")
    print(Fore.RED+" 9:    Return to Main Menu                              :"+' |'+"██ Proceed > "+Fore.WHITE+"| " )
    print("                                                                          ")
    #print("████████████████████████████████████████████████████████████████████████████")
    settfac = input("What would you like to do? ")
    if settfac == "1":
        print('''DBFA displays an image for 2 seconds when it is started. 
        This image changes with each major iteration of DBFA. 
        Displaying this image let's us prepare files in the background so that DBFA runs smoothly once its started.
        Disabling this option may lead to errors. Continue? ''')
        print(" ")
        print("Display DBFA boot image? ")
        print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
        settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
        if settfac1x == "y":
            transitionprogress()
            print("DBFA will now display its boot image when it prepares the backend on boot. ")
            print("")
            time.sleep(1)
            settingsmenu()
        elif settfac1x == "n":
            transitionprogressneg()
            print("DBFA won't display its boot image when it prepares the backend on boot from now. ")
            print("")
            time.sleep(1)
            settingsmenu()
        else:
            print("That's an invalid input... ")
            print("")
            time.sleep(1)
            settingsmenu()
        
    elif settfac == "2":
        print('''DBFA creates an invoice on each billing cycle
        If the customer account in-use is registered with DBFA, the invoice is E-Mailed to the same.
        Disabling this option will stop DBFA from E-Mailing customers with their invoice from now.''')
        print(" ")
        print("E-Mail registered customers their invoice? ")
        print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
        settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
        if settfac1x == "y":
            transitionprogress()
            print("DBFA will continue E-Mailing customers with their invoice. ")
            print("")
            time.sleep(1)
            settingsmenu()
        elif settfac1x == "n":
            transitionprogressneg()
            print("DBFA will stop E-Mailing customers their invoice from now on. ")
            print("")
            time.sleep(1)
            settingsmenu()
        else:
            print("That's an invalid input... ")
            print("")
            time.sleep(1)
            settingsmenu()
        
    elif settfac == "3":
        print('''In our mission of making DBFA the ultimate space to control your entire store and its functioning,
        we keep adding tiny tid-bits to make that process even easier.
        DBFA Music Controls is one such feature introduced in DBFA 8 RC3x (IB3).
        When you disable this functionality:
                - The currently-playing track will no longer be displayed. 
                - DBFA Music Controls, including but not limited to pause/play, prev and next will be restricted. ''')
        print(" ")
        print("Enable DBFA Music Controls? ")
        print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
        settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
        if settfac1x == "y":
            transitionprogress()
            print("DBFA Music Controls Service will be started with the next menu-cycle. ")
            print("")
            time.sleep(1)
            settingsmenu()
        elif settfac1x == "n":
            transitionprogressneg()
            print("DBFA Music Controls Service will be restricted from the next menu-cycle.")
            print("")
            time.sleep(1)
            settingsmenu()
        else:
            print("That's an invalid input... ")
            print("")
            time.sleep(1)
            settingsmenu()
        
        
    elif settfac == "4":
        print("CSV files once generated are auto-opened in your default worksheet app")
        print("Example: Microsoft Excel, LibreOffice Calc, Google Docs, et cetera.")
        print(" ")
        print("Open file after export? ")
        print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
        settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
        if settfac1x == "y":
            transitionprogress()
            print("DBFA will now open CSV files when exported on request. ")
            print("")
            time.sleep(1)
            settingsmenu()
        elif settfac1x == "n":
            transitionprogressneg()
            print("DBFA will not open CSV files when exported from now on. ")
            print("")
            time.sleep(1)
            settingsmenu()
        else:
            print("That's an invalid input... ")
            print("")
            time.sleep(1)
            settingsmenu()
        
    elif settfac == "5":
        print('''In our process of phasing-out .txt based storage in favour of sqlite storage, 
        we at DBFA are trying to make our files even tougher to access than ever before without valid credentials.
        
        DBFA is currently experimenting with sqlcipher encryption for it's sqlite databases.
        Please note that this functionality is a part of DBFA internal test builds for now,
        and is not ready for public rollout.
        
        This process might impact DBFA's data integrity. We recommend you to run *DBFA Backup&Switch* from option *5*
        before you attempt to encrypt/ decrypt DBFA databases by running this command.''')
        print(" ")
        print("Enable DBFA database encryption? ")
        print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
        settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
        if settfac1x == "y":
            transitionprogress()
            print('''DBFA will attempt to encrypt it's databases when restarted. 
            This process may fail, as this *internal test build* of DBFA currently has encryption as a beta feature.''')
            print("")
            time.sleep(1)
            settingsmenu()
        elif settfac1x == "n":
            transitionprogressneg()
            print('''DBFA will attempt to de-crypt it's databases on the next restart. 
            This process may fail, as this *internal test build* of DBFA currently has encryption as a beta feature.
            
            If DBFA databases are already decrypted, no change will take place and data integrity will be untouched.''')
            print("")
            time.sleep(1)
            settingsmenu()
        else:
            print("That's an invalid input... ")
            print("")
            time.sleep(1)
            settingsmenu()
        
    elif settfac == "6":
        print('''This option PERMANENTLY CLEARS ALL DBFA CUSTOMER RECORDS.
        This includes their registration data, purchase records, and loyalty points.
        
        This execution can NOT BE REVERSED.
        DATA INTEGRITY MAY BE LOST during this process.
        Proceed with caution! ''')
        print(" ")
        print("ERASE DBFA customer records PERMANENTLY? ")
        print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
        settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
        if settfac1x == "y":
            transitionprogress()
            print("DBFA will continue E-Mailing customers with their invoice. ")
            print("")
            time.sleep(1)
            settingsmenu()
        elif settfac1x == "n":
            transitionprogressneg()
            print("DBFA will stop E-Mailing customers their invoice from now on. ")
            print("")
            time.sleep(1)
            settingsmenu()
        else:
            print("That's an invalid input... ")
            print("")
            time.sleep(1)
            settingsmenu()

    elif settfac == "7":
        print('''This option PERMANENTLY CLEARS ALL DBFA VOUCHERS/ COUPONS
        All current vouchers/ coupons WILL BE LOST.
        Vouchers already issued will become redundant unless manually re-added again.
        Validity and usage limits will be lost for all voucher/ coupon instanced recorded by DBFA.
        
        However, DBFA's logged voucher/ coupon usage will continue to exist in memory and will not be erased.
        
        This execution can NOT BE REVERSED.
        DATA INTEGRITY MAY BE LOST during this process.
        Proceed with caution! ''')
        print(" ")
        print("ERASE DBFA voucher/ coupon records PERMANENTLY? ")
        print("y:    ",  '| ON '+Fore.GREEN+'████'+Fore.WHITE+'|')
        settfac1x = input(("n:     "+ '|'+Fore.RED+'████'+Fore.WHITE+' OFF|: '))
        if settfac1x == "y":
            transitionprogress()
            print("DBFA will continue E-Mailing customers with their invoice. ")
            print("")
            time.sleep(1)
            settingsmenu()
        elif settfac1x == "n":
            transitionprogressneg()
            print("DBFA will stop E-Mailing customers their invoice from now on. ")
            print("")
            time.sleep(1)
            settingsmenu()
        else:
            print("That's an invalid input... ")
            print("")
            time.sleep(1)
            settingsmenu()


    elif settfac == "8":
        print("DBFA Updater is currently in the making. ")
        print("You'll be notified immediately this feature is enabled. ")
        print("Support for this will come with a future update. ")

    elif settfac == "9":
        os._exit(0)

    else:
        print("That's an invalid input... ")
        print("")
        time.sleep(1)
        settingsmenu()

while(1):
    settingsmenu()