# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import defaultdict
from copy import deepcopy


def binary_diagnostic():
    with open("diagnostic_report.txt") as f:
        diag_report = f.readlines()
    agg = defaultdict(int)
    for l in diag_report:
        for i, d in enumerate(l[:-1]):
            agg[i] += int(d)
    gamma_rate = ""
    epsilon_rate = ""
    for v in agg.values():
        if v > len(diag_report) // 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    epsilon_rate = int(epsilon_rate, 2)
    gamma_rate = int(gamma_rate, 2)
    print(gamma_rate * epsilon_rate)


def compute_1(report):
    tmp = report
    for i in range(0, len(report[0]) - 1):
        l = []
        commun_value = get_commun_for_oxy(tmp, i)
        for r in tmp:
            if r[i] == commun_value:
                l.append(r)
        if len(l) == 1:
            print(f'found:{int(l[0], 2)}')
            break
        tmp = deepcopy(l)


def compute_2(report):
    tmp = report
    for i in range(0, len(report[0]) - 1):
        l = []
        commun_value = get_commun_for_2(tmp, i)
        for r in tmp:
            if r[i] != commun_value:
                l.append(r)
        if len(l) == 1:
            print(f'found:{int(l[0], 2)}')
            break
        tmp = deepcopy(l)
        # print(tmp)

def life_support_rating():
    with open("diagnostic_report.txt") as f:
        diag_report = f.readlines()
    compute_1(deepcopy(diag_report))
    compute_2(deepcopy(diag_report))


def get_commun_for_oxy(diag_report, at):
    agg = 0

    for l in diag_report:
        agg += int(l[at])
    if agg >= len(diag_report) / 2:
        return "1"
    else:
        return "0"


def get_commun_for_2(diag_report, at):
    agg = 0

    for l in diag_report:
        agg += int(l[at])
    if agg >= len(diag_report) / 2:
        return "1"
    else:
        return "0"


if __name__ == '__main__':
    # binary_diagnostic()
    life_support_rating()
