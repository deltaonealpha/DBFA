2a
logger.write("--------------------------------------- \n")
logger.write("  \n")
logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
logger.write(dt_string)
logger.write(" \n")
logger.write("New customer registered: ")
x = " custname: " + custname + " custemail: " + email + "\n"
logger.write(x)
logger.write("--------------------------------------- \n")

2b
logger.write("--------------------------------------- \n")
logger.write("  \n")
logger.write("Date and time: ") #including the date and time of billing (as taken from the system)
logger.write(dt_string)
logger.write(" \n")
logger.write("Customer registry accessed! \n")
logger.write("--------------------------------------- \n")

2c
logger.write("--------------------------------------- \n")
logger.write("\nDBFA Customer Purchase Records accessed! \n")

2d
logger.write("--------------------------------------- \n")
logger.write("\nCustomer search used. \n")

2e
logger.write("\n\n--------------------------------------- \n")
logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
logger.write("Customer data exported to CSV! ")
with HiddenPrints():
    try:
        sender = telegram_bot_sendtext(dt_string + "\n" + "Customer data exported to CSV- REDFLAG Urgent Security Notice!")
        print(sender)
    except Exception:
        pass
logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
logger.write("--------------------------------------- \n\n\n")





3a


3b


3c


3d


3e
logger.write("\n--------------------------------------- \n")
logger.write("Sales log accessed! ")

3f
logger.write("\n\n--------------------------------------- \n")
logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
with HiddenPrints():
    try:
        sender = telegram_bot_sendtext(dt_string + "\n" + "Customer data exported to CSV- REDFLAG Urgent Security Notice!")
        print(sender)
    except Exception:
        pass
logger.write("Sales data exported to CSV! ")
logger.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
logger.write("--------------------------------------- \n\n\n")