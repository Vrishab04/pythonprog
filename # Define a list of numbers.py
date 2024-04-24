# Define a list of numbers
numbers = [12, 3, 20, 5, 8, 11, 15, 2]

# Initialize variables to store the largest even and odd numbers
largest_even = None
largest_odd = None

# Iterate over the list of numbers
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        # Check if the number is larger than the current largest even number
        if largest_even is None or num > largest_even:
            # Update the largest even number
            largest_even = num
    # Check if the number is odd
    else:
        # Check if the number is larger than the current largest odd number
        if largest_odd is None or num > largest_odd:
            # Update the largest odd number
            largest_odd = num

# Print the largest even and odd numbers
print("Largest even number: ", largest_even)
print("Largest odd number: ", largest_odd)