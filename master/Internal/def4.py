
            from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
            init(convert = True)
            print(Fore.RED+'''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Security Options                                    DBFA Debugger >>> Permissive Options
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
DBFA Client will restart to execute Permissive Options!'''+Fore.MAGENTA+'''
'1' - to CLEAR ALL CUSTOMER RECORDS
'2' - to CLEAR ALL VOUCHERS/ COUPONS
'3' - to exit CIT

What would you like to do?                '''+Fore.RED+'''█▀▀█ █▀ ██  █ █ █▀▀  █▀▀  █▀ ██   Internal'''+Fore.MAGENTA+'''
'''+Fore.RED+'''▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  '''+Fore.RED+'''█__█ █_ ███ █_█ █_▀█ █_▀█ █_ █ ▀_ Testing Mode'''+Fore.MAGENTA+'''
'''+Fore.CYAN+'''DBFA Debugger >>> Permissive Options ~    
'''+Fore.RED+'''▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''+Fore.WHITE)

            citfacin = int(input("Waiting for input:: "))
            if citfacin == 1:
                # window.close()
                with HiddenPrints():
                    try:
                        sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: CIT del cust recs - deltaDBFA")
                        print(sender)
                    except Exception:
                        pass
                os.startfile(r'securepack.py')
                time.sleep(1)
                os._exit(0)
            if citfacin == 2:
                # window.close()
                with HiddenPrints():
                    try:
                        sender = telegram_bot_sendtext(dt_string + "\n" + "Accessed: CIT del voucher recs - deltaDBFA")
                        print(sender)
                    except Exception:
                        pass
                os.startfile(r'securepackxvc.py')
                time.sleep(1)
                os._exit(0)
            else:
                continue
    
        else:
            continue


    elif ffxfac == "3":
        print("Exiting CIT")
        time.sleep(1)
        continue
    else:
        print("Invalid input. . . . ")
        time.sleep(1)
else:
    print("This function is restricted on your account.")
