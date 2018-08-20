

number = int(input("Please enter a 4 digits number: "))
if not number >= 1000 and number <= 9999:
    print("Your number is invalid")
else:
    print("The number is: "+str(number))
    print("The digits of the number are:")
    digitsSum = 0
    while number > 0:
        print(number % 10)
        digitsSum = digitsSum + number % 10
        number = number / 10
    print("The sum of the digits is: "+str(sum))