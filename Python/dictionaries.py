# Dictionaries are mutable, unordered collections of key-value pairs in Python. 
# They are defined using curly braces {} with keys and values separated by colons. 
# Here's a brief overview of how to create, access, modify, and delete items in a dictionary:
# Create a dictionary:
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(my_dict)      
# Accessing values:
print(my_dict['key1'])  # Output: value1
# Modifying values:
my_dict['key2'] = 'new_value2'
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'new_value2', 'key3': 'value3'}
# Adding new key-value pairs:
my_dict['key4'] = 'value4'
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'new_value2', 'key3': 'value3', 'key4': 'value4'}
# Deleting key-value pairs:
del my_dict['key3']
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'new_value2', 'key4': 'value4'}
# Dictionary methods:
print(my_dict.keys())    # Output: dict_keys(['key1', 'key2', 'key4'])
print(my_dict.values())  # Output: dict_values(['value1', 'new_value2', 'value4'])
print(my_dict.items())   # Output: dict_items([('key1, 'value1'), ('key2', 'new_value2'), ('key4', 'value4')])
# Checking if a key exists:
print('key2' in my_dict)  # Output: True
print('key3' in my_dict)  # Output: False
# Looping through a dictionary:
for key, value in my_dict.items():
    print(f"{key}: {value}")
for key in my_dict.keys():
    print(f"{key}: {my_dict[key]}")
for value in my_dict.values():
    print(value)
# Output:
# key1: value1
# key2: new_value2
# key4: value4
# Nested dictionaries:
print(my_dict.get('key8',0))  # Output: value1
my_dict.setdefault('color','red')
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'new_value2', 'key4': 'value4', 'color': 'red'}    
my_dict.setdefault('color','black')
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'new_value2', 'key4': 'value4', 'color': 'red'}

# charactercount
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
charCount = {}
for character in message.upper():
    charCount.setdefault(character,0)
    if character not in charCount:
        charCount[character] = 1
    else:
        charCount[character] += 1   
pprint.pprint(charCount)
stringcharcount = pprint.pformat(charCount)
print(stringcharcount)