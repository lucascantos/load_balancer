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

def check_chains(index):
    if np.any(chain_index[:] == index):
        print("ja tem")
        return
    else:
        chain_index.append(index)


chain_index = [0]
flag = True
while flag:
    print(f"New Chain starting at {chain_index[0]}")
    dynamic_machine = np.zeros(ttask + len(users_input))
    rolling_sum = 0
    for index in range(chain_index[0], len(users_input)):
        print(index)
        users = users_input[index]
        users_diff = users - solo_machine[index]*umax

        
        rolling_sum += users_diff        
        if users_diff > 0:
            if np.any(dynamic_machine + make_chain(index)[:] > umax):
                print(f'index: {index} insidelink')
                check_chains(index)
                continue

            if 0 < dynamic_machine[index] < umax  or index == chain_index[0]:
                total_ticks = index + ttask-1 
            else:
                print(f"index: {index} new chain m8")
                check_chains(index)
                continue     

            dynamic_machine += make_chain(index)
        print(f'index: {index} - {users_diff} | {rolling_sum} | {total_ticks} | {dynamic_machine}')
    flag = False
    

        #     if rolling_sum == 0:
        #         print("NEW CHAIN")
        #         vm_tick_users = np.zeros(ttask + len(users_input))
                
        #     rolling_sum += users_diff
        #     if rolling_sum > umax:
        #         print("Overflow")
        #         rolling_sum = umax




 

