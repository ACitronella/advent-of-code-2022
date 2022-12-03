from functools import reduce

class SelfSettingDict(dict):
    def mySet(self, k, v):
        self[k] = v
        return self

d = reduce(lambda d, x: d.mySet(chr(ord("a")+x-1), x), range(1, 27), SelfSettingDict())
d = reduce(lambda d, x: d.mySet(chr(ord("A")+x-27), x), range(27, 53), d)

with open("input.txt", mode="r") as f:
    s = f.readlines()
    s = map(lambda x: (set(x[:len(x)//2]), set(x[len(x)//2:])), s)
    s = map(lambda x: x[0].intersection(x[1]).pop(), s)
    s = map(lambda x: d[x], s)
    print(sum(s))
