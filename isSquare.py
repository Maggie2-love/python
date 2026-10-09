def isSquare(number):
    for count in range(number + 1):
        if count * count == number:
            return True 
            
    return False
    
print(isSquare(25))




def isSquare(number):
    if number<0:
        return False
    square_root= int(number ** 0.5)
    if square_root * square_root == number:
        return True
    else:
        return False
        
print(isSquare(20))
