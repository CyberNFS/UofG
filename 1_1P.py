# ' '.join() – takes an argument (any ch) and joins a second argument (a list of strings)
List = ['first', 'second', 'third']
# they all have to be strings
String = "".join(List)
print(type(String))
# the outcome is a string

# ' '.split() – takes a string (arg) and split it to a list delimeted by second arg (ch)
split = "Strings splitting functions".split(' ')
print(type(split))
# the outcome is a list

# manual looping through elements of a string
# new finding, the ignore underscore ch in fact is accessible
for _ in ' '.join(List):
    pass
    # print(_)

# .index() – finds the position of a substring
Index = String.index('f')
print(type(Index))
# if not in string ValueError is raised
# and the script stops executing

# .find() – finds the position of a substring
Find = String.find('fo')
print(Find)
# returns -1 if not in string
# the script did not stop executing

Replace = String.replace('t', 'T')
print(Replace, '\n')

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# a List can contain elements of different types
Mixed = ['string', 2, 3.0, {'key': 'value'}]
print(type(Mixed))
for _ in Mixed:
    print(type(_), end=' , ')

# whitespace for consistency
print()

Repeating = ["alpha", "bravo", "charlie", "alpha", "echo", "foxtrot"]
# len() – gets the number of elements in a list
Length = len(Repeating)
print(type(Length))
# slicing [start:stop:step], [::-1] – reversing the order of a list
Reversed = Repeating[::-1]

# we can compare the positions of the original and the reversed list
for f, s in enumerate(Reversed):
    pass
    # print(f, s)

for a, b in enumerate(Repeating):
    pass
    # print(a, b)


Membership = 'fourth' not in Reversed
print(type(Membership))
# returns a boolean

Reversed.remove('alpha')
Reversed.remove('alpha')
print(len(Reversed))

a = "program"
a = a.partition('r')
print(a)
