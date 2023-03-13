
# Cat class – name, weight, age, temperament, colour instance variables.
class Cat:
    def __init__(self, name, weight, age, temperament, colour):
        self.name = name
        self.weight = weight
        self.age = age
        self.temperament = temperament
        self.colour = colour


c = Cat("Cooper", 4.0, 4, "terrible", "gray")
assert hasattr(c, "name") and c.name == "Cooper"
assert hasattr(c, "weight") and c.weight == 4.0
assert hasattr(c, "age") and c.age == 4
assert hasattr(c, "temperament") and c.temperament == "terrible"
assert hasattr(c, "colour") and c.colour == "gray"

# Family Names ––––––––––––––––––––––––––––––––––––––––––––––––––––––>


class FamilyName:
    # Default last name.
    last_name = "Unknown"

    # Initialise the object with the first name
    def __init__(self, first_name):
        self.first_name = first_name

    # Set the last name for all instances of the class.
    @classmethod
    def set_last_name(cls, last_name):
        # First instance is conventionally named cls as self.
        cls.last_name = last_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"


# A2 ASSERTIONS
nm_1 = FamilyName("John")
nm_1.get_name()

nm_1.set_last_name("Williamson")
assert nm_1.get_name() == "John Williamson"

nm_2 = FamilyName("Marco")
assert nm_2.get_name() == "Marco Williamson"

nm_1.set_last_name("Polo")
assert nm_2.get_name() == "Marco Polo"
assert nm_1.get_name() == "John Polo"


# Convert Dictionary ––––––––––––––––––––––––––––––––––––––––––––––––––––––>
import random

# Define class – name, number of sides, shape instances.


class Die:
    def __init__(self, name, sides, shape):
        self.name = name
        self.sides = sides
        self.shape = shape

    # Roll & Return a random value between 1 – number of sides.
    def roll_die(self):
        return random.randint(1, self.sides)

    # Sum of the opposite faces
    def opposite_face_sum(self):
        if self.sides > 4:
            return self.sides + 1
        else:
            raise ValueError("Die has no opposing sides!")


# Given list of dictionaries
dice = [
    {"name": "d6", "sides": 6, "shape": "cube"},
    {"name": "d4", "sides": 4, "shape": "tetrahedron"},
    {"name": "d12", "sides": 12, "shape": "dodecahedron"},
    {"name": "d8", "sides": 8, "shape": "octahedron"},
    {"name": "d20", "sides": 20, "shape": "icosahedron"},
]

# list of Die instances initialised from 'dice' list
dice_class = [Die(die["name"], die["sides"], die["shape"]) for die in dice]

# A3 ASSERTIONS
print(f"\n\nQuestions\n\tfor\n\t\tA3\n")
assert len(dice_class) == len(dice)
assert dice_class[0].__class__.__name__ == "Die"
assert dice_class[0].name == dice[0]["name"]
assert dice_class[0].sides == dice[0]["sides"]
assert dice_class[0].shape == dice[0]["shape"]
for d in dice_class:
    print(f"{d.name} rolled a {d.roll_die()}")

assert dice_class[0].opposite_face_sum() == 7
assert dice_class[-1].opposite_face_sum() == 21

# Fraction ––––––––––––––––––––––––––––––––––––––––––––––––>


class Fraction:
    # Class takes two arguments (num, denom).
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # Return float
    def as_float(self):
        """Returns float division So returns the closest float.
         Update needed for rare cases."""
        return self.numerator / self.denominator

    # Return string
    def as_string(self):
        # f-string"{num}/{denom}"
        return f"{self.numerator}/{self.denominator}"

    # Multiply for both a / b (numerator and denominator)
    def multiply(self, fraction):
        num = self.numerator * fraction.numerator
        denom = self.denominator * fraction.denominator
        return Fraction(num, denom)


# A4 ASSERTIONS
half = Fraction(1, 2)
two_third = Fraction(2, 3)
three_eight = Fraction(3, 8)
assert half.as_float() == 0.5
assert three_eight.as_float() == 3.0 / 8.0
assert two_third.as_string() == "2/3"
assert half.as_string() == "1/2"
prod = half.multiply(two_third)
assert prod.as_float() == (1 / 2) * (2 / 3)
assert prod.as_string() == "2/6"
assert half.as_float() == 0.5
assert half.as_string() == "1/2"

# Special Methods ––––––––––––––––––––––––––––––––––––––––>


