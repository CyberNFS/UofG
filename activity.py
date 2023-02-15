import sys


def activityNotifications(fileName):
    with open(fileName) as f:
        # n - number of spending activities
        # d - number of trailing days
        n, d = map(int, f.readline().strip().split())
        expenditure = list(map(int, f.readline().strip().split()))
        # initialise count
        count = 0
        frequency_dict = [0] * 2001
        # number of days – frequency
        for i in range(d):
            frequency_dict[expenditure[i]] += 1
        # create the arrays
        for i in range(n - d):
            trailing_expenditure = expenditure[i:i + d]
            # find median help function below
            median = find_median(frequency_dict, d)
            # set notification condition
            if expenditure[i + d] >= 2 * median:
                count += 1
            frequency_dict[expenditure[i]] -= 1
            frequency_dict[expenditure[i + d]] += 1
        print(count)


def find_median(frequency_dict, d):
    if d % 2 == 0:
        first_median_index = d // 2
        second_median_index = first_median_index - 1
        first_median = get_index(frequency_dict, first_median_index)
        second_median = get_index(frequency_dict, second_median_index)
        return (first_median + second_median) / 2
    else:
        median_index = d // 2
        median = get_index(frequency_dict, median_index)
        return median

# get the value at specific index in the frequency dictionary


def get_index(frequency_dict, index):
    # initialise count
    count = 0
    for i in range(2001):
        count += frequency_dict[i]
        if count > index:
            return i


activityNotifications(sys.argv[1])
