
f = open("input.txt")
instructions = f.read().splitlines()

keys = [line.split(":")[0] for line in instructions]
values = [line.split(":")[1].strip().split(" ") for line in instructions]

paths = {}

for index in range(len(keys)):
    paths[keys[index]] = values[index]

start_node = "you" 

queue = [start_node]
ans1 = 0

while len(queue) > 0:
    node = queue.pop()
    for out_node in paths[node]:
        if out_node == "out":
            ans1+=1
        else:
            queue.append(out_node)


print("Part 1 Answer:", ans1)


cache = {}

def visit(node, visited):
    
    if node == "out":
        if "dac" in visited and "fft" in visited:
            return 1
        return 0
    
    key = (node, "dac" in visited, "fft" in visited)
    
    if key in cache.keys():
        return cache[key]
        
    
    ans = 0
    for out_node in paths[node]:
        
        temp_visited = visited.copy()
        temp_visited.add(out_node)
        ans += visit(out_node, temp_visited)

    cache[key] = ans
    
    return ans
    
print("Part 2 Answer:", visit("svr", set()))