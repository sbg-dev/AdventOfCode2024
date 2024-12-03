from typing import List
import re

# Part 1 = 167090022
data: List = []
regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

with open("day3_input.md", "r", encoding="utf-8") as f:
    for line in f:
        data.append(line.strip())

instructions: List = []
instructions = [regex.findall(i) for i in data]

total: int = 0
for line in instructions:
    for factor1, factor2 in line:
        total += int(factor1) * int(factor2)
print(total)
