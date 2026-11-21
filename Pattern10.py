# Question 10: Hollow Square

# Check each position in the 5-by-5 square.
for i in range(5):
    for j in range(5):
        # Print stars along the four edges.
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        # Leave the inside of the square empty.
        else:
            print(" ", end=" ")# Print spaces inside the square.
    print()