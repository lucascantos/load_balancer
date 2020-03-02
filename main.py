import math

# abrir arquivo

# pegar ttask e umax

# loop nas demais linhas


# Remove Users

# Remove Server

# Add server

# Add user


umax = 2
ttask = 4

server_list = {
    'user_count': [],
    'ticks_used': [],
    'user_list': []
}

user_list = {
    'first_tick':[],
    'server_id': [],

}

tick_data = {
    'servers_active':[],
}
users_input = [1,3,0,1,0,1]


cost_count = [5,4,4]

def remove_users():
    pass

def add_users(users_number, server):
    pass

def available_servers(server_count):
    servers = []
    for server_id in range(server_count):
        if server_list['user_count'][server_id] <= umax:
            servers.append(server_id)

    return []

def remove_server():
    pass

def add_server():
    pass 

def tick_update():
    pass

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


        

 

