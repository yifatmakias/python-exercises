

listLen = int(input("Enter the list length: "))
numbersList = []
sumNumbers = 0
while listLen > 0:
    number = input("Enter a number: ")
    numbersList.insert(listLen, number)
    sumNumbers += number
    listLen -= 1
print("List:" + str(numbersList))
print("Sum:" + str(sumNumbers))
