print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Divide")

# Get user choice
option = int(input("Choose an operation: "))

# Check if the option is valid
if option in [1, 2, 3, 4]:
    # Get the numbers and convert them to integers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Perform the selected operation
    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
      
        if num2 != 0:
            result = num1 / num2  
        else:
            result = "undefined (division by zero)"
    
    print(f"The result of the operation is: {result}")
else:
    print("Invalid operation entered.")
