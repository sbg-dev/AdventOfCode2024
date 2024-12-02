from typing import List

# Part 1 = 660
data: List[List] = []
with open("day2_input.md", "r", encoding="utf-8") as f:
    for line in f:
        data.append(line.strip().split())

safe_count: int = 0

def is_safe(report: List[int]) -> bool:
    """
    Check if a report is safe according to the original rules.
    """
    increasing, decreasing = 0, 0
    for i in range(len(report) - 1):
        level1 = report[i]
        level2 = report[i + 1]
        difference = level1 - level2
        if 0 < difference <= 3:
            decreasing += 1
        elif -3 <= difference < 0:
            increasing += 1
        else:
            return False
    return increasing == 0 or decreasing == 0

def can_be_safe_with_dampener(report: List[int]) -> bool:
    """
    Check if a report can be made safe by removing one level.
    """
    for i in range(len(report)):
        # Create a modified report by removing the i-th level
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False

for report in data:
    report = list(map(int, report))  # Convert report levels to integers
    print(f"New run: {report}")
    if is_safe(report) or can_be_safe_with_dampener(report):
        safe_count += 1

print(safe_count)