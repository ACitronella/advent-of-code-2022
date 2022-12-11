head_position = [0, 0]
last_head_position = [0, 0]
tail_position = [0, 0]
last_tail_positions = set()
with open("input.txt", mode="r") as f:
    for l in f.readlines():
        direction, step = l.split()
        step = int(step)
        for _ in range(step):
            last_head_position = head_position.copy()
            # hope for branch optimization
            if direction == "R":
                head_position[0] += 1
            elif direction == "L":
                head_position[0] -= 1
            elif direction == "U":
                head_position[1] += 1
            elif direction == "D":
                head_position[1] -= 1
            if ((tail_position[0] - head_position[0]) ** 2 + (tail_position[1] - head_position[1]) ** 2)**0.5 > 1.42: # more than sqrt(2), nine blocks around
                tail_position = last_head_position
            last_tail_positions.add(tuple(tail_position))
            
    print(len(last_tail_positions))
