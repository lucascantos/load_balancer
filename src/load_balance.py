import numpy as np

# self.users_input = [1,3,0,1,0,1]
# self.umax = 2
# self.ttask = 4
'''
A simple load balance algorithm.
The idea is to check the final cost of Virtual Machines
based on the load of users connected to it. 

A single virtual machine can be viewd as a chain vector
on which the links are connected if the new users connected
can be placed on the current VM. 

Author: Lucas Cantos
'''
class LoadBalance(object):
    def __init__(self, ttask, umax, users_input):
        '''

        '''
        self.users_input = users_input
        self.umax = umax
        self.ttask = ttask

    def load_balance(self):
        '''
    
        '''    
        # If there are still users, a new VM (chain) will be made  
        while np.array(self.users_input, int).any():
            max_cap = self.umax
            single_chain = self._make_chain(0,0)

            for index, users in enumerate(self.users_input):
                # Checks if there is room for new users and if placing them will overload
                if max_cap > 0 :
                    if users > max_cap:
                        users = max_cap
                    self.users_input[index] -= users

                    try:
                        # Just a precaution
                        single_chain += self._make_chain(index, users)
                    except Exception as e:
                        print(f'Index too high, returned a None: {e}')
                        raise
                            
                max_cap = self.umax - single_chain[index+1]
                
                # On new terations, ignore if n of users is zero
                if not np.array(single_chain).any():
                    continue
                
                # If the next link in chain is zero, the chain is over. Next
                if single_chain[index+1] <= 0:
                    break
            yield {
                'connections': list(single_chain),
                'cost': self._vm_cost(single_chain)
                }
    
    def _make_chain(self, index, value):
        '''
        Make a vector of size equal to the number of wroking ticks
        int index: the starting index to be filled
        int value: the magnitude of the vector
        '''
        chain_ticks = np.zeros(self.ttask + len(self.users_input), int)

        if index > len(self.users_input):
            print("Index too high!")
            return None
        
        for link in range(self.ttask):
            chain_ticks[index + link] = value
        return chain_ticks

    def _vm_cost(self,vm, price=1):
        '''
        Calculate the price of a given VM
        np.array vm: numpy array of users on a given VM
        float price: price value of a single tick. Defaul = 1
        '''        
        vm_cost = np.count_nonzero(vm) * price
        return vm_cost