from typing import List

# Part 1
data: List[List] = []
with open("day2_test_input.md", "r", encoding="utf-8") as f:
    for line in f:
        data.append(line.strip().split())

save_count: int = 0
for report in data:
    print(f"New run: {report}")
    save: bool = True
    for i in range(len(report)-1):
        level1 = int(report[i])
        level2 = int(report[i+1])
        difference = level1 - level2
        if 1 <= abs(difference) > 3 or difference == 0:
            print("Unsave")
            save = False
            break
    if save == True:
        save_count += 1

print(save_count)