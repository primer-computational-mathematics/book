# Dictionaries
``` {index} Dictionaries
```
A dictionary is a Python data structure that can store data as key-value pairs. The syntax is:

    dict1 = {key1: value1, key2: value2, key3: value3, etc...}
Keys can be strings or numbers and values can be anything: strings, numbers, lists, arrays, etc. Keys must be unique - if you set it twice, the second value replaces the first.

rocks_dict = {"basalt": 1, "granite": 2,
              "marl": 3, "gneiss": 4, 
              "shale": 5}
print(rocks_dict)

We can access and modify values based on their key:

# Access value with key 'basalt'
print(rocks_dict["basalt"])

# Create a new key 'sandstone' with value 6
rocks_dict["sandstone"] = 6
print(rocks_dict)

# Add another key/valye pair to the dictionary
rocks_dict.update({"schist": 7})
print(rocks_dict)

# Remove new entry
del rocks_dict["sandstone"]
print(rocks_dict)

# Remove entry
rocks_dict.pop("schist")
print(rocks_dict)

We can also search and iterate over keys:

# Search if key 'granite' exists
if "granite" in rocks_dict:
    print(rocks_dict["granite"])
    
# Iterate over keys in rocks_dict
for key in rocks_dict:
    print(key, rocks_dict[key])