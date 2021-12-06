import re
from collections import defaultdict


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class segment:
    def __init__(self, p1, p2):
        self.point_1 = p1
        self.point_2 = p2


def build_grid(segments, max_val):
    grid = defaultdict(list)
    for i in range(0, max_val + 1):
        grid[i] = [0] * (max_val + 1)
    for s in segments:
        if s.point_1.x == s.point_2.x:
            min_val = min(s.point_1.y, s.point_2.y)
            max_val = max(s.point_1.y, s.point_2.y)
            for v in range(min_val, max_val + 1):
                grid[v][s.point_1.x] += 1
        elif s.point_1.y == s.point_2.y:
            min_val = min(s.point_1.x, s.point_2.x)
            max_val = max(s.point_1.x, s.point_2.x)
            for v in range(min_val, max_val + 1):
                grid[s.point_1.y][v] += 1
        else:
            distance_x = s.point_1.x - s.point_2.x
            distance_y = s.point_1.y - s.point_2.y
            if abs(distance_x) != abs(distance_y):
                continue
            if distance_x > 0 and distance_y > 0:
                for i in range(0, abs(distance_x) + 1):
                    grid[s.point_2.y + i][s.point_2.x + i] += 1

            if distance_x < 0 and distance_y < 0:
                for i in range(0, abs(distance_x) + 1):
                    grid[s.point_2.y-i][s.point_2.x - i] += 1

            if distance_x < 0 and distance_y > 0:
                for i in range(0, abs(distance_x) + 1):
                    grid[s.point_1.y-i][s.point_1.x + i] += 1
            if distance_x > 0 and distance_y < 0:
                for i in range(0, abs(distance_x) + 1):
                    grid[s.point_1.y+i][s.point_1.x - i] += 1
    return grid


def get_overlap_points(grid):
    count = 0
    for row in grid.values():
        for c in row:
            count += 1 if c > 1 else 0
    return count


def print_hi():
    print("HI")
    with open("vents.txt") as f:
        vents = f.readlines()
    segments, max_val = get_segments(vents)
    grid = build_grid(segments, max_val)
    print(grid)
    nb_points = get_overlap_points(grid)
    print(nb_points)


def get_segments(vents):
    segments = []
    max_val = 0
    for raw_seg in vents:
        x = re.search("(\d+),(\d+) -> (\d+),(\d+)", raw_seg)
        [x1, y1, x2, y2] = list(x.groups())
        segments.append(segment(point(int(x1), int(y1)), point(int(x2), int(y2))))
        max_val = max(max_val, int(x1), int(y1), int(x2), int(y2))
    return segments, max_val


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
