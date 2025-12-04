f = open("input.txt")
instructions = f.read().splitlines()

indices = [
    (row, col)
    for row in (-1, 0, 1)
    for col in (-1, 0, 1)
    if not (row == 0 and col == 0)
]

matrix = [list(ins) for ins in instructions]

at_sign = "@"
partOne = True
ans1 = 0
ans2 = 0
old_ans = 1

while ans2 != old_ans or ans1 > ans2:
    old_ans= ans2
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if col == at_sign:
                count = 0
                for r, c in indices:
                    if  len(matrix) > r + row_index >= 0  and len(row) > c + col_index >= 0 and matrix[row_index+r][col_index+c] == at_sign:
                        count += 1
                        if count > 3:
                            break
                            
                if count <= 3:
                    if partOne:
                        ans1+=1
                    else:
                        matrix[row_index][col_index] = "."
                        ans2 +=1
    partOne = False
            
print("Part 1 Answer:", ans1)
print("Part 2 Answer:", ans2)