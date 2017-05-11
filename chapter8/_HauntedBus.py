# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:25:21 2017

"""

class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):  # <1>
        self.passengers = passengers  # <2>

    def pick(self, name):
        self.passengers.append(name)  # <3>

    def drop(self, name):
        self.passengers.remove(name)
        
        
if __name__ == "__main__":
    bus1 = HauntedBus(['Alice', 'Bill'])
    print bus1.passengers
    bus1.pick("xx")
    print bus1.passengers
    bus1.drop("Alice")
    print bus1.passengers
    
    bus2 = HauntedBus()
    print bus2.passengers
    bus2.pick("Carrie")
    bus3 = HauntedBus()
    print bus3.passengers
    bus3.pick("Dave")
    print bus2.passengers
    