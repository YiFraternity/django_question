def read_file(file="./log/error.txt"):
    f = open(file,"r")
    lines = f.readlines()
    lst = []
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            continue
        lst.append(line)
    return lst




