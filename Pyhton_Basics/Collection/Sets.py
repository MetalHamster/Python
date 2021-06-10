# unordered
# unchangeable
# no duplicate values.
# no indexes

# Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set4 = {"abc", 34, True, 40, "male"}
set5 = set(("apple", "banana", "cherry"))

# Access
for i in set1:
    print(i)

print("apple" in set1)

# Add
set1.add("orange")

# Update
set1.update(set2)

# Remove #Discard #Pop
