# Part1
list1 = []
list2 = []

with open("day1_input.md", "r", encoding="utf-8") as file:
    for line in file:
        left, right = line.strip().split("   ")
        list1.append(int(left))
        list2.append(int(right))

list1.sort()
list2.sort()

distance = sum([abs((x)- (y)) for x, y in zip(list1, list2)])
print(distance)

# Part2
result = 0

for x in list1:
    i = 0
    for y in list2:
        if x == y:
            i += 1
    print(x, i, x * i)
    result = result + x * i

print(result)
