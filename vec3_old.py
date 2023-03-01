import math


class Vec3:
    def __init__(self, x, y, z):
        # Initialize the components of the vector
        self.x = x
        self.y = y
        self.z = z

    def as_list(self):
        # Return the vector components as a list
        return [self.x, self.y, self.z]

    def __add__(self, other):
        # Add the components of two vectors and return a new vector
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scale):
        # Multiply each component of the vector by a scalar and return a new vector
        return Vec3(self.x * scale, self.y * scale, self.z * scale)

    def __truediv__(self, scale):
        # Divide each component of the vector by a scalar and return a new vector
        return Vec3(self.x / scale, self.y / scale, self.z / scale)

    def length(self):
        # Calculate the length of the vector using the Pythagorean theorem
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def direction(self):
        # Calculate the unit vector (direction) by dividing each component by the length
        return self * (1 / self.length())

    def __matmul__(self, other):
        # Calculate the dot product of two vectors
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __sub__(self, other):
        # Subtract the components of two vectors and return a new vector
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def distance(self, other):
        # Calculate the distance between two vectors using the Pythagorean theorem
        return (self - other).length()

    def __str__(self):
        # Return the vector as a string in the format "<x y z>"
        return f"<{self.x} {self.y} {self.z}>"

    def __eq__(self, other):
        # Check if the distance between two vectors is less than 1e-6
        return self.distance(other) < 1e-6


# B1 ASSERTIONS

v1 = Vec3(1, 2, 3)
v2 = Vec3(1.0, 0.0, 1.0)
v3 = Vec3(1.0, 0.0, 0.0)
v4 = Vec3(10.0, 0.0, 0.0)
v5 = Vec3(0.0, 0.0, 1.0)

print(
    f'Vec3(1, 2, 3) =\t\t\t\t\t\t\t{v1}\ntype =\t\t\t\t\t\t\t\t\t{type(v1)}\n\nVec3(1.0, 0.0, 1.0) =\t\t\t\t\t{v2}\n\nVec3(1.0, 0.0, 0.0) =\t\t\t\t\t{v3}\n')
print(
    f'\tCalculations\n\nv1 * 2 =\t\t\t\t\t\t\t\t{v1 * 2}\n\nv1 + v2 - v3 + v4 - v5 * 2 =\t\t\t{v1 + v2 - v3 + v4 - v5 * 2}\n')
print('length of "Vec3(1.0, 0.0, 0.0)" =\t\t', v3.length())


assert v3 * 10 == v4
assert v4 / 10 == v3

assert v1 - v2 == Vec3(0, 2, 2)
assert v1 + v2 == Vec3(2, 2, 4)
assert v3 + v5 == Vec3(1, 0, 1)

assert v3.length() == v5.length()
assert v1.length() == 14**0.5
assert v3.length() == 1.0

assert v3.distance(v5) == 2.0**0.5
assert v4.direction() == v3
assert v5.direction() == v5
# @ calls __matmuL__

assert v3 @ v3 == 1.0
assert v3 @ v5 == 0.0

assert v3.as_list() == [1.0, 0.0, 0.0]
assert (v3 * 2).as_list() == [2.0, 0.0, 0.0]


# Path ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––>

class Path:
    def __init__(self):
        # Initialize an empty list to store points as (time, point) tuples
        self.points = []

    def add(self, pt, t):
        # Add a new point as a (time, point) tuple to the list
        self.points.append((t, pt))

    def get(self, t):
        # If there are no points in the path, raise a ValueError
        if not self.points:
            raise ValueError("No points in path")

        # If there is just one point, return it
        if len(self.points) == 1:
            return self.points[0][1]

        # If t is smaller than any time in the path, return the point with smallest t
        if t <= self.points[0][0]:
            return self.points[0][1]

        # If t is greater than any time in the path, return the point with largest t
        if t >= self.points[-1][0]:
            return self.points[-1][1]

        # Otherwise, find the two points between which t lies
        for i in range(len(self.points) - 1):
            if self.points[i][0] <= t < self.points[i + 1][0]:
                # Interpolate between the two points and return the result
                t1, p1 = self.points[i]
                t2, p2 = self.points[i + 1]
                a = (t - t1) / (t2 - t1)
                return p1 * (1 - a) + p2 * a

    def t_range(self):
        # If there are no points in the path, return None
        if not self.points:
            return None
        # Otherwise, return the minimum and maximum value of t
        return (self.points[0][0], self.points[-1][0])

# B2 Assertions


# Tests
# p = Path()
# p.add(Vec3(0, 0, 0), 0.0)
# try:
#     p.get(0)
# except ValueError:
#     assert True
# p.add(Vec3(1, 0, 0), 1.0)
# assert p.t_range() == (0.0, 1.0)
# assert p.get(0.0) == Vec3(0, 0, 0)
# assert p.get(1.0) == Vec3(1, 0, 0)
# p.add(Vec3(1, 0, 1), 2.0)
# assert p.get(2.0) == Vec3(1, 0, 1)

# assert p.get(0.5) == Vec3(0.5, 0, 0)
# assert p.get(0.25) == Vec3(0.25, 0, 0)
# assert p.get(1.5) == Vec3(1, 0, 0.5)
# assert p.t_range() == (0.0, 2.0)

# p.add(Vec3(0, 1, 0), 0.5)
# assert p.get(0.5) == Vec3(0, 1, 0)
# assert p.get(0.25) == Vec3(0, 0.5, 0)
# assert p.get(0.75) == Vec3(0.5, 0.5, 0)

# p.add(Vec3(1, 0, 1), -2.0)
# assert p.t_range() == (-2.0, 2.0)
# assert p.get(-2) == Vec3(1, 0, 1)
