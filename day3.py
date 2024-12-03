from typing import List
import re
# Part 1
data: List = []
regex = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
with open("day3_test_input.md", "r", encoding="utf-8") as f:
    for line in f:
        data.append(line.strip())
print(data)
for line in data:
    instructions = regex.findall(line)
print(instructions)
sum: int = 0
for factor1, factor2 in instructions:
    sum += int(factor1) * int(factor2)
print(sum)