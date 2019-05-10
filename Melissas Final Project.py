print("Welcome to the Car Sales Program!\n\n")

vehiclePrices = {'car':2000, 'truck':3000}
enginePrices = {'v6':2000, 'v8':3000}
totalPrice = 0
responseValid = False
running = True
def log(choice1,choice2):
    logFile = open("MelissasCarSalesLog.txt",'a')
    logFile.write(choice1)
    logFile.write(", ")
    logFile.write(choice2)
    logFile.write(" \n\n")
    logFile.close()
    return True

while running:


    while responseValid == False:
        choice1 = input('Would you like to buy a car or a truck?')
        if choice1.lower() == 'car':
            totalPrice += vehiclePrices['car']
            responseValid = True
        elif choice1.lower() == 'truck':
            totalPrice += vehiclePrices['truck']
            responseValid = True
        else:
            print("You didn't enter a valid answer. Please try again.")
            break
    responseValid = False
        
    while responseValid == False:
        choice2 = input('Would you like to buy a v8 or a v6?')
        if choice2.lower() == 'v6':
            totalPrice += enginePrices['v6']
            responseValid = True
        elif choice2.lower() == 'v8':
            totalPrice += enginePrices['v8']
            responseValid = True
        else:
            print("You didn't enter a valid answer. Please try again.")
            break
    responseValid = False
    running = log(choice1,choice2)
    print("your total price is : $" + str(totalPrice))


