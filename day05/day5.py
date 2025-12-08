f = open("input.txt")
instructions = f.read().splitlines()

nums = []
ans1 = 0
ans2 = 0
for ins in instructions:
    if "-" in ins:
        start = int(ins.split("-")[0])
        end = int(ins.split("-")[1])
        nums.append([start, end])
    else:
        if ins != "":
            for num in nums:
                if num[1] >= int(ins) >=num[0]:
                    ans1+=1
                    break
            
print("Part 1 Answer:", ans1)

nums = sorted(nums)
last_seen = 0
for i, num in enumerate(nums):
    if last_seen > num[0] and last_seen > num[1]:
        continue
    elif last_seen >= num[0]:
        ans2 += num[1] - last_seen
    else:
        ans2 += num[1] - num[0] + 1
    
    last_seen = max(last_seen, num[1])
        
print("Part 2 Answer:", ans2)

