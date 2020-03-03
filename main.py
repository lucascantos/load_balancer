from src.helpers import open_file, save_file
from src.unit_test import random_data
from src.load_balance import LoadBalance
import numpy as np

def main(input_path=None, output_path=None):
    # Open file and load data
    if input_path:
        input_data = open_file(input_path)
    else:
        output_path = 'test/random_output.txt'
        print('Performing random test')
        input_data = random_data()
        print(input_data)
    # Processing
    new_balance = LoadBalance(input_data[0], input_data[1], input_data[2:])

    # Making output
    total_cost = 0
    final_output=[]

    for vm in new_balance.load_balance():
        for i, users in enumerate(vm['connections']):
            if total_cost <= 0:
                final_output.append([users] if users > 0 else [])
            else:
                final_output[i].append(users) if users > 0 else None
        total_cost += vm['cost']
        
    if len(final_output[-1]) == 0:
        final_output[-1].append(0)

    final_output.append([total_cost])
    if not output_path:
        output_path = 'output.txt'
    save_file(output_path, final_output)

if __name__ == "__main__":
    main()
