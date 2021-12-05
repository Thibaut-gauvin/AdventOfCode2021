from typing import List


def part1():
    gamma_rate = ""
    epsilon_rate = ""

    for i in range(0, 12):
        zero_count = 0
        one_count = 0
        with open('input.txt', 'r') as file:
            for line in file:
                current = line.strip()
                if int(current[i]) == 0:
                    zero_count += 1
                else:
                    one_count += 1
            if one_count > zero_count:
                gamma_rate = "%s%s" % (gamma_rate, "1")
                epsilon_rate = "%s%s" % (epsilon_rate, "0")
            else:
                gamma_rate = "%s%s" % (gamma_rate, "0")
                epsilon_rate = "%s%s" % (epsilon_rate, "1")

    print(gamma_rate)
    print(epsilon_rate)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def get_o2(binary_len: int, inputs: List) -> int:
    for pos in range(binary_len):
        current = list(map(lambda x: x[pos], inputs))
        zero_count = current.count("0")
        one_count = current.count("1")

        if one_count > zero_count or one_count == zero_count:
            inputs = list(filter(lambda x: x[pos] == "1", inputs))
        elif one_count < zero_count:
            inputs = list(filter(lambda x: x[pos] == "0", inputs))
        if len(inputs) == 1:
            return int(inputs[0], 2)


def get_co2(binary_len: int, inputs: List) -> int:
    for pos in range(binary_len):
        current = list(map(lambda x: x[pos], inputs))
        zero_count = current.count("0")
        one_count = current.count("1")

        if one_count > zero_count or one_count == zero_count:
            inputs = list(filter(lambda x: x[pos] == "0", inputs))
        elif one_count < zero_count:
            inputs = list(filter(lambda x: x[pos] == "1", inputs))
        if len(inputs) == 1:
            return int(inputs[0], 2)


def part2():
    inputs = []
    with open('input.txt', 'r') as file:
        for line in file:
            binary_len = len(line.strip())
            inputs.append(line.strip())

    o2 = get_o2(binary_len, inputs)
    co2 = get_co2(binary_len, inputs)
    return o2 * co2


if __name__ == "__main__":
    result = part2()
    print(result)
