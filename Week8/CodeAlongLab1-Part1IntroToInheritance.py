class Animal():
    def __init__(self):
        print("Animal created")
    def whoamI(self):
        print("I am an animal")
    def eat(self):
        print("I am now eating")
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):
    def __init__ (self, name):
        Animal.__init__(self)
        print("Dog created")
        self.name = name
    def whoamI(self):
        print("I am a Dog, my name is", self.name)
    def eat(self):
        print("I am now eating")
    def speak(self):
        return self.name + " says woof!"


class Cat(Animal):
    def __init__ (self, name):
        Animal.__init__(self)
        print("Dog created")
        self.name = name
    def whoamI(self):
        print("I am a Cat, my name is", self.name)
    def eat(self):
        print("I am now eating")
    def speak(self):
        return self.name + " says meow!"

class Bird(Animal):
    def __init__ (self, name):
        Animal.__init__(self)
        print("Dog created")
        self.name = name
    def whoamI(self):
        print("I am a Bird, my name is", self.name)
    def eat(self):
        print("I am now eating")


def pet_speak(pet):
    print(pet.speak())

fido = Dog("Fido")
felix = Cat("Felix")
polly = Bird("Polly")

pet_speak(fido)
pet_speak(felix)