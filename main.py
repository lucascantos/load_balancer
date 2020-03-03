from src.helpers import open_file, save_file
from src.load_balance import LoadBalance
import numpy as np


input_path = 'input/input.txt'
input_data = open_file(input_path)
new_balance = LoadBalance(input_data[0], input_data[1], input_data[2:])
total_cost = 0
output_path = 'output/output.txt'
x=[]
for j, vm in enumerate(new_balance.load_balance()):
    for i, users in enumerate(vm['connections']):
        if j <= 0:
            x.append([users])
        else:
            x[i].append(users)

print(x)