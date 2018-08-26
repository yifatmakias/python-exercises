import random


print("Welcome to the submarine game! :)")
board_size = 10
attempts = 0
submarine_row = random.randint(1, 10)
submarine_col = random.randint(1, 10)
submarine_found = False

while not submarine_found:
    try:
        row = int(input("Enter the row number: "))
        col = int(input("Enter the column number: "))
    except ValueError:
        print("Invalid input")
    if not 1 <= row <= board_size or not 1 <= col <= board_size:
        print("Invalid input")

    if row == submarine_row and col == submarine_col:
        print("Congratulations! exact hit!")
        print("Number of attempts: {}".format(attempts))
        submarine_found = True
    elif abs(row - submarine_row) == 1 or abs(col - submarine_col) == 1:
        print("Your so close!")
        attempts += 1
    elif row == submarine_row or col == submarine_col:
        print("Interesting...")
        attempts += 1
    else:
        print("Keep thinking...")
        attempts += 1
