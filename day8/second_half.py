
with open("input.txt", mode="r") as f:
    forest = [[int(c) for c in l if c != "\n"] for l in f.readlines()]
    outside_tree = (len(forest)-1) * 4
    inside_tree = 0
    score = []
    for i, f in enumerate(forest[1:-1], start=1):
        for j, t in enumerate(f[1:-1], start=1):
            left = 0
            for k in range(j-1, -1, -1): # left
                if t > forest[i][k]: left += 1
                else: 
                    left += 1
                    break

            right = 0
            for k in range(j+1, len(forest[0])): # right
                if t > forest[i][k]: right += 1
                else: 
                    right += 1
                    break
        
            up = 0
            for k in range(i-1, -1, -1): # top
                if t > forest[k][j]: up += 1
                else: 
                    up += 1
                    break
        
            down = 0
            for k in range(i+1, len(forest)): # down
                if t > forest[k][j]: down += 1
                else: 
                    down += 1
                    break
            score.append(left*right*up*down)
    print(max(score))
