# indexing[]
name = "Matthias Flueckiger"

# [start:stop:step]
first_name = name[0:8:1]  # short -> [:8]
last_name = name[9:19:1]  # short -> [9:]
only_step = name[0:19:1]  # short -> [::1]

print(first_name)
print(last_name)

# slicing()

website1 = "https://google.ch"
website2 = "https://bing.ch"

slice = slice(8, -3)

print("Website 1: "+website1[slice])
print("Website 2: "+website2[slice])
