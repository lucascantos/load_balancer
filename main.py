import math
import numpy as np

users_input = [1,3,0,1,0,1]
umax = 2
ttask = 4

def make_chain(index, value):
    chain_ticks = np.zeros(ttask + len(users_input))

    if index > len(users_input):
        print("Index too high!")
        return None

    for link in range(ttask):
        chain_ticks[index + link] = value
    return chain_ticks

def check_chains(index): 
    if np.any(np.array(chain_index)[:] == index):
        return
    else:
        chain_index.append(index)

chain_index = [0]

flag = True
while len(chain_index) > 0:
    print(f"New Chain starting at {chain_index[0]}")
    dynamic_vm = np.zeros(ttask + len(users_input))
    rolling_sum = 0
    cap_meter = 2
    for index in range(chain_index[0], len(users_input)):
        users = users_input[index]
        users_diff = users        
        rolling_sum += users_diff  
         
        if users_diff > 0:
            if np.any(dynamic_vm + make_chain(index, users_diff)[:] > umax):
                check_chains(index)
                if cap_meter <= 0:
                    continue
                else:
                    users_diff = cap_meter

            if 0 < dynamic_vm[index] < umax  or index == chain_index[0]:
                total_ticks = index + ttask-1 
                cap_meter = umax - users_diff
                users_input[index] -= cap_meter
            else:
                check_chains(index)
                continue     
  
            dynamic_vm += make_chain(index, users_diff)
    print(users_input)
    print(f'index: {index} - {users_diff} | {cap_meter} | {rolling_sum} | {total_ticks} | {dynamic_vm}')

    del chain_index[0]
    

        #     if rolling_sum == 0:
        #         print("NEW CHAIN")
        #         vm_tick_users = np.zeros(ttask + len(users_input))
                
        #     rolling_sum += users_diff
        #     if rolling_sum > umax:
        #         print("Overflow")
        #         rolling_sum = umax




 

