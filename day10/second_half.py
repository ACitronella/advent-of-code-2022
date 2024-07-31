x = 1
# signal_strength = 0
cycle = 0
crt_screen = ["."] * 240

def endcycle(cycle:int, x:int, crt_screen:list[str]):
    cycle_mod40 = cycle % 40
    if cycle_mod40 >= x-1 and cycle_mod40 <= x+1:
        crt_screen[cycle] = "#"
    cycle += 1
    return cycle, crt_screen


with open("input.txt", mode="r") as f:
    file_contents = f.readlines()

    for l in file_contents:
        instructions = l.strip().split(" ")
        if instructions[0] == "noop":
            cycle, crt_screen = endcycle(cycle, x, crt_screen)
        elif instructions[0] == "addx":
            cycle, crt_screen = endcycle(cycle, x, crt_screen)
            cycle, crt_screen = endcycle(cycle, x, crt_screen)
            x += int(instructions[1])

for idx, s in enumerate(crt_screen):
    print(s, end="")
    if idx % 40 == 39:
        print()