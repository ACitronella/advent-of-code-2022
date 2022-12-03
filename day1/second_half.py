
with open("input.txt", mode="r") as f:
    s = "".join(f.readlines())
    m = map(lambda x: x.split("\n"), s.split("\n\n")) # seperate each str of number into their own list
    m = map(lambda x: map(int, x), m)                 # convert each of str of number into number
    m = map(sum, m)                                   # get a sum of each input
    print(sum(sorted(m)[-3:]))

