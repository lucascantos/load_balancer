

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
