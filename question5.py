# Store a list of words
words = input("Enter a list of words separated by spaces: ").split()

# Create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

print(f"Words with an odd number of characters: {odd_length_words}")
