# Question 6: Right-Aligned Triangle

for i in range(1, 6):

    # Print spaces before stars
    for j in range(5 - i):
        print(" ", end=" ")

    # Print stars
    for j in range(i):
        print("*", end=" ")

    print()