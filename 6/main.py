from collections import defaultdict


def print_hi(lanterns, nb_days):
    for i in range(0, nb_days):
        nb_news = 0
        for li, lantern in enumerate(lanterns):
            if lantern == 0:
                lanterns[li] = 6
                nb_news += 1
            else:
                lanterns[li] -= 1
        for n in range(0, nb_news):
            lanterns.append(8)

    # print(lanterns)
    print(len(lanterns))


cache_babies_count = defaultdict(int)


def get_babies(day_to):
    count = day_to // 7
    count +=get_babies()
    print(f'day to :{day_to}=>{count}')
    return count


if __name__ == '__main__':
    with open("lanternfish_ages.txt") as f:
        raw_lanterns = f.readline()
    fishes = list(map(lambda v: int(v), raw_lanterns.split(',')))
    days = [0] * 9
    # Update the current numbers
    for fish in fishes:
        days[fish] += 1
    for i in range(256):
        # To make it cyclic: 0, 1, 2, 3, 4, 5, 6, 7, 8
        today = i % len(days)
        # Add new babies
        days[(today + 7) % len(days)] += days[today]
    print(f'Total lanternfish after 256 days: {sum(days)}')