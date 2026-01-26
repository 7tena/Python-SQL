def divideby42(num):
    try:
        result = 42/int(num)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input type. Please provide a number.")
    else:
        print(result)
    
num = input("Enter a number to divide 42: ")
divideby42(num)