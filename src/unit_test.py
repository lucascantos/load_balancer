import random
from src.helpers import save_file

def random_data():
    ttask = random.randint(1, 10)
    umax = random.randint(1, 10)

    input_data = [ttask, umax]
    for _ in range(random.randint(2, 10)):
        input_data.append(random.randint(0,10))
    
    with open('test/random_input.txt',"w") as f:
        f.write("\n".join(map(str, input_data)))
    return input_data
