from colorama import init, Fore, Back, Style #color-settings for the partner/sponsor adverts
logoxold = (Fore.CYAN+''' 
                            Options:  
  █▀▀█ █▀█  █▀▀ █▀█  █▀▀█   1  - Issue a Bill                                            4  - Store Report
  █__█ █▀▀█ █▀  █▬█  ▄▄▄▄   2  - Manage Customers:                                       5  - Manage Deliveries
  CLIENT 8.12 DONNAGER              a: Register a Customer    c: Purchase Records        6  - DBFA Options 
'''+Fore.MAGENTA+'''  The OG Store Manager'''+Fore.CYAN+'''              b: Customer Registry      d: Find a Customer         7  - Start DBFA Backup & Switch 
                                    e: Export data as CSV                                8  - Analyse Sales
                            3  - Store Options:                                          
                                    a: Manage Stock           c: Manage Vouchers         9  - View Software License
                                    b: DBFA Stock Master      d: Product Listing         10 - About DBFA 8.12
                                    e: Sales Log              f: Export data as CSV      11 - Quit
  '''+Fore.MAGENTA+'''                          
  DBFA Music Controls:: *prev* - << previous | *pause* - <|> pause/play | *next* - >> next  '''+Fore.CYAN+'''
-----------------------------------------------------------------------------------------------------------------------''')

logoxnew = (Fore.CYAN+'''
Options:
  1  - Issue a Bill                                              4  - Store Report
  2  - Manage Customers:                                         5  - Manage Deliveries
          a: Register a Customer    c: Purchase Records          6  - DBFA Options
          b: Customer Registry      d: Find a Customer           7  - Start DBFA Backup & Switch
          e: Export data as CSV                                  8  - Analyse Sales
  3  - Store Options:                                            
          a: Manage Stock           c: Manage Vouchers           9  - View Software License
          b: DBFA Stock Master      d: Product Listing           10 - About DBFA 8.12
          e: Sales Log              f: Export data as CSV        11 - Quit
'''+Fore.MAGENTA+'''                                                                 
What would you like to do?                  The OG Store Manager'''+Fore.CYAN+''' █▀▀█ █▀█  █▀▀ █▀█  █▀▀█   
---------------------------------------------------------------- █__█ █▀▀█ █▀  █▬█  ▄▄▄▄                            
DBFA Music Controls: *prev* <<< | *pause* <|> | *next* >>>       CLIENT 8.12 DONNAGER                               
-------------------------------------------------------------------------------------''')



print(len('-----------------------------------------------------------------------------------------------------------------------'))
print(len('Profit (last week): '))