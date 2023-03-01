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


class FamilyTree:

    # constructor method takes in a dictionary of People objects
    def __init__(self, tree):
        self.tree = tree

    # class method to load a family tree from a file using read_family

    @classmethod
    def load_from_file(cls, fname):
        return FamilyTree(read_family(fname))

    # method to find a Person object by name and year of birth
    def find_by_name(self, name, year):
        # loop over all the people in the dictionary
        for person in self.tree.values():
            # if the person's name and birth year match, return the Person object
            if person.name == name and person.birth_year == year:
                return person
        # if no Person object is found, return None
        return None

    # method to get the census of a given year
    def census(self, year):
        # create a list to store the people in the census
        census_list = []
        # loop over all the people in the dictionary
        for person in self.tree.values():
            # if the person was alive in the census year, add them to the list
            if person.is_alive_in_year(year):
                census_list.append(person)
        # sort the census list by birth year
        census_list.sort(key=lambda person: person.birth_year)
        # return the sorted census list as a string
        return "\n".join([str(person) for person in census_list])

    # method to get the parents of a given person
    def parents(self, person):
        # get the IDs of the person's parents from their Person object
        father_id, mother_id = person.father_id, person.mother_id
        # if the person has no known father or mother, return None for both
        if father_id == "---" and mother_id == "---":
            return None, None
        # otherwise, look up the Person objects corresponding to the father and mother IDs
        father, mother = self.tree.get(father_id), self.tree.get(mother_id)
        # return the father and mother Person objects
        return father, mother

    # method to get the siblings of a given person
    def siblings(self, person):
        # create a list to store the siblings
        siblings_list = []
        # loop over all the people in the dictionary
        for sibling in self.tree.values():
            # if the sibling has the same father and mother IDs as the given person, they are a sibling
            if sibling.father_id == person.father_id and sibling.mother_id == person.mother_id:
                # exclude the given person from the siblings list
                if sibling.id != person.id:
                    siblings_list.append(sibling)
        # sort the siblings list by birth year
        siblings_list.sort(key=lambda person: person.birth_year)
        # return the sorted siblings list as a string
        return "\n".join([str(person) for person in siblings_list])

    # method to get the children of a given person
    def children(self, person):
        # create a list to store the children
        children_list = []
        # loop over all the people in the dictionary
        for child in self.tree.values():
            # if the child has the given person as a parent, they are a child
            if child.father_id == person.id or child.mother_id == person.id:
                children.append(child)
        return children


f = FamilyTree.load_from_file("family_tree.txt")
print(f.census(1940))
