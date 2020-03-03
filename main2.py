import math
import numpy as np

users_input = [9,9,0,0,9,0]
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

while np.array(users_input).any():
    max_cap = umax
    single_chain = make_chain(0,0)
    for index, users in enumerate(users_input):
        if max_cap > 0 :
            if users > max_cap:
                users = max_cap
            users_input[index] -= users
            single_chain += make_chain(index, users)
        max_cap = umax - single_chain[index+1]


        if not np.array(single_chain).any():
            continue

        if single_chain[index+1] <= 0:
            break




