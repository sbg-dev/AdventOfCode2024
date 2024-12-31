from typing import List


def parse_input_data(rules, orders):
    with open("inputs/day5_test_input.md", "r", encoding="utf-8") as file:
        for line in file:
            try:
                left, right = line.strip().split("|")
                rules.append([left, right])
            except ValueError:
                orders.append(line.strip())
    print(rules)
    print(orders)


def main():
    rules: List = []
    orders: List = []
    parse_input_data(rules, orders)


if __name__ == "__main__":
    main()
