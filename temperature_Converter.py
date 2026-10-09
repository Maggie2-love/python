#Repeat five times
#Prompt user to input temperature in celsius
#If temperature less than -273 then
#Print Impossible temperature
#Else fahrenheit = (temperature × 9 / 5) + 32
#Print fahrenheit


for number in range(5):
    temperature = float(input("Enter temperature in Celsius: "))

    if temperature < -273:
        print("Impossible temperature!")
    else:
        fahrenheit = (temperature * 9 / 5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)
