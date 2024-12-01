
list1 = []
list2 = []

with open("day1_input.md", "r", encoding="utf-8") as file:
    for line in file:
        left, right = line.strip().split("   ")
        list1.append(left)
        list2.append(right)

list1.sort()
list2.sort()

distance = [abs(int(x) - int(y)) for x, y in zip(list1, list2)]
print(sum(distance))
