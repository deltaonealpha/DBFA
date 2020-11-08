splitfac = input("Split bill? (y/n): ")
if splitfac in ("Y", "y"):
    try:
        splitcountfac = int(input("Enter the number of people to split for: "))
    except:
        try:
            print("Person count must be real! ~")
            splitcountfac = int(input("Enter the number of people to split for: "))
        except:
            print("Billing splitting has been cancelled due to repetitive invalid inputs. Bill will be generated without a split.")
            splitcountfac = 1
    if "." in str(((netpay)/int(splitcountfac))):
        splitpay = float(eval((str(((netpay)/int(splitcountfac))).split('.')[0] + '.' + (str(((netpay)/int(splitcountfac))).split('.')[1])[0:2])))
    else:
        splitpay = float(eval(netpay/int(splitcountfac)))
else:
    pass

print((splitpay))