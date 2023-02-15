# birthday book function

book = {}


# def add_to_book(**kwargs):
#     for key, value in kwargs.items():
#         book[key] = value


# add_to_book(
#     John={"month": "Jan", "date": 17},
#     Jane={"month": "Feb", "date": 14},
#     Jim={"month": "Mar", "date": 21})

# print(book, end='\n')

def booking(name, month, date):
    book[name] = {'month': month, 'date': date}


booking('John', 'Sep', 12)
booking('Elsa', 'Dec', 14)
booking('Juli', 'Jan', 31)
booking('Tivadar', 'Jul', 11)
booking('Anna', 'Sep', 21)
booking('Uki', 'Dec', 22)
booking('Puki', 'Jan', 23)
booking('Sumbuly', 'Jul', 25)


def birthday(name):
    if name in book:
        return book[name]['month'], book[name]['date']
    return 'The name is not in the book library yet. Add birthday using booking(name, month, date)'


print(birthday('John'))


def birthdays(month):
    result = []
    for name, info in book.items():
        if info['month'] == month:
            result.append((name, info['month'], info['date']))
    print(result)


birthdays('Jan')


def getBirthdays(fileName, book):
    with open(fileName, 'r') as f:
        for line in f:
            name, month, day = line.strip().split()
            book[name] = {'month': month, 'day': int(day)}


# Example usage
book = {}
getBirthdays('birthdays.txt', book)
print(book)


def activityNotifications(fileName):
    with open(fileName) as f:
        n, d = map(int, f.readline().strip().split())
        expenditure = list(map(int, f.readline().strip().split()))
        count = 0
        for i in range(n - d):
            trailing_expenditure = expenditure[i:i + d]
            trailing_expenditure.sort()
            median = trailing_expenditure[d // 2]
            if expenditure[i + d] >= 2 * median:
                count += 1
        return count
