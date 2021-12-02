def part1():
    coordinates = {"horizon": 0, "deeps": 0}

    with open('input.txt', 'r') as file:
        for line in file:
            stripped = line.strip()
            current = stripped.split()
            action_key = current[0]
            action_value = int(current[1])

            if action_key == "forward":
                coordinates["horizon"] += action_value
            if action_key == "up":
                coordinates["deeps"] -= action_value
            if action_key == "down":
                coordinates["deeps"] += action_value

        print(coordinates)
        return coordinates["horizon"] * coordinates["deeps"]


def part2():
    coordinates = {"horizon": 0, "deeps": 0, "aim": 0}

    with open('input.txt', 'r') as file:
        for line in file:
            stripped = line.strip()
            current = stripped.split()
            action_key = current[0]
            action_value = int(current[1])

            if action_key == "forward":
                coordinates["horizon"] += action_value
                coordinates["deeps"] += coordinates["aim"] * action_value
            if action_key == "up":
                coordinates["aim"] -= action_value
            if action_key == "down":
                coordinates["aim"] += action_value

        print(coordinates)
        return coordinates["horizon"] * coordinates["deeps"]


if __name__ == "__main__":
    result = part2()
    print(result)
