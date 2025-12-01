f = open("input.txt")
instructions = f.read().splitlines()

res = 0
res1 = 0
dial = 50
for ins in instructions:
    oldDial = dial
    num = int(ins[1:])
    dial += num if ins[0] == "R" else -num
        
    if dial > 99 or dial < 0:
        res1 += abs(dial // 100)
        if dial > 0 and dial % 100 == 0:
            res1 -= 1

        if oldDial == 0 and ins[0] == "L":
            res1 -= 1
            
    dial = dial % 100
    
    if dial == 0:
        res += 1
        
print("Part 1 Answer:", res)
print("Part 2 Answer:", res + res1)
