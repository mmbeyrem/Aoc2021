def get_distance(p1, p2, memo={}):
    to = abs(p1 - p2)
    sum_d = 0
    if to not in memo:
        for i in range(0, to+1):
            sum_d += i
        memo[to] = sum_d

    return memo[to]


def get_closed_position(crabs_postion, memo={}):
    min_d = 9999999999
    closed_p = -1
    for p in range(0, max(crabs_postion)):
        sum_d = 0
        if p not in memo:
            for i in crabs_postion:
                if p == i:
                    continue
                sum_d += get_distance(p, i)
            memo[p] = sum_d
        if memo[p] < min_d:
            min_d = sum_d
            closed_p = p
    return min_d, closed_p


if __name__ == '__main__':
    with open("crab_position.txt") as f:
        crabs = list(map(lambda v: int(v), f.readline().split(',')))
    print(crabs)
    distance, position = get_closed_position(crabs)
    print(f'{distance}, {position}')
