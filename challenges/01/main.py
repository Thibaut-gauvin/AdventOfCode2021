def part1():
    counter = 0
    previous_value = None

    with open('input.txt', 'r') as file:
        for line in file:
            current = int(line.strip())
            if previous_value is None:
                previous_value = current
                continue
            if current > previous_value:
                counter += 1
            previous_value = current

        return counter


def part2():
    counter = 0
    seq = []
    window_size = 3
    previous_value = None

    with open('input.txt', 'r') as file:
        for line in file:
            intval = int(line.strip())
            seq.append(intval)

        for i in range(len(seq) - window_size + 1):
            current = seq[i: i + window_size]
            if previous_value is None:
                previous_value = current
                continue
            if sum(current) > sum(previous_value):
                counter += 1
            previous_value = current

        return counter


if __name__ == "__main__":
    result = part2()
    print(result)
