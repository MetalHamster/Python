# ordered
# unchangeable
# duplicate allowed
# indexed


# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple4 = ("abc", 34, True, 40, "male")
tuple5 = tuple(("apple", "banana", "cherry"))

# Access
print(tuple5[0])
print(tuple5[-1])

# Unpack
(green, yellow, red) = tuple5
print(green)
print(yellow)
print(red)
