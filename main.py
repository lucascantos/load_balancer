import math
import numpy as np

users_input = [1,3,0,1,0,1]
umax = 2
ttask = 4

def make_chain(index):
    chain_ticks = np.zeros(ttask + len(users_input))

    if index > len(users_input):
        print("Index too high!")
        return None

    for link in range(ttask):
        chain_ticks[index + link] = 1
    return chain_ticks

# Make a list with machines which will last only ttask
n_machines = lambda x: math.floor(x/umax)
solo_machine = [n_machines(users) if users>umax else 0 for users in users_input]


new_chain = True
dynamic_machine = []
chain_index = []
while new_chain:

    rolling_sum = 0

    for index in range(len(users_input)):
        users = users_input[index]
        users_diff = users - solo_machine[index]*umax
        print(f'index: {index}')

        if users_diff > 0:
            if rolling_sum == 0:
                print("NEW CHAIN")
                vm_tick_users = np.zeros(ttask + len(users_input))
                
            rolling_sum += users_diff
            if rolling_sum <= umax:
                total_ticks = index + ttask
                vm_tick_users += make_chain(index)
            else:             
                dynamic_machine.append(vm_tick_users)   
                rolling_sum = 0           

            
            print(vm_tick_users)
    print(dynamic_machine)
    new_chain=False




 

