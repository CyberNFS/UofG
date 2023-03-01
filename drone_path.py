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

# Displaying the Path –––––––––––––––––––––––––––––- >

drone_path = Path()
# on ground
drone_path.add(Vec3(0, 0, 0), 0)
# up
drone_path.add(Vec3(0, 0, 2), 1)
# forward, up
drone_path.add(Vec3(5, 0, 5), 5)
# left
drone_path.add(Vec3(5, 7, 7), 10)
# backward
drone_path.add(Vec3(-5, 7, 7), 15)
# right
drone_path.add(Vec3(-5, -7, 5), 20)
# forward
drone_path.add(Vec3(5, -7, 5), 25)
# left
drone_path.add(Vec3(5, 0, 5), 30)
# home
drone_path.add(Vec3(0, 0, 0), 35)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use("TkAgg")


# show the drone path
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# sample a path at regular points
def sample_path(path, ts):
    return np.array([path.get(t).as_list() for t in ts])


# plot the drone path
times = np.linspace(-10, 60, 500)
label_times = times[180:-180:20]
np_path = sample_path(drone_path, times)
ax.scatter(np_path[:, 0], np_path[:, 1],
           np_path[:, 2], cmap='viridis', c=times)
ax.text(0, 0, 0, "Launch point")

# show some time labels on the path
for t in label_times:
    # we can sample at *any* time, which makes this easy to write
    drone_pt = drone_path.get(t)
    ax.text(drone_pt.x, drone_pt.y, drone_pt.z, f"{t:.1f}s")
