class Dog:
    def __init__(self,name,age):
        self.dogName = name
        self.dogAge = age
    def sit(self):
        print(f"{self.dogName} is now sitting")
    def rollOver(self):
        print(f"{self.dogName} rolled over!")

myDog = Dog("Soffi", 12)

print(myDog.dogName, myDog.dogAge)

myDog.sit()
myDog.rollOver()