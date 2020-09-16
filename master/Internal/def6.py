r'''
def primecheck(number):
    if number == 1:
        print(number, " :not a prime number!")
    if number == 2:
        print(number, " :is a prime number!")
    else:
        for i in range (2, number):
            if number % i == 0:
                pcheck = 0                
            else:
                pcheck = 1
                break
    if pcheck == 0:
        print(number, " :is not a prime number!")
    else:
        print(number, " :is a prime number!")
primecheck(12)
primecheck(1)
primecheck(2)
primecheck(17)

#-------------------------------------------OUTPUT-------------------------------------------
# PS C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master> & C:/Users/balaj/AppData/Local/Programs/Python/Python37/python.exe c:/Users/balaj/OneDrive/Documents/GitHub/DBFA/master/def6.py
# 12  :is not a prime number!
# 1  :not a prime number!
# 2  :is a prime number!
# 17  :is a prime number!
# PS C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master>
'''

def bubbler(data):
    print(data)
    count = 0
    for i in range (len(data)-1):
        for j in range (0, len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                count += 1
                print(data)
    print("Data sorted in ", count, "turns.")
                

print("The list has been sorted.")                
  
data = [64, 34346, 275, 35, 24, 11, 30] 
print("Original data set: ", data)
bubbler(data)
print("Sorted data set: ", data)
  
#-------------------------------------------OUTPUT-------------------------------------------
# PS C:\Users\balaj\OneDrive\Documents\GitHub\DBFA\master> & C:/Users/balaj/AppData/Local/Programs/Python/Python37/python.exe c:/Users/balaj/OneDrive/Documents/GitHub/DBFA/master/def6.py
# The list has been sorted.
# Original data set:  [64, 34346, 275, 35, 24, 11, 30]
# Sorted data set:  [11, 24, 30, 35, 64, 275, 34346]