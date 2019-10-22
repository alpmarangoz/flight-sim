# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:31:38 2019

@author: amarangoz
"""
import uuid 

class Vehicle:
    var = "chk"
    
#    def __init__(self, name = 'v-' + str(uuid.uuid4()).split('-')[0][:4],
    def __init__(self,init_paramaters):
        # Check inputs, assign defaults for undefined ones        
        if "name" in init_paramaters:
            self.name = init_paramaters["name"]
        else:
            self.name = 'v-' + str(uuid.uuid4()).split('-')[0][:4]
            
        if "initial_position" in init_paramaters:
            self.position = init_paramaters["initial_position"]
        else:
            self.position = [0,0,0]
        
        if "initial_velocity" in init_paramaters:
            self.velocity = init_paramaters["initial_velocity"]
        else:
            self.velocity = [0,0,0]        
    
    def __str__(self):
        print_string = self.name + " is at position " + \
            str(self.position) + " with velocity of " + \
            str(self.velocity)
        return print_string

    
    def move(self):
        print(self.name + " is moving.")

    def calculateStates(self):
        print("Position is " + str(self.position))
        print("Velocity is " + str(self.velocity))
    
    
    

class Integration:
    def __init__(self, name):
        self.name = name
        
    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")



pars = {"name":"aklp","initial_position":[1,2,3],"initial_velocity":[3,4,5]}
v = Vehicle(pars)

