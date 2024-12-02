from typing import List

# Part 1 = 660
data: List[List] = []
with open("day2_input.md", "r", encoding="utf-8") as f:
    for line in f:
        data.append(line.strip().split())

save_count: int = 0
for report in data:
    print(f"New run: {report}")
    save: bool = True
    increasing, decreasing = 0, 0
    for i in range(len(report)-1):
        level1 = int(report[i])
        level2 = int(report[i+1])
        difference = level1 - level2
        if 0 < difference <= 3:
            decreasing += 1
        elif -3 <= difference < 0:
            increasing += 1
        else:
            save = False
    if decreasing != 0 and increasing != 0:
        save = False
    if save == True:
        save_count += 1
print(save_count)