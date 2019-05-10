vehiclePrices = {'car':2000, 'truck':3000}
enginePrices = {'v6':2000, 'v8':3000}
pricePerCar = 2000
pricePerTruck = 3000
pricePerEnginev6 = 2000
pricePerEnginev8= 3000
totalPrice = 0
yesChoice = ['yes', 'y']
noChoice = ['no', 'n']


print("Welcome to the Car Sales Program!\n\n")

Intro = (input("Would you like to buy a new vechicle?\n\nPlease enter y/n."))

def ask_yes_no(question):
    """Ask a yes or no question"""

    allowed_answers = ("y", "yes", "n", "no")
    response = None
    while response not in allowed_answers :
        response = input(question).lower()
        if response not in allowed_answers:
            print("That is not a valid response.")
    return response

Choice1 = input("would you like to buy a car or a truck today?\n\nPlease enter car or truck")
allowed_answers = ("car","truck")
response = None
while response not in allowed_answers :
    response = input(Choice1).lower()
    if response not in allowed_answers:
        print("That is not a valid response.")

Choice2 = input("would you like it to have a v6 or a v8 engine?\n\nPlease enter v6 or v8")
allowed_answers = ("v6","v8")
response = None
while response not in allowed_answers :
    response = input(Choice2).lower()
    if response not in allowed_answers:
        print("That is not a valid response.")




totalPrice = pricePerCar or pricePerTruck + pricePerEnginev6 or pricePerEnginev8
print("your total price is : $" + str(totalPrice))
