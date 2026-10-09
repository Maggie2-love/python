def sum_square(numbers):
    sum = 0
    for number in numbers:
        sum +=number **2
      
    return sum
numbers = [2,3,4,5,7]
print(sum_square(numbers))
