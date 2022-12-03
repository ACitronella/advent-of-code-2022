from functools import reduce

class SelfSettingDict(dict):
    def mySet(self, k, v):
        self[k] = v
        return self

def group_3_lines(s:"list[str]") -> "list[str]":
    if s:
        return [s[0] + s[1] + s[2]] + group_3_lines(s[3:])
    return []

d = reduce(lambda d, x: d.mySet(chr(ord("a")+x-1), x), range(1, 27), SelfSettingDict())
d = reduce(lambda d, x: d.mySet(chr(ord("A")+x-27), x), range(27, 53), d)

with open("input.txt", mode="r") as f:
    s = f.readlines()
    s = group_3_lines(s)
    s = map(lambda x: list(map(lambda y: set(y), x.split("\n"))), s)
    s = map(lambda x: x[0].intersection(x[1]).intersection(x[2]).pop(), s)
    s = map(lambda x: d[x], s)
    print(sum(s))
