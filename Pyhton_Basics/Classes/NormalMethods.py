# Define class
class Toaster:
    # Create Methods

    # This method will be called, when the object is created
    # Any parameters when creating the object will be used in this method
    def __init__(self, name):
        # self references the current instance of the class
        self.name = name

    def start_toasting(self):
        print("Toasting . . .")

    def get_name(self):
        return self.name


# Create object of class Toaster
toaster = Toaster("Toast factory")
# Call function
toaster.start_toasting()
print(toaster.get_name())
