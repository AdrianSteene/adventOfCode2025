import math

f = open("input.txt")
instructions = f.read().splitlines()

all_points = []
all_grids = []
all_extra = []

for ins in instructions:
    
    split1 = ins.split("]")
    grid = split1[0][1:]
    
    points = [points.strip()[1:].split(",") for points in split1[1].split(")")]
    
    extra = points[len(points)-1:][0]
    extra[len(extra)- 1] = extra[len(extra)- 1][:len(extra[len(extra)- 1])-1]
    points = points[:len(points)-1]
    
    all_points.append(points)
    all_grids.append(grid)
    all_extra.append(extra)
    

def find_least_nbr(current_grid, goal_grid, points, nbr_points, lowest):
    if nbr_points > lowest:
        return lowest

    nbr_points +=1
    for point in points:
        temp_points = points.copy()
        temp_points.remove(point)
        temp_grid = current_grid.copy()
        point = list(map(int, point))
        for i in range(len(temp_grid)):

            if i in point:
                for p in point:
                    if temp_grid[p] == ".":
                        temp_grid[p] = "#"
                    else:
                        temp_grid[p] = "."
                break
        

        if temp_grid == goal_grid:

            return nbr_points
        elif len(temp_points) == 0:
            return math.inf
        
        lowest = min(find_least_nbr(temp_grid, goal_grid, temp_points, nbr_points, lowest), lowest)
    return lowest

res = 0
    
for i in range(len(all_grids)):
    print(i/len(all_grids) *100)
    grid = all_grids[i]
    start_point = ["." for x in range(len(grid))]

    points = {tuple(p) for p in all_points[i]}

    res += find_least_nbr(start_point, list(grid), points, 0, math.inf)


print(res)
            
        
    