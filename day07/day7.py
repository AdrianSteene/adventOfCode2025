f = open("input.txt")
instructions = f.read().splitlines()


rows = [0 for x in range(len(instructions))]
# part 1
res = 0
for row_index in range(2, len(instructions)):
    for col_index in range(len(instructions[row_index])):
        
        if instructions[row_index][col_index] == "^":

            for i in range(row_index-1, -1, -1):
                if instructions[i][col_index-1] == "^" or instructions[i][col_index+1] == "^":
                    res += 1
                    rows[row_index] +=1
                    break
                elif instructions[i][col_index] == "^":
                    break

print("Part 1 Answer:", res)

def find_nbr_paths(row, col, dic):

    res = 0
    while True:
        if row == len(instructions):
            return 1
        elif (row, col) in dic.keys():
            res += dic[(row, col)]
            break
        elif instructions[row][col] == "^":
            r1 = find_nbr_paths(row+1, col-1, dic)
            r2 = find_nbr_paths(row+1, col+1, dic)
            dic[(row+1, col-1)] = r1
            dic[(row+1, col+1)] = r2
            res += r1
            res += r2
            break
        row += 1

    return res

print("Part 2 Answer:", find_nbr_paths(0, instructions[0].index("S"), {}))