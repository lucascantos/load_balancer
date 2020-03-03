import math

# abrir arquivo

# pegar ttask e umax

users_input = [1,3,0,1,0,1]

# Make a list with machines which will last only ttask
n_machines = lambda x: math.floor(x/umax)
solo_machine = [n_machines(users) if users>umax else 0 for users in users_input]

new_chain = True
dinamic_machine = []
chain_index = []
while new_chain:
    for index in range(len(users_input)):
        
        user = users_input[index]
        if users > 0:

        # New Chain
        chain_index.append(index)


        

 

