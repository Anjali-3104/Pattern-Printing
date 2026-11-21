# Question 11: Hollow Right-Angled Triangle
# Build the triangle one row at a time.
for i in range(1, 6):
    for j in range(1, i + 1):
        # Print stars on the left edge, diagonal, and bottom row.
        if j == 1 or j == i or i == 5:
            print("*", end=" ")
            # Leave the inner positions blank.
        else:
            print(" ", end=" ")
    print()