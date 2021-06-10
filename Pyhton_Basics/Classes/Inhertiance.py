class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name} Age: {self.age}")


# With (Pet) you inherit from the class Pet
class Cat(Pet):
    def speak(self):
        print("Nyaa")


class Dog(Pet):
    def __init__(self, name, age, owner):
        # Call init method from parent class Pet
        super().__init__(name, age)
        self.owner = owner

    def speak(self):
        print("Woof")

    # Overwrite show method
    def show(self):
        print(f"Name: {self.name} Age: {self.age} Owner: {self.owner}")


# pet = Pet("Luxy",2)
# pet.show()

# The Cat class itself doesn't have an init method, but it inherits from Pet
cat = Cat("kitty", 5)
cat.show()
cat.speak()

dog = Dog("doge", 10, "stray")
dog.show()
dog.speak()