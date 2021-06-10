# ordered
# changeable
# duplicates allowed
# indexed

# append()	Add an element to the end of the list
# clear()	Removes all items from the list
# copy()	Returns a copy of the list
# count()	Returns the count of number of items passed as an argument
# extend()	Add the elements of a list to the end of the current list
# index()	Returns the index of the first matched item
# insert()	Insert an item at the defined index
# pop()		Removes and returns an element at the given index
# remove()	Removes an item from the list
# reverse()	Reverse the order of items in the list
# sort()	Sort items in a list in ascending order


# Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

# Constructor mostly for cast a different collection type
list5 = list(("apple", "banana", "cherry"))


# Add an item at the end
list1.append("pear")
list1.append("pear")

# Insert at specific position
list1.insert(0, "orange")

# Remove the first occurrence of the value
list1.remove("pear")

# Loop through list
for i in list1:
    print(i)

# Sort
list1.sort()

for i in list1:
    print(i)
