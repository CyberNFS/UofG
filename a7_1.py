# Family Tree
class Person:
    def __init__(self, name, birth_year, death_year=None, mother=None, father=None, person_id=None):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
        self.mother = mother
        self.father = father
        self.id = id(self)
        self.person_id = person_id
        self.last_name = name.split()[-1]

    def age_in_year(self, year):
        if self.death_year and year >= self.death_year:
            return self.death_year - self.birth_year
        else:
            return year - self.birth_year

    def is_alive_in_year(self, year):
        return not self.death_year or year < self.death_year

    def __repr__(self):
        return f"{self.name} ({self.birth_year})"

# ASSERTS FOR B1 ——–––––––——–––––––——–––––––——–––––––——–––––––——–––––––>


# p1 = Person("Alice", 1980)
# p2 = Person("Bob", 1970, 2010)
# p3 = Person("Carol", 1950, mother=p1, father=p2)

# print(p1)  # Alice (1980)
# print(p2.age_in_year(2000))  # 30
# print(p3.is_alive_in_year(2000))  # True


# Reading Data
def read_family(fname):
    people = {}

    with open(fname, 'r') as f:
        for line in f:
            parts = line.strip().split(',')

            year = int(parts[0])
            person_id = parts[1]

            if parts[2] == 'born':
                name = parts[3]
                mother_id = parts[4]
                father_id = parts[5]

                mother = people.get(mother_id)
                father = people.get(father_id)

                person = Person(name, year, mother=mother, father=father)
                people[person_id] = person
            else:  # died
                person = people.get(person_id)
                if person:
                    person.death_year = year

    return people


people = read_family("family_tree.txt")
# for person in people.values():
#     print(person.name)
from pprint import pprint
# pprint(people)


# Simple Queries

# CENSUS
def census(people, year):
    alive = []
    for person in people.values():
        if person.birth_year <= year and (not person.death_year or person.death_year > year):
            alive.append(person)
    return alive


s = census(people, 1940)
# print(s)


# ROLL
def roll(people, year):
    alive = []
    for person in people:
        if person.birth_year <= year and (not person.death_year or person.death_year > year):
            alive.append(person)
    sorted_alive = sorted(alive, key=lambda p: p.last_name)
    lines = []
    for person in sorted_alive:
        age = year - person.birth_year
        lines.append(f'{person.name}, age {age}')
    return '\n'.join(lines)


# print(roll(census(people, 1940), 1940))

# tuples sort check   Queries                                                   !!!!!!!!!!

# FIND


def find_by_name(people, name, year=None):
    matching_people = []
    for person in people.values():
        if person.name == name and (not year or (person.birth_year <= year and (not person.death_year or person.death_year > year))):
            matching_people.append(person)
    return sorted(matching_people, key=lambda p: p.birth_year)


# print(find_by_name(people, "Sonia Bond", 1700))


# MEMORIAL
def memorial(people, year):
    dead_people = []
    for p in people.values():
        if p.death_year is not None and p.death_year < year:
            age_at_death = p.death_year - p.birth_year
            dead_people.append((p, age_at_death))
    dead_people.sort(key=lambda x: (x[0].death_year, x[0].birth_year))
    output_list = [
        f"{p.name} died {p.death_year}, age {age}" for p, age in dead_people]
    output = '\n'.join(output_list)
    return output


# print(memorial(people, 1700))

# # Check who was the last person:
# p_id = "u307493"

# if p_id in people:
#     p = people[p_id]
#     print(f"Found person: {p.name}")
