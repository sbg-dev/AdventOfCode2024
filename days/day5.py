from typing import List


def parse_input_data(rules: dict, orders: List):
    with open("inputs/day5_input.md", "r", encoding="utf-8") as file:
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


def check_order(order: str, instructions: List):

    def find_rule_for_element(element) -> list:
        if element not in instructions:
            return []
        return instructions[element]

    def compare_rule_with_order(instruction, order) -> bool:
        for element in order:
            if element not in instruction:
                return False
        return True

    for i in range(len(order)-1):
        instuction = find_rule_for_element(order[i])
        if not compare_rule_with_order(instuction, order[i+1:]):
            return False
    return True


def main():
    rules: dict = {}
    orders: List = []
    page_sum: int = 0
    parse_input_data(rules, orders)

    for order in orders:
        if check_order(order, rules):
            page_sum += order[len(order) // 2]
    print(page_sum)


if __name__ == "__main__":
    main()
