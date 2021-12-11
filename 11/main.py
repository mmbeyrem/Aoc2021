def to_ints(l: str):
    for c in l:
        yield int(c)


def inc_neighbors(position, octopusList):
    re_flush = False
    li, ci = position
    neighbors = [(li - 1, ci - 1), (li - 1, ci), (li - 1, ci + 1),
                 (li, ci - 1), (li, ci + 1),
                 (li + 1, ci - 1), (li + 1, ci), (li + 1, ci + 1)]
    for neighbor in neighbors:
        pl, pc = neighbor
        if 0 <= pl < len(octopusList) and 0 <= pc < len(octopusList[0]):
            octopusList[pl][pc] += 1
            re_flush = re_flush or octopusList[pl][pc] > 9
    return re_flush


def flush(octopusList, memo):
    for li, l in enumerate(octopusList):
        for ci, c in enumerate(l):
            if c > 9 and (li, ci) not in memo:
                need_flush = inc_neighbors((li, ci), octopusList)
                memo[(li, ci)] = True
                if need_flush:
                    flush(octopusList, memo)


def set_to_zero(octopusList):
    for li, l in enumerate(octopusList):
        octopusList[li] = list(map(lambda v: 0 if v > 9 else v, l))


def step(octopusList):
    inc(octopusList)
    memo = dict()
    flush(octopusList, memo)
    set_to_zero(octopusList)
    return len(memo)


def inc(octopusList):
    for i, l in enumerate(octopusList):
        octopusList[i] = list(map(lambda v: v + 1, l))


if __name__ == '__main__':
    with open("octopus.txt") as f:
        octopusList = list(map(lambda l: list(to_ints(l)), map(lambda l: l.strip(), f.readlines())))
    i = 0
    while True:
        print(f'step {i + 1}:')
        nb_flush = step(octopusList)
        i += 1
        if nb_flush == (len(octopusList) * len(octopusList[0])):
            print(i)
            break
