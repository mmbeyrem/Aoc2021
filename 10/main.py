from collections import deque

from more_itertools import first

symbols = {'{': '}', '[': ']', '<': '>', '(': ')'}


def is_openning(c):
    return c in symbols.keys()


def is_closing(c):
    return c in symbols.values()


def is_corrupted(line):
    q = deque()
    for c in line.strip():
        if is_openning(c):
            q.append(c)
        if is_closing(c):
            open_symbol = q.pop()
            if (open_symbol, c) not in symbols.items():
                return c
    return None


def complete(line) -> list:
    q = deque()
    end_sequence = []
    for c in line.strip():
        if is_openning(c):
            q.append(c)
        if is_closing(c):
            q.pop()
    while q:
        c = q.pop()
        end_c = symbols[first(filter(lambda s: s[0] == c, symbols))]
        end_sequence.append(end_c)
    return end_sequence


def score(v, weights) -> int:
    weight_sum = 0
    for i in v:
        weight_sum *= 5
        weight_sum += weights[i]
    return weight_sum


if __name__ == '__main__':
    with open("navigation.txt") as f:
        navigation_lines = f.readlines()

    symbols_weight = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}
    print(sum(map(lambda v: symbols_weight[v], map(lambda l: is_corrupted(l),
                                                   navigation_lines))))
    completion_symbols_weight = {')': 1, ']': 2, '}': 3, '>': 4, None: 0}
    completion_scores = list(map(lambda v: score(v, completion_symbols_weight),
                                 map(lambda v: complete(v), filter(lambda l: not is_corrupted(l),
                                                                   navigation_lines))))
    completion_scores.sort()
    middle_pos = len(completion_scores) // 2
    print(completion_scores[middle_pos])
