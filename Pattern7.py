# Question 7: Star Pyramid

for i in range(1, 6):
    # Add spaces to keep the stars centered.
    for j in range(5 - i):
        print(" ", end=" ")
    # Print an odd number of stars in each row.
    for j in range(2 * i - 1):
        print("*", end=" ")# The number of stars is odd: 1, 3, 5, 7, and 9.
    print()