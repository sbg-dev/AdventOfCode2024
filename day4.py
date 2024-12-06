from typing import List

# Day 4 Part 1 = 2583
data: List = []
with open("day4_test_input.md", "r", encoding="utf-8") as f:
    for line in f:
        data.append(line.strip())

coordinates = [(0,1), (0,-1), (-1,0), (1,0), # horizontal and vertical
                (-1,1), (1,1), (1,-1), (-1,-1)] # diagonal clockwise rotation
word = "XMAS"

def search_directions(r, c, dr, dc, word):
    for i in range(len(word)):
        nr = r + dr * i
        nc = c + dc * i
        if not (0 <= nc < column_count and 0 <= nr < row_length):
            return False
        if data[nr][nc] != word[i]:
            return False
    return True

row_length: int = len(data)
column_count: int = len(data[0])
match: bool = True
count: int = 0

for row in range(row_length):
    print(f"Column: {data[row]}")
    for column in range(column_count):
        for dr, dc in coordinates:
            if search_directions(row, column, dr, dc, word):
                count += 1
print(count)