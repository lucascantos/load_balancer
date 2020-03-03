import numpy as np

def open_file(path):
    return np.loadtxt(path, int)

def save_file(path, data):
    with open(path,"w") as f:
        f.write("\n".join(",".join(map(str, x)) for x in data))