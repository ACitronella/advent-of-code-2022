
with open("input.txt", mode="r") as f:
    forest = [[int(c) for c in l if c != "\n"] for l in f.readlines()]
    outside_tree = (len(forest)-1) * 4
    inside_tree = 0
    for i, f in enumerate(forest[1:-1], start=1):
        for j, t in enumerate(f[1:-1], start=1):
            is_visible = 1
            for k in range(j): # left
                if t <= forest[i][k]:
                    is_visible = 0
                    break
            if not is_visible:
                is_visible = 1
                for k in range(j+1, len(forest[0])): # right
                    if t <= forest[i][k]:
                        is_visible = 0
                        break
            if not is_visible:
                is_visible = 1
                for k in range(i): # top
                    if t <= forest[k][j]:
                        is_visible = 0
                        break
            if not is_visible:
                is_visible = 1
                for k in range(i+1, len(forest)): # down
                    if t <= forest[k][j]:
                        is_visible = 0
                        break
            inside_tree += is_visible
    print(inside_tree + outside_tree)
