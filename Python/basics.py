# spam=0
# while spam < 5:
#     print('Hello world')
#     spam = spam+1

# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')

# name = 'Jimmy'
# for i in range(5):
#     print('Jimmy five times (' + str(i) + ')')

# total = 0
# for num in range(101):
#     total = total + num
# print(total)

# range(start, stop, step)
# for i in range(0, 10, 2):
#     print(i)
# for i in range(5, 0, -1):
#     print(i)

# import random
# i = random.randint(1, 10)
# print(i)

from random import *
i = randint(1, 10)
print(i)

import sys
print('Hello')
sys.exit()
print('Goodbye')  # This line will not be executed