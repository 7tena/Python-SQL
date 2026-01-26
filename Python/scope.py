# def bacon():
#     eggs = 42  # Local variable
#     print(eggs)

# def spam():
#     eggs = 99  # Local variable
#     bacon()
#     print(eggs) 

# bacon()
# spam()  # Calls the first spam function again
eggs = "Hello"
def eggss():
    # global eggs
    # eggs = 10
    print(eggs)  # This will cause an error because eggs is not defined globally
    


eggss()  # Calls the eggs function which prints the global eggs variable
print(eggss())