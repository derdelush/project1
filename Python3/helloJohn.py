def hello(firstName, lastName):
    print("Hello", firstName, lastName)

def goodbye():
    firstName, lastName = input("Enter your name: ").split()
    print("Goodbye", firstName, lastName)

hello("John","Smith")
goodbye()
