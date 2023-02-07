import datetime
import string

book = {}


# def add_to_book(name, month, day):
#     book[name] = {'month': month, 'day': day}

def add(book, name, month, day):
    # Check if day is within the range for each month
    try:
        if month == "Jan" or month == "Mar" or month == "May" or month == "Jul" or month == "Aug" or month == "Oct" or month == "Dec":
            if not (0 < int(day) <= 31):
                raise ValueError(
                    "Error: Invalid day for the month of {}".format(month))
        elif month == "Apr" or month == "Jun" or month == "Sep" or month == "Nov":
            if not (0 < int(day) <= 30):
                raise ValueError(
                    "Error: Invalid day for the month of {}".format(month))
        elif month == "Feb":
            if not (0 < int(day) <= 29):
                raise ValueError(
                    "Error: Invalid day for the month of {}".format(month))
        else:
            raise ValueError("Error: Invalid month")
    except ValueError:
        print("Invalid range")
    except TypeError:
        print("Day has to be a number.")

    # Add the birthday to the book
    book[name] = {"month": month, "day": int(day)}


def get_birthday(name):
    if name in book:
        return f"{name}'s birthday is on {book[name]['month']} {book[name]['day']}"
    else:
        return f"No birthday found for {name}"


def get_birthdays(file_name, book):
    try:
        with open(file_name, 'r') as f:
            for line in f:
                name, month, day = line.strip().split(',')
                add(book, name, month, day)
        print(f'{file_name} was read.\n')
    except FileNotFoundError:
        print("Error: File not found.\n")
    except NameError:
        print("Error: Name not found.\n")


def list_birthdays(month):
    birthdays = [
        f"{name} on {book[name]['day']}" for name in book if book[name]['month'] == month]
    if birthdays:
        return f"Birthdays in {month}: " + ', '.join(birthdays)
    else:
        return "No birthdays found for the month"


def predict_upcoming_birthdays():
    now = datetime.datetime.now()
    current_month = now.strftime("%b")
    current_day = now.day
    next_week = now + datetime.timedelta(days=7)
    upcoming_birthdays = [f"{name} on {book[name]['day']}" for name in book if book[name]['month'] == current_month and int(
        book[name]['day']) >= current_day and int(book[name]['day']) <= next_week.day]
    if upcoming_birthdays:
        return "Upcoming birthdays in the next week: " + ', '.join(upcoming_birthdays)
    else:
        return "No upcoming birthdays in the next week."


while True:

    command = input("command(press 0 for help) : ")

    if command == '0' or command == 'menu' or command == 'help' or command == '?':
        print("\nRead in text file to operate on it.\nUse commands such as read, get, etc. or command numbers.")
        print("\nMenu:")
        print("1. Add a birthday")
        print("2. Get a birthday")
        print("3. Read birthdays from file")
        print("4. List birthdays in a month")
        print("5. Predict upcoming birthdays in the next week")
        print("6. Quit")

    elif command == '1' or command == 'add':
        name = input("Enter name: ").capitalize()
        month = input("Enter month (e.g. Jan, Feb, etc.): ").capitalize()
        day = input("Enter day: ")
        try:
            add(book, name, month, day)
        except ValueError:
            print('Day has to be a real integer value.')

    elif command == '2' or command == 'get':
        name = input("Enter name: ")
        print(get_birthday(name), '\n')

    elif command == '3' or command == 'read':
        file_name = input("Enter file name: ")
        get_birthdays(file_name, book)

    elif command == '4' or command == 'list':
        month = input("Enter month (e.g. Jan, Feb, etc.): ").capitalize()
        print(list_birthdays(month), '\n')

    elif command == '5' or command == 'predict' or command == 'p':
        print(predict_upcoming_birthdays(), '\n')

    elif command == '6' or command == 'quit' or command == 'q':
        break

    else:
        print("Invalid command.\n")
