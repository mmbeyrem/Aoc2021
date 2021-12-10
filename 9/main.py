import math


def build_hight_matrix():
    heightmap_matrix = []
    for r in heightmap:
        l = list()
        for i in r:
            l.append(int(i))
        heightmap_matrix.append(l)
    return heightmap_matrix


def get_basin(position, matrix, visited={}):
    if position not in visited:
        x, y = position
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] == 9:
            return 0
        visited[position] = True
        return 1 + get_basin((x - 1, y), matrix) + get_basin((x, y - 1), matrix) + \
               get_basin((x + 1, y), matrix) + get_basin((x, y + 1), matrix)
    return 0


def get_low_points(matrix):
    lows = []
    basins = []
    for ri, r in enumerate(matrix):
        for li, v in enumerate(r):
            prev = r[li - 1] if (li - 1) >= 0 else math.inf
            next = r[li + 1] if (li + 1) < len(r) else math.inf
            upper = matrix[ri - 1][li] if (ri - 1) >= 0 else math.inf
            lower = matrix[ri + 1][li] if (ri + 1) < len(matrix) else math.inf
            if v < prev and v < next and v < upper and v < lower:
                lows.append(v)
                basins.append(get_basin((ri, li), matrix))
    return lows, basins


if __name__ == '__main__':
    with open("heightmap.txt") as f:
        heightmap = list(map(lambda l: l.strip(), f.readlines()))
    matrix = build_hight_matrix()
    points, basins = get_low_points(matrix)
    risks = list(map(lambda v: v + 1, points))
    print(sum(risks))
    basins.sort(reverse=True)
    print(basins)
    print(basins[:3])
    multi = 1
    for v in basins[:3]:
        multi *=v
    print(multi)
