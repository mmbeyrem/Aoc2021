from more_itertools import first


def make_matrix(w, h):
    matrix = [['.' for _ in range(w)] for _ in range(h)]
    return matrix


def set_points(matrix, points):
    for p in points:
        x, y = map(lambda v: int(v), p)
        matrix[y][x] = '#'


def fold_x(matrix, at):
    for l in matrix:
        if all(map(lambda c: c == '-', l)):
            break
        l[at] = '-'
        for i in range(1, at + 1):
            l[at - i] = "#" if l[at - i] == "#" or l[at + i] == "#" else '.'


def fold_y(matrix, at):
    for ci, _ in enumerate(matrix[at]):
        matrix[at][ci] = '-'
    for i in range(1, at + 1):
        for ci, c in enumerate(matrix[at - i]):
            matrix[at - i][ci] = "#" if c == "#" or matrix[at + i][ci] == '#' else '.'


def count_dots(matrix):
    count = 0
    for l in matrix:
        if all(map(lambda c: c == '-', l)):
            break
        for c in l:
            if c == '-':
                break
            count += 1 if c == '#' else 0
    return count


if __name__ == '__main__':
    with open("instructions.txt") as f:
        instructions = list(map(lambda l: l.strip(), f.readlines()))
    end_of_points = instructions.index('')
    points = list(map(lambda l: l.split(','), instructions[:end_of_points]))
    print(points)
    max_x = 1 + max(map(lambda p: int(p[0]), points))
    max_y = 1 + max(map(lambda p: int(p[1]), points))
    matrix = make_matrix(max_x, max_y)
    set_points(matrix, points)
    # print(matrix)
    fold_instructions = instructions[(end_of_points + 1):]
    # print(fold_instructions)
    fold_instructions = list(map(lambda l: tuple(first(l.split(" ")[-1:]).split("=")), fold_instructions))
    for ins in fold_instructions:
        axe, at = ins
        print(f"fold{ins}")
        if axe == "y":
            fold_y(matrix, int(at))
        elif axe == "x":
            fold_x(matrix, int(at))
    for l in matrix:
        if all(map(lambda c: c == '-', l)):
            break
        print(l)
    print(count_dots(matrix))
