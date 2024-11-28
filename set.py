# Accept user input for the first set of integers
set1 = set(map(int, input("Enter integers for the first set (separated by spaces): ").split()))

# Accept user input for the second set of integers
set2 = set(map(int, input("Enter integers for the second set (separated by spaces): ").split()))

# Find the intersection of the two sets
common_elements = set1.intersection(set2)

print(f"Common elements in both sets: {common_elements}")
