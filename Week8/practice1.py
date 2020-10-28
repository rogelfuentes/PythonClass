class Animal:
    def __init__(self):
            print("Animal constructor created")
    
    def whoami(self):
        print("I'm a animal")
    def eat(self):
        print("Animal eating")
    def speak(self):
        raise NotImplementedError("Subclass must implement this ")
        # pass
        # print("Animal is speaking")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self)
        self.name = name
    
    def whoami(self):
        print("I'm a dog, my name is: ", self.name)
    def eat(self):
        print("I'm eating")
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    def __init__(self, name):
        # **************************************
        Animal.__init__(self)
        # *************************************
        self.name = name
    
    def whoami(self):
        print("I'm a cat, my name is: ", self.name)
    def eat(self):
        print("I'm eating")
    def speak(self):
         return self.name + " says meow!"

class Bird(Animal):
    def __init__(self, name):
        Animal.__init__(self)
        self.name = name
    
    def whoami(self):
        print("I'm a bird, my name is: ", self.name)
    def eat(self):
        print("I'm eating")
    # def speak(self):
    #      return self.name + " says piopio"



def pet_speak(pet):
    print(pet.speak())

fido = Dog('fido')
felix = Cat('felix')

pet_speak(fido)
pet_speak(felix)
