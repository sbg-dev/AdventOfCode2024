from typing import List


def parse_input_data(rules: dict, orders: List):
    with open("inputs/day5_test_input.md", "r", encoding="utf-8") as file:
        for line in file:
            if line == '\n':
                continue
            try:
                left, right = line.strip().split("|")
                left, right = int(left), int(right)
                if left not in rules:
                    rules[left] = []
                rules[left].append(right)
            except ValueError:
                orders.append([int(x) for x in line.strip().split(",")])


def main():
    rules: dict = {}
    orders: List = []
    parse_input_data(rules, orders)


if __name__ == "__main__":
    main()