class Fraction:
    # Constructor to initialize the numerator and denominator of the fraction
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # Method to get the fraction as a float
    def as_float(self):
        return self.numerator / self.denominator

    # Method to get the fraction as a string
    def as_string(self):
        return f"{self.numerator}/{self.denominator}"

    # Method to multiply the fraction by another fraction or an integer
    def multiply(self, other):
        # If other is an instance of Fraction, multiply the numerators and denominators
        if isinstance(other, Fraction):
            num = self.numerator * other.numerator
            denom = self.denominator * other.denominator
        # If other is an integer, multiply the numerator by the integer
        elif isinstance(other, int):
            num = self.numerator * other
            denom = self.denominator
        # Otherwise, raise a TypeError
        else:
            raise TypeError("Can only multiply by int or Fraction")
        # Return a new Fraction instance with the multiplied values
        return Fraction(num, denom)

    # Method to get the fraction as a string (overrides the default string representation)
    def __str__(self):
        return self.as_string()

    # Method to multiply the fraction by another fraction or an integer using the * operator
    def __mul__(self, other):
        return self.multiply(other)


# A5 ASSERTIONS
half = Fraction(1, 2)
print(f'\n\nQuestions\n\tfor\n\t\tA5\n{half}\n{half * half}\n{half*4}')
assert str(half) == "1/2"
two_third = Fraction(2, 3)
assert str(two_third) == "2/3"
prod = half * two_third
assert str(prod) == "2/6"
assert str(half.multiply(2)) == "2/2"
assert str(half * 2) == "2/2"
try:
    half * 2.0
except TypeError:
    assert True
else:
    assert False, "Didn't fail when multiplying by an float"

# B2 –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––>
from typing import List, Tuple


class Vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scale: float) -> 'Vec3':
        return Vec3(self.x * scale, self.y * scale, self.z * scale)

    def __truediv__(self, scale: float) -> 'Vec3':
        return Vec3(self.x / scale, self.y / scale, self.z / scale)

    def __sub__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def length(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def direction(self) -> 'Vec3':
        return self * (1 / self.length())

    def __matmul__(self, other: 'Vec3') -> float:
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def distance(self, other: 'Vec3') -> float:
        return (self - other).length()

    def __eq__(self, other: 'Vec3') -> bool:
        return self.distance(other) < 1e-6

    def as_list(self) -> List[float]:
        return [self.x, self.y, self.z]

    def __str__(self) -> str:
        return f"<{self.x} {self.y} {self.z}>"


class Path:
    def __init__(self):
        # Return the vector components as a list
        self.points = []

    def add(self, pt: Vec3, t: float):
        # Add the components of two vectors and return a new vector
        self.points.append((t, pt))

    def get(self, t):
        # If there are no points in the path, raise a ValueError
        if len(self.points) == 0:
            raise ValueError("Path is empty")

        # If there is just one point, return it
        if len(self.points) == 1:
            return self.points[0][1]

        # Get the time range of the path
        t_min, t_max = self.t_range()

        # If t is smaller than any time in the path, return the point with smallest t
        if t < t_min:
            return self.points[0][1]

        # If t is greater than any time in the path, return the point with largest t
        if t >= t_max:
            return self.points[-1][1]

        # Find the first time in the list greater than t, t2 and the corresponding point in space p2
        i = 0
        self.points.sort()
        while self.points[i + 1][0] < t:
            i += 1
            if i + 1 == len(self.points):
                break
        if i + 1 == len(self.points):
            return self.points[-1][1]

        # Find the immediately previous point (in the sense of time) in the list p1 and its time t1
        t1, p1 = self.points[i]

        # Compute the position p of the drone at time t using linear interpolation formula
        t2, p2 = self.points[i + 1]
        a = (t - t1) / (t2 - t1)
        p = p1 * (1 - a) + p2 * a
        return p

    def t_range(self) -> Tuple[float, float]:
        if not self.points:
            return (None, None)
        return (min(t for t, _ in self.points), max(t for t, _ in self.points))


# B2 Assertions


# Tests
p = Path()
p.add(Vec3(0, 0, 0), 0.0)
try:
    p.get(0)
except ValueError:
    assert True
p.add(Vec3(1, 0, 0), 1.0)
assert p.t_range() == (0.0, 1.0)
assert p.get(0.0) == Vec3(0, 0, 0)
assert p.get(1.0) == Vec3(1, 0, 0)
p.add(Vec3(1, 0, 1), 2.0)
assert p.get(2.0) == Vec3(1, 0, 1)

assert p.get(0.5) == Vec3(0.5, 0, 0)
assert p.get(0.25) == Vec3(0.25, 0, 0)
assert p.get(1.5) == Vec3(1, 0, 0.5)
assert p.t_range() == (0.0, 2.0)
p.add(Vec3(0, 1, 0), 0.5)
assert p.get(0.5) == Vec3(0, 1, 0)
assert p.get(0.25) == Vec3(0, 0.5, 0)
assert p.get(0.75) == Vec3(0.5, 0.5, 0)

p.add(Vec3(1, 0, 1), -2.0)
assert p.t_range() == (-2.0, 2.0)
assert p.get(-2) == Vec3(1, 0, 1)
