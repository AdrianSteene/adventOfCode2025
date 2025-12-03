import numpy as np

f = open("input.txt")
instructions = f.read().splitlines()

ans1 = 0
ans2 = 0
for ins in instructions:
    nums = list(map(int, ins))
    # part 1
    index = np.argmax(nums[:len(nums)-1])
    second = max(nums[index+1:])
    ans1 += int(str(nums[index]) + str(second))
    
    # part 2
    index = 0
    res = []
    choose = nums[:len(nums)-12+len(res)]
    while len(res) != 12:
        choose.append(nums[len(nums)-12+len(res)])
        index = np.argmax(choose)
        res.append(choose[index])
        choose = choose[index+1:]
    
    ans2 += int("".join(map(str, res)))

print("Part 1 Answer:", ans1)
print("Part 2 Answer:", ans2)