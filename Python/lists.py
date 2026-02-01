# lists
# supplies = ['pens', 'pencils', 'paper', 'stapler']
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i]) 

# assignments
# a = 'AAA'
# b = 'BBB'
# a, b = b, a
# print('a is ' + a)
# print('b is ' + b)

# methods
# remove removes the first occurrence of a value
list1 = ['cat', 'dog', 'rabbit']
list2 = ['cow', 'sheep', 'goat']
list1.extend(list2)
print(list1)
list1.append('horse')
print(list1)
list1.insert(1, 'fox')
print(list1)
list1.remove('dog')
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)
print(list1.index('rabbit'))
print(list1.count('cat'))
list1.clear()
print(list1)    

list3 = ['a','b','A','B']
list3.sort()
print(list3)
list3.sort(key=str.lower)
print(list3)    

# Lists are mutable, meaning their contents can be changed after creation.
# Strings are immutable, meaning they cannot be changed after creation.

spam = [1,2,3,4]
cheese = spam
cheese.append(5)
print(spam)  # Output: [1, 2, 3, 4, 5]
print(cheese)  # Output: [1, 2, 3, 4, 5]

def appendx(someList):
    someList.append('x')    
appendx(spam)
print(spam)  # Output: [1, 2, 3, 4, 5, 'x']

import copy
spam = [1,2,3,4]
cheese = copy.deepcopy(spam)
cheese.append(5)
print(spam)  # Output: [1, 2, 3, 4]
print(cheese)  # Output: [1, 2, 3, 4, 5]
