#Program to convert celsius to fahrenheit
#4SF20CI002 - ABHIJTH MALLYA
celsius = int(input("Enter the temperature in Celsius :: "))
try :
    fahrenheit = (celsius*1.8) + 32
    print("{} celsius is {} fahrenheit".format(celsius,fahrenheit))
except :
    print("Error occured")