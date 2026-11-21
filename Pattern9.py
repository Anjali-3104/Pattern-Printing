# Question 9: Diamond Pattern
# Print the upper half of the diamond.
for i in range(1, 6):
# Add spaces to center this row.
    for j in range(5 - i):
        print(" ", end=" ")
    # Print an odd number of stars.
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

# Print the lower half, with fewer stars in each row.
for i in range(4, 0, -1):
    # Add spaces to keep this half centered.
    for j in range(5 - i):
        print(" ", end=" ")
        # Print an odd number of stars.
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()