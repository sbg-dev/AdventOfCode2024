from typing import List

# Day 4 Part 1 = 2583
# Day 4 Part 2 = 1978
data: List = []
with open("day4_input.md", "r", encoding="utf-8") as f:
    for line in f:
        data.append(line.strip())

coordinates = [(0,1), (0,-1), (-1,0), (1,0), # horizontal and vertical
                (-1,1), (1,1), (1,-1), (-1,-1)] # diagonal clockwise rotation
word = "XMAS"

def search_cross_match(r, c, coordinates, word):

    reverse_word = word[::-1]
    pattern = []
    for dr, dc in coordinates:
        nr = r + dr
        nc = c + dc
        if not (0 <= nc < column_count and 0 <= nr < row_length):
            return False
        pattern.append(data[nr][nc])
    pattern = "".join(pattern)
    return pattern == word or pattern == reverse_word

def search_directions(r, c, dr, dc, word):

    for i, _ in enumerate(word):
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
x_match_count: int = 0

for row in range(row_length):
    for column in range(column_count):
        for dr, dc in coordinates:
            if search_directions(row, column, dr, dc, word):
                count += 1
        if data[row][column] == "A":
                # Check both diagonals
                tr_lr = [(-1,1),(0,0), (1,-1)]
                tl_ll = [(-1,-1), (0,0), (1,1)]
                top_left_to_bottom_right = search_cross_match(row, column, tr_lr, "MAS")
                bottom_left_to_top_right = search_cross_match(row, column, tl_ll, "MAS")
                if top_left_to_bottom_right and bottom_left_to_top_right:
                    x_match_count += 1

print(data[4:7])
print(f"Count: {count}")
print(f"x_match_count: {x_match_count}")
