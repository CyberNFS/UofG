import sys
import math
import tkinter as tk
from tkinter import Canvas


def read_cities(filename):
    """Read city coordinates from a file."""
    with open(filename, 'r') as f:
        cities = []
        max_y = 0
        for line in f:
            x, y, name = line.strip().split()
            x = int(x)
            y = int(y)
            cities.append((x, y, name))
            if y > max_y:
                max_y = y
        # Flip the Y coordinates so that (0,0) is at the bottom left of the canvas.
        for i in range(len(cities)):
            x, y, name = cities[i]
            cities[i] = (x, max_y - y, name)
        return cities


def distance(city1, city2):
    """Compute the Euclidean distance between two cities."""
    x1, y1, _ = city1
    x2, y2, _ = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def nearest_neighbour(cities):
    """Compute a tour of cities using the nearest neighbour algorithm."""
    tour = [cities[0]]  # start at an arbitrary city
    unvisited = set(cities[1:])  # all other cities are unvisited
    while unvisited:
        current_city = tour[-1]
        nearest_city = min(
            unvisited, key=lambda city: distance(current_city, city))
        tour.append(nearest_city)
        unvisited.remove(nearest_city)
    return tour


def draw_tour(cities, tour):
    """Draw a tour of cities on a 2D plane."""
    # Compute the minimum and maximum X and Y coordinates of the cities.
    min_x = min(x for x, _, _ in cities)
    max_x = max(x for x, _, _ in cities)
    min_y = min(y for _, y, _ in cities)
    max_y = max(y for _, y, _ in cities)

    # Compute the scaling factor to fit the cities onto the canvas.
    scale = 500 / max(max_x - min_x, max_y - min_y)

    # Create a new Tkinter window and canvas to draw the cities.
    root = tk.Tk()
    canvas = Canvas(root, width=scale * (max_x - min_x + 10),
                    height=scale * (max_y - min_y + 10))
    canvas.pack()

    # Draw the names of the cities next to their locations.
    for x, y, name in cities:
        canvas.create_text(scale * (x - min_x + 5),
                           scale * (max_y - y + 5), text=name)

    # Draw the tour as a sequence of connected lines on the canvas.
    for city1, city2 in zip(tour, tour[1:] + [tour[0]]):
        x1, y1, _ = city1
        x2, y2, _ = city2
        canvas.create_line(scale * (x1 - min_x + 5), scale * (max_y - y1 + 5),
                           scale * (x2 - min_x + 5), scale * (max_y - y2 + 5))

    root.mainloop()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: No filename provided")
        sys.exit(1)
    try:
        filename = sys.argv[1]
        cities = read_cities(filename)
        tour = nearest_neighbour(cities)
        length = sum(distance(city1, city2)
                     for city1, city2 in zip(tour, tour[1:] + [tour[0]]))
        print(f'Tour length: {int(length)}')
        draw_tour(cities, tour)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
