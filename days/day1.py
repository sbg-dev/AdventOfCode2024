
def main():
    # Part1 = 1580061
    list1 = []
    list2 = []

    with open("inputs/day1_input.md", "r", encoding="utf-8") as file:
        for line in file:
            left, right = line.strip().split("   ")
            list1.append(int(left))
            list2.append(int(right))

    list1.sort()
    list2.sort()

    distance = sum([abs((x)- (y)) for x, y in zip(list1, list2)])

    # Part2 = 23046913

    doublicates = [x for x in list1 for y in list2 if x == y]
    from collections import Counter
    result = sum([x[0] * x[1] for x in Counter(doublicates).items()])

    return {"distance": distance, "result": result}

if __name__ == "__main__":
    main()
