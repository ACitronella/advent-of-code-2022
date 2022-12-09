import re
class Directory():
    def __init__(self):
        self.directory = {"/": {}}
        self.current_dir = ["/"]
    def mkdir(self, folder:str):
        d = self.directory
        for v in self.current_dir:
            d = d[v]
        d[folder] = {}

    def mkfile(self, file:str, size:int):
        d = self.directory
        for v in self.current_dir:
            d = d[v]
        d[file] = size

    def cd(self, folder:str):
        if folder == "/":
            self.current_dir = ["/"]
        elif folder == "..":
            self.current_dir.pop()
        else:
            self.mkdir(folder)
            self.current_dir.append(folder)
        return self
    def ls(self, file:str, size:int):
        self.mkfile(file, size)
        return self
    @staticmethod
    def getSize(d:dict, s=0) -> int:
        for k, v in d.items():
            if isinstance(v, int): s += v
            else:
                s += Directory.getSize(v, s)
        return s
    @staticmethod
    def traverlyGetSize(d:dict):
        l = []
        def getSize(d:dict) -> int: # i consider this as cheating but i have no choice
            s = 0
            for k, v in d.items():
                if isinstance(v, int): s += v
                else: 
                    si = getSize(v)
                    l.append(si)
                    s += si
            return s
        getSize(d)
        return l

d = Directory()
cd_regex = r"\$ cd ([\w./]+)"
list_file_regex = r"(\d+) ([\w.]+)"
list_folder_regex = r"dir (\w+)"
cd_regex = re.compile(cd_regex)
list_file_regex = re.compile(list_file_regex)
list_folder_regex = re.compile(list_folder_regex)

with open("input.txt", mode="r") as f:
    for cmd in f.readlines():
        if (m:=cd_regex.match(cmd)):
            args = m.group(1)
            d.cd(args)
        if (m:=list_file_regex.match(cmd)):
            size = int(m.group(1))
            file = m.group(2)
            d.mkfile(file, size)
        if (m:=list_folder_regex.match(cmd)):
            folder = m.group(1)
            d.mkdir(folder)
    print(sum(filter(lambda x : x < 100000, Directory.traverlyGetSize(d.directory))))
