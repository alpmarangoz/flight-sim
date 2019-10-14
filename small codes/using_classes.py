# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:31:38 2019

@author: amarangoz
"""
import uuid 

class Vehicle:
    var = "chk"
    
#    def __init__(self, name = 'v-' + str(uuid.uuid4()).split('-')[0][:4], 
    def __init__(self, name = 'v-' + str(uuid.uuid4()).split('-')[0][:4], 
                 initial_position = [0,0,0], 
                 initial_velocity = [0,0,0]):
        
        self.name = name
        self.position = initial_position
        self.velocity = initial_velocity
        
        
    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")



class Shark:
    def __init__(self, name):
        self.name = name
        
    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")


def main():
    sammy = Shark('a')
    sammy.swim()
    sammy.be_awesome()

if __name__ == "__main__":
    main()


