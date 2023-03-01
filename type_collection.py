class TypeCollection:
    def __init__(self):
        self.type_dict = {}

    def add(self, obj):
        # Get the type name of the object
        type_name = type(obj).__name__

        # Add the object to the appropriate list in the dictionary
        if type_name in self.type_dict:
            self.type_dict[type_name].append(obj)
        else:
            self.type_dict[type_name] = [obj]

    def remove(self, obj):
        # Get the type name of the object
        type_name = type(obj).__name__

        # Raise a ValueError if the type name is not in the dictionary
        if type_name not in self.type_dict:
            raise ValueError("Object not found in collection")

        # Remove the object from the appropriate list in the dictionary
        self.type_dict[type_name].remove(obj)

    def remove_all(self, typename):
        # Remove all objects of the given type name from the dictionary
        if typename in self.type_dict:
            del self.type_dict[typename]

    def get_all(self, typename):
        # Return all objects of the given type name
        if typename in self.type_dict:
            return self.type_dict[typename]
        else:
            return []

    def __str__(self):
        # Sort the type names alphabetically and create a string representation of the objects
        output = ""
        for type_name in sorted(self.type_dict.keys()):
            output += f"{type_name}\n"
            for obj in self.type_dict[type_name]:
                output += f"    {obj}\n"
        return output


# A6 Tests
print(f"\n\nQuestions\n\tfor\n\t\tA6\n")
t = TypeCollection()
t.add(1)
t.add(1.0)
t.add("1")
t.add("hey")
t.add(9)
t.add(2)
t.add((3, 4))
t.remove(1)

print(f"\tt is:\n{t}")
assert t.get_all("int") == [9, 2]
assert t.get_all("str") == ["1", "hey"]
assert t.get_all("tuple") == [(3, 4)]
t.remove_all("int")
assert t.get_all("int") == []

print('Bottom-line\nAll Clear.')
