x = 1
signal_strength = 0
cycle = 0

def endcycle(cycle:int , signal_strength:int):
    cycle += 1
    print(cycle, x, x * cycle, sep="\t")
    if cycle % 40 - 20 == 0:
        signal_strength += x*cycle
    return cycle, signal_strength


with open("small_input.txt", mode="r") as f:
    file_contents = f.readlines()

    for l in file_contents:
        instructions = l.split(" ")
        if instructions[0].strip() == "noop":
            cycle, signal_strength = endcycle(cycle, signal_strength)
        elif instructions[0].strip() == "addx":
            cycle, signal_strength = endcycle(cycle, signal_strength)
            cycle, signal_strength = endcycle(cycle, signal_strength)
            x += int(instructions[1])

print(signal_strength)