import sys


def add_to_birthday_book(birthday_book, name, birthday):
    birthday_book[name] = birthday
    return birthday_book


def print_birthday(birthday_book, name):
    if name in birthday_book:
        birthday = birthday_book[name]
        print(f"{name}'s birthday is on {birthday['month']} {birthday['day']}")
    else:
        print(f"No birthday found for {name}.")


if __name__ == "__main__":
    birthday_book = {}

    while True:
        print("Enter name (or 'q' to quit):")
        name = input()
        if name == 'q':
            break
        print("Enter month:")
        month = input()
        print("Enter day:")
        day = int(input())
        birthday = {'month': month, 'day': day}
        birthday_book = add_to_birthday_book(birthday_book, name, birthday)

    if len(sys.argv) == 2:
        name = sys.argv[1]
        print_birthday(birthday_book, name)
    else:
        print("Please provide a name.")
