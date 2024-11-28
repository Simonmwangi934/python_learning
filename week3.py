# Function to check if the power of base raised to exponent is greater than 5000
def large_power(base, exponent):
    # Calculate base raised to the power of exponent
    result = base ** exponent
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Function to check if a number is divisible by ten
def divisible_by_ten(num):
    # Check if the number is divisible by 10 using modulus
    if num % 10 == 0:
        return True
    else:
        return False

# Example Usage
if __name__ == "__main__":
    # Test large_power function
    print("Testing large_power:")
    print(f"large_power(2, 13): {large_power(2, 13)}")  
    print(f"large_power(2, 10): {large_power(2, 10)}")  

    # Test divisible_by_ten function
    print("\nTesting divisible_by_ten:")
    print(f"divisible_by_ten(50): {divisible_by_ten(50)}") 
    print(f"divisible_by_ten(37): {divisible_by_ten(37)}") 
