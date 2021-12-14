import math
from collections import defaultdict


def insert(polymer_template, rules):
    new_polymer = ""
    for i, c in enumerate(polymer_template[:-1]):
        pair = polymer_template[i:i + 2]
        tmp = rules[pair] if pair in rules else ""
        new_polymer += f'{c}{tmp}'
    return f'{new_polymer}{polymer_template[-1:]}'


def parse_rules(rules):
    rules_dict = {}
    for rule in map(lambda r: r.split('->'), rules):
        rules_dict[rule[0].strip()] = rule[1].strip()
    print(rules_dict)
    return rules_dict


def count_occ(polymer):
    counter = defaultdict(int)
    for c in polymer:
        counter[c] += 1
    return counter


def sylab_parse(polymer_template):
    dic = defaultdict(int)
    for i in range(len(polymer_template) - 1):
        dic[polymer_template[i: i + 2]] += 1
    return dic


def inc_sylab(syllables, rules):
    new_dict = defaultdict(int)
    for s in syllables:
        if s in rules:
            new_dict[f'{s[0]}{rules[s]}'] += syllables[s]
            new_dict[f'{rules[s]}{s[1]}'] += syllables[s]
        else:
            new_dict[s] += syllables[s]

    return new_dict


def phase_2(polymer_template, rules):
    syllables = sylab_parse(polymer_template)
    for _ in range(0, 40):
        syllables = inc_sylab(syllables, rules)

    chars_counter = defaultdict(int)
    for s in syllables:
        chars_counter[s[1]] += syllables[s]
    min_max(chars_counter)


def min_max(counter):
    max_occ = ('', -1)
    min_occ = ('', math.inf)
    for c in counter.items():
        key, v = c
        if v > max_occ[1]:
            max_occ = c
        if v < min_occ[1]:
            min_occ = c
    print(max_occ)
    print(min_occ)
    print(max_occ[1] - min_occ[1])


if __name__ == '__main__':
    with open("pair_insertion_rules.txt") as f:
        polymer_template = f.readline().strip()
        f.readline()
        rules = list(map(lambda l: l.strip(), f.readlines()))
    rules = parse_rules(rules)
    tmp = polymer_template
    for _ in range(0, 10):
        tmp = insert(tmp, rules)
    counter = count_occ(tmp)
    min_max(counter)
    phase_2(polymer_template, rules)
