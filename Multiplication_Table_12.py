print("                 Multiplication Table")
print("      1   2   3   4   5   6   7   8   9 10  11  12")
print("    -----------------------------------------------")

for number in range(1, 13):
    print(f"{number} |", end="")

    for count in range(1, 13):
        print(f"{number * count:4}", end="")

    print()
