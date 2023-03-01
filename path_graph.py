import vec3


class Path:
    def __init__(self):
        self.points = []  # a list of tuples (time, point)

    def add(self, pt, t):
        # append the new point with its time to the list
        self.points.append((t, pt))

    def get(self, t):
        if not self.points:
            raise ValueError("There are no points in the path.")
        elif len(self.points) == 1:
            return self.points[0][1]  # return the only point in the list
        elif t < self.points[0][0]:
            return self.points[0][1]  # return the point with smallest t
        elif t > self.points[-1][0]:
            return self.points[-1][1]  # return the point with largest t
        else:
            # Find the first time in the list greater than t, t2 and the corresponding point in space p2
            for i in range(len(self.points) - 1):
                if self.points[i + 1][0] > t:
                    t2, p2 = self.points[i + 1]
                    t1, p1 = self.points[i]
                    # Compute the position p of the drone at time t using linear interpolation
                    a = (t - t1) / (t2 - t1)
                    p = p1 * (1 - a) + p2 * a
                    return p

    def t_range(self):
        if not self.points:
            raise ValueError("There are no points in the path.")
        else:
            times = [pt[0] for pt in self.points]
            return (min(times), max(times))


# B2 ASSERTIONS

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
