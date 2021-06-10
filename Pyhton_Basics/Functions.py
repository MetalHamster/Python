# Definition of a function
def my_function():
    print("Hello from a function")
    print("Block function")


# Calling a function
my_function()


# With parameters
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


# With return
def my_function(x):
    return 5 * x


print(my_function(3))
