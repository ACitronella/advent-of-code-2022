from functools import reduce
import re
shelf = {}
ops_line_format = re.compile("move (\\d+) from (\\d+) to (\\d+)")

def ops_on_shelf(shelf, howmany, sour, dest):
    tmp = []
    for _ in range(howmany):
        tmp.append(shelf[sour].pop())
    shelf[dest].extend(tmp[::-1])
    return shelf

def extract_ops_params(op_str):
    r = ops_line_format.match(op_str)
    howmany = int(r.group(1))
    sour = int(r.group(2))
    dest = int(r.group(3))
    return howmany, sour, dest

with open("input.txt", mode="r") as f:
    max_shelf_num = 0
    fl = f.readlines()
    sep_line = 0
    while sep_line < len(fl) and fl[sep_line] != "\n":
        sep_line += 1
    for idx, v in enumerate(fl[sep_line-1]):
        if v != " " and v != "\n":
            v = int(v)
            shelf[v] = list(filter(lambda y: y != " ", map(lambda x : x[idx], fl[:sep_line-1])))[::-1]
            if v > max_shelf_num:
                max_shelf_num = v
    shelf = reduce(lambda sh, params: ops_on_shelf(sh, params[0], params[1], params[2]), map(extract_ops_params, fl[sep_line+1:]), shelf)
    for idx in range(1, max_shelf_num+1):
        print(shelf[idx][-1], end="")

