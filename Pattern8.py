# Question 8: Inverted Star Pyramid
# Start with 9 stars and reduce the number in each row.
for i in range(5, 0, -1):
    # Add spaces to keep the stars centered.
    for j in range(5 - i):
        print(" ", end=" ")
    # Print an odd number of stars for this row.
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
