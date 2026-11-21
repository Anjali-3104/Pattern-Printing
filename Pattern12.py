# Question 12: Butterfly Pattern

# Print the upper half, increasing the wing size.
for i in range(1, 6):
    # Print the left wing.
    for j in range(i):
        print("*", end=" ")
    # Add spaces between the two wings.
    for j in range(2 * (5 - i)):
        print(" ", end=" ")
    for j in range(i):
    # Print the right wing.
        print("*", end=" ")
    print()

# Print the lower half, decreasing the wing size.
for i in range(4, 0, -1):
    # Print the left wing.
    for j in range(i):
        print("*", end=" ")
    # Add spaces between the two wings.
    for j in range(2 * (5 - i)):
        print(" ", end=" ")
    #Print the right wing.
    for j in range(i):
        print("*", end=" ")
    print()
