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


def part2():
    oxygen_generator_rating = 0
    co2_scrubber_rate = 0


if __name__ == "__main__":
    result = part1()
    print(result)
