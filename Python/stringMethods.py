# String Methods in Python

# 1. upper() - Convert to uppercase
text = "hello world"
print(text.upper())  # Output: HELLO WORLD

# 2. lower() - Convert to lowercase
text = "HELLO WORLD"
print(text.lower())  # Output: hello world

# 3. capitalize() - Capitalize first character
text = "hello world"
print(text.capitalize())  # Output: Hello world

# 4. title() - Capitalize first letter of each word
text = "hello world"
print(text.title())  # Output: Hello World

# 5. strip() - Remove leading/trailing whitespace
text = "  hello world  "
print(text.strip())  # Output: hello world

# 6. replace() - Replace substring
text = "hello world"
print(text.replace("world", "python"))  # Output: hello python

# 7. split() - Split string into list
text = "hello world python"
print(text.split())  # Output: ['hello', 'world', 'python']

# 8. join() - Join list elements into string
words = ["hello", "world", "python"]
print(" ".join(words))  # Output: hello world python

# 9. find() - Find substring index
text = "hello world"
print(text.find("world"))  # Output: 6

# 10. startswith() - Check if starts with substring
text = "hello world"
print(text.startswith("hello"))  # Output: True

# 11. endswith() - Check if ends with substring
text = "hello world"
print(text.endswith("world"))  # Output: True

# 12. count() - Count occurrences
text = "hello world hello"
print(text.count("hello"))  # Output: 2

# 13. isdigit() - Check if all characters are digits
print("123".isdigit())  # Output: True
print("abc".isdigit())  # Output: False

# 14. isalpha() - Check if all characters are alphabetic
print("abc".isalpha())  # Output: True
print("123".isalpha())  # Output: False

# 15. isalnum() - Check if all characters are alphanumeric
print("abc123".isalnum())  # Output: True
print("abc 123".isalnum())  # Output: False

# 16. join() - Join list elements with separator
fruits = ["apple", "banana", "orange"]
print(", ".join(fruits))  # Output: apple, banana, orange

numbers = ["1", "2", "3", "4"]
print("-".join(numbers))  # Output: 1-2-3-4

# 17. rjust() - Right justify a string
text = "hello"
print(text.rjust(10))  # Output: "     hello"

# 18. ljust() - Left justify a string
text = "hello"
print(text.ljust(10))  # Output: "hello     "

# 19. center() - Center a string
text = "hello"
print(text.center(11))  # Output: "   hello   "     

# rstrip() - Remove trailing whitespace
text = "hello world   "
print(text.rstrip())  # Output: "hello world"       

# lstrip() - Remove leading whitespace
text = "   hello world"
print(text.lstrip())  # Output: "hello world"   

# pyperclip.copy() - Copy text to clipboard
import pyperclip        
pyperclip.copy("Hello, World pyperclip test!")
print(pyperclip.paste())  # Output: Hello, World!

# String formatting
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")   

# Srring concatenation using % operator
name = "Bob"
age = 25
print("My name is %s and I am %d years old." % (name, age)) 

# use batch file to run multiple python files at once   
