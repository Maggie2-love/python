def minimum_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest  = number
    return smallest

numbers =[8, 4, 9, 2, 5, 7, 3]
print( minimum_number(numbers))
