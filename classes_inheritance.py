# Question 1:
# Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two
# instance variables, color and price. Assign to the variable testOne an instance of Bike who's color is blue and
# who's price is 89.99. Assign to the variable testTwo an instance of Bike who's color is purple and who's price is # 25.0.

class bike():
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def getC(self):
        return self.color

    def getP(self):
        return self.price


testOne = bike("blue", 89.99)
testTwo = bike("purple", 25.0)

# Question 2:
# Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing
# a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. 
# Write a class method called increase that increases the quantity by 1 each time it is invoked. You should also write a 
# str method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples."
# e.g. "A basket of 4 red apples." or "A basket of 50 blue apples."

class AppleBasket():
    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity

    def getC(self):
        return self.apple_color

    def getQ(self):
        return self.apple_quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)


print(AppleBasket("Red", 4))

# Question 3:
# Define a class called BankAccount that accepts the name you want associated with you're bank account in a string,
# and an integer that represents the amount of money in the account. The constructor should initialize two instance
# variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount,
# you see "You're account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with
# "Bob" as the name and 100 as the amount. Save this to the variable t1.

class BankAccount():

    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def getN(self):
        return self.name

    def getA(self):
        return self.amt

    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt)


t1 = BankAccount("Bob", 100)
print(t1)
