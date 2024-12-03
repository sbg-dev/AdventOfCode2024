from typing import List
import re

# Part 1 = 167090022
data: List = []
instructions: List = []

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

with open("day3_input.md", "r", encoding="utf-8") as f:
    for line in f:
        instructions.append(re.findall(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", line))

print(len(instructions))
total: int = 0
enabled: bool = True
for line in instructions:
    for instr in line:
        if re.match(do_pattern, instr[0]):  # Match `do()`
            enabled = True
        elif re.match(dont_pattern, instr[1]):  # Match `don't()`
            enabled = False
        elif instr[2] and instr[3]: # Match `mul(...)`
            if enabled:
                x, y = int(instr[2]), int(instr[3])
                total += x * y

print(total)
