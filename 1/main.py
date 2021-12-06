# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def depth_measurement():
    prev = -1
    inc_counter = -1
    with open('depth.txt') as f:
        lines = f.readlines()
    for l in lines:
        depth = int(l)
        if depth > prev:
            inc_counter += 1
        prev = depth
    print(inc_counter)


def depth_3_measurement():
    inc_counter = -1
    old_messure = -1
    with open('depth.txt') as f:
        lines = f.readlines()
    for i, _ in enumerate(lines[:-2]):
        new_ressure = int(lines[i + 1]) + int(lines[i + 2]) + int(lines[i])
        if new_ressure > old_messure:
            inc_counter += 1
        old_messure = new_ressure
    print(inc_counter)


if __name__ == '__main__':
    depth_measurement()
    depth_3_measurement()
