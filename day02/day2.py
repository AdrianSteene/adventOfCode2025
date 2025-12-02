f = open("input.txt")
instructions = f.read().split(",")
# instructions = ["11-22"]
# "111" "1212" "123412341234"
ans1 = 0
ans2 = 0
for ins in instructions:
    start, end = ins.split("-")

    for num in range(int(start), int(end)+1, 1):
        num = str(num)
        
        # part 1
        if num[:len(num)//2] == num[len(num)//2:]:
            ans1 += int(num)
        
        # part 2
        if len(num) ==1:
            continue
        if num[0] * len(num) == num:
                ans2 += int(num)
                continue
        
        for n in range(2, len(num)//2+1, 1):
            if num[:len(num)//n] * n  == num:
                ans2 += int(num)
                break
        

print("Part 1 Answer:", ans1)
print("Part 2 Answer:", ans2)