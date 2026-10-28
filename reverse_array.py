def reverse_number(numbers):

    for row in range(len(numbers)):

        for index in range(len(numbers[row])):

            for column in range(len(numbers[row])):

                if numbers[row][column] < numbers[row][index]:

                    temp = numbers[row][column]

                    numbers[row][column] = numbers[row][index]

                    numbers[row][index] = temp


numbers = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
          ]

reverse_number(numbers)

for row in range(len(numbers)):

    for column in range(len(numbers[row])):

        print(numbers[row][column], end="   ")

    print()
