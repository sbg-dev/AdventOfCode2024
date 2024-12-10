from typing import List

def main():
    # Part 2 = 689
    data: List[List] = []
    with open("inputs/day2_input.md", "r", encoding="utf-8") as f:
        for line in f:
            data.append(line.strip().split())

    safe_count: int = 0

    def is_safe(report: List[int]) -> bool:
        """
        Check if a report is safe according to the original rules.
        """
        decreasing = all(0 < report[i] - report[i + 1] <= 3 for i in range(len(report)-1))
        increasing = all(-3 <= report[i] - report[i + 1] < 0 for i in range(len(report)-1))

        return increasing or decreasing

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

    return safe_count

if __name__ == "__main__":
    main()