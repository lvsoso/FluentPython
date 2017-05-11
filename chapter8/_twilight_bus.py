# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:57:13 2017

"""

class TwilightBus(object):

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
        
        
if __name__ == "__main__":
    
    bus1 = TwilightBus(['Alice', 'Bill'])
    print bus1.passengers
    bus1.pick("xx")
    print bus1.passengers
    bus1.drop("Alice")
    print bus1.passengers
    
    bus2 = TwilightBus()
    print bus2.passengers
    bus2.pick("Carrie")
    bus3 = TwilightBus()
    print bus3.passengers
    bus3.pick("Dave")
    print bus2.passengers
    
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
    bus = TwilightBus(basketball_team)
    bus.drop('Tina')
    bus.drop('Pat')
    print basketball_team