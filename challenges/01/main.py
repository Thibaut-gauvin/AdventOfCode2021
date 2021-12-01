def main():
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


if __name__ == "__main__":
    result = main()
    print(result)
