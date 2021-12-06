# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def phase1():
    with open("plan.txt") as f:
        operations = f.readlines()
    forward = 0
    x_axe = 0
    for op in operations:
        direction, x = op.split(' ')
        if direction == "forward":
            forward += int(x)
        if direction == "up":
            x_axe -= int(x)
        if direction == "down":
            x_axe += int(x)
    print(f"{forward}:{x_axe}=> {forward * x_axe}")


def phase2():
    with open("plan.txt") as f:
        operations = f.readlines()
    h_position = 0
    aim = 0
    depth = 0
    for op in operations:
        direction, x = op.split(' ')
        if direction == "forward":
            h_position += int(x)
            depth += (aim * int(x))
        if direction == "up":
            aim -= int(x)
        if direction == "down":
            aim += int(x)
    print(f"{h_position}:{aim}=> {h_position * depth}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    phase2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
