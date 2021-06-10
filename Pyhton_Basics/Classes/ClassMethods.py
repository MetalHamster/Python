class Person:
    # Class attribute, defined outside a methode and without self
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        # Call classmethod
        Person.add_person()

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

p1 = Person("Jim")
p2 = Person("Bin")

print(Person.get_number_of_people())
