from collections import defaultdict


def build_paths(caves):
    paths = defaultdict(set)
    for c in caves:
        head, tail = c.split('-')
        paths[head].add(tail)
        for t in tail:
            if t != "end" and t != head:
                paths[tail].add(head)
    return paths


def find_path(paths, previous_path, found_paths: set):
    prev = previous_path[len(previous_path) - 1]
    for p in paths[prev]:
        if p != 'end' and p != 'start':
            if p.isupper() or (previous_path.count(p) == 0 or all(
                    map(lambda x: previous_path.count(x) < 2,
                        filter(lambda v: v.islower(), previous_path)))):
                find_path(paths, [*previous_path, p], found_paths)
        if p == "end":
            found_paths.add(",".join([*previous_path, p]))


if __name__ == '__main__':
    with open("caves.txt") as f:
        caves = list(map(lambda l: l.strip(), f.readlines()))
    paths = build_paths(caves)
    print(paths)
    found_paths = set()
    find_path(paths, ["start"], found_paths)
    print(len(found_paths))
