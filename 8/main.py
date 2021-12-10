def decode9(patterns, decoded):
    nine_chars = set()
    for c in decoded[4]:
        nine_chars.add(c)
    for c in decoded[7]:
        nine_chars.add(c)
    for p in patterns:
        if len(p) != len(nine_chars) + 1:
            continue
        is_nine = True
        for c in nine_chars:
            if c not in p:
                is_nine = False
        if is_nine and p not in decoded.values():
            decoded[9] = p
            break


def decode5(patterns, decoded):
    nine_chars = set()
    for c in decoded[9]:
        nine_chars.add(c)

    for p in patterns:
        five_plus_one_chars = set()
        for c in decoded[1]:
            five_plus_one_chars.add(c)
        for c in p:
            five_plus_one_chars.add(c)
        if five_plus_one_chars == nine_chars and p not in decoded.values():
            decoded[5] = p
            break


def decode6(patterns, decoded):
    eight_chars = set()
    for c in decoded[8]:
        eight_chars.add(c)

    for p in patterns:
        six_plus_one_chars = set()
        for c in decoded[1]:
            six_plus_one_chars.add(c)
        for c in p:
            six_plus_one_chars.add(c)
        if six_plus_one_chars == eight_chars and p not in decoded.values():
            decoded[6] = p
            break


def decode0(patterns, decoded):
    eight_chars = set()
    for c in decoded[8]:
        eight_chars.add(c)

    for p in patterns:
        three_plus_zero = set()
        for c in decoded[3]:
            three_plus_zero.add(c)
        for c in p:
            three_plus_zero.add(c)
        if three_plus_zero == eight_chars and p not in decoded.values():
            decoded[0] = p
            break


def decode3(patterns, decoded):
    nine_chars = set()
    for c in decoded[9]:
        nine_chars.add(c)

    for p in patterns:
        three_plus_four = set()
        for c in decoded[4]:
            three_plus_four.add(c)
        for c in p:
            three_plus_four.add(c)
        if three_plus_four == nine_chars and p not in decoded.values():
            decoded[3] = p
            break


def same_chars(k, output):
    set1 = set()
    for c in k:
        set1.add(c)
    set2 = set()
    for c in output:
        set2.add(c)
    return set1 == set2


class Signal:
    easy_digits = {2: 1, 4: 4, 3: 7, 7: 8}

    def __init__(self, patterns, output_value):
        self.patterns = patterns.strip().split(' ')
        self.output_value = output_value.strip().split(' ')

    def get_easy_digits(self):
        c = 0
        for segment in self.output_value:
            if len(segment) in self.easy_digits.keys():
                c += 1
        return c

    def __str__(self):
        return f'{self.output_value}'

    def decode_output(self):
        decoded = {}
        self.decode_easy_digits(decoded)
        decode9(self.patterns, decoded)
        decode5(self.patterns, decoded)
        decode6(self.patterns, decoded)
        decode3(self.patterns, decoded)
        decode0(self.patterns, decoded)
        for p in self.patterns:
            if p not in decoded.values():
                decoded[2] = p
        print(decoded)
        tmp = ''
        for output in self.output_value:
            for k, v in decoded.items():
                if same_chars(v, output):
                    tmp += str(k)
        print(tmp)
        return int(tmp)

    def decode_easy_digits(self, decoded):
        for p in self.patterns:
            if len(p) in self.easy_digits:
                decoded[self.easy_digits[len(p)]] = p


if __name__ == '__main__':
    with open("signal.txt") as f:
        raw_signals = f.readlines()

    signals = []
    for raw_signal in raw_signals:
        [patterns, output_value] = raw_signal.split('|')
        signals.append(Signal(patterns, output_value))

    count_easy_digits = 0
    for s in signals:
        count_easy_digits += s.get_easy_digits()
    # print(count_easy_digits)

    sum_output = 0
    for s in signals:
        print(f'decode {s}:')
        sum_output += s.decode_output()

    print(f'Total  :{sum_output}')
