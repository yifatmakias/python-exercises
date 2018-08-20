
dictionary = {}


def print_options():
    print("Dictionary options:")
    print("1. add new word")
    print("2. search a word")
    print("3. delete a word")
    print("4. exit")


def add():
    key_word = raw_input("Enter the english word: ")
    val_word = raw_input("Enter the translation: ")
    dictionary[key_word] = val_word
    print("The word was entered successfully")


def search():
    key_word = raw_input("Enter the english word to search: ")
    if key_word in dictionary:
        print("The translation is: " + dictionary[key_word])
    else:
        print("This word is not in the dictionary")


def delete():
    key_word = raw_input("Enter the english word to delete: ")
    if key_word in dictionary:
        del dictionary[key_word]
        print("The word was successfully deleted")
    else:
        print("This word is not in the dictionary")


to_exit = False
while to_exit is False:
    print_options()
    try:
        option_number = int(raw_input("Enter your option selection: "))
        if option_number == 1:
            add()
        elif option_number == 2:
            search()
        elif option_number == 3:
            delete()
        elif option_number == 4:
            to_exit = True
        else:
            print("Your option is invalid")
    except ValueError:
        print("Your option is not valid")
