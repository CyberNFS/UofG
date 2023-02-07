import sys


def activityNotifications(fileName):
    with open(fileName) as f:
        n, d = map(int, f.readline().strip().split())
        expenditure = list(map(int, f.readline().strip().split()))
        count = 0
        trailing_expenditure = [0] * d
        for i in range(d):
            trailing_expenditure[i] = expenditure[i]
        for i in range(n - d):
            sorted_expenditure = radix_sort(trailing_expenditure)
            median = find_median(sorted_expenditure, d)
            if expenditure[i + d] >= 2 * median:
                count += 1
            trailing_expenditure = update_trailing_expenditure(
                trailing_expenditure, expenditure[i], expenditure[i + d])
        print(count)


def radix_sort(expenditure):
    max_expenditure = max(expenditure)
    exponent = 1
    while max_expenditure // exponent > 0:
        expenditure = counting_sort(expenditure, exponent)
        exponent *= 10
    return expenditure


def counting_sort(expenditure, exponent):
    n = len(expenditure)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = expenditure[i] // exponent
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = expenditure[i] // exponent
        output[count[index % 10] - 1] = expenditure[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        expenditure[i] = output[i]
    return expenditure


def find_median(expenditure, d):
    if d % 2 == 0:
        first_median_index = d // 2
        second_median_index = first_median_index - 1
        first_median = expenditure[first_median_index]
        second_median = expenditure[second_median_index]
        return (first_median + second_median) / 2
    else:
        median_index = d // 2
        median = expenditure[median_index]
        return median


def update_trailing_expenditure(trailing_expenditure, remove, add):
    trailing_expenditure.remove(remove)
    trailing_expenditure.append(add)
    return trailing_expenditure


activityNotifications(sys.argv[1])
