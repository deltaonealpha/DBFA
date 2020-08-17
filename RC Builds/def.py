def xmainmenu(): #defining a function for the main menu

    from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
    init(convert = True)
    print(Fore.RED,)
    print("---------------------------------------------")
    print(Fore.WHITE, 'A word from our partner: ' + Fore.BLACK + Back.CYAN + 'HOTEL? Trivago!' + Back.BLACK + Style.RESET_ALL + Fore.RED) #Text over here #Custom advert
    print("---------------------------------------------", Style.RESET_ALL)
    print('''       _______   ______   _____  ____
      / /--/-/  / /-/-/  /____/ / / /|
     / /  / /  / /==/ / / /__  /-/--/|
    /_/__/_/  /_/_/_/  /_/    / /   /|''')

    print("\nOptions: ") 
    print("1: Issue a Bill")
    print("2: Manage Customers")
    print("    a: Register a Customer")
    print("    b: Customer Registry")
    print("    b: Customer Purchase Records")
    print("3: Store Options:")
    print("    a: Manage Stock")
    print("    b: Manage Vouchers")
    print("    c: Product Listing")
    print("    d: Sales Log")
    print("4: Auto-Generate Store Report")
    print("5: Start DBFA Backup&Switch")
    print("6: View Software License,")
    print("7: Quit")
    print("- enter CIT code to view more options -")
    print()
    print()
xmainmenu()