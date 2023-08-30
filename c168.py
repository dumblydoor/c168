#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:04:39 2023

@author: aquilavijayanayagam
"""



class Citizen:
    def _init_(self,name,age,dob,id_number):
        self.Citizen_name = name 
        self.Citizen_age = age
        self.Citizen_dob = dob 
        self.Citizen_id = id_number
        
    def add_citizen(self):
        print("name: "+self.Citizen_name)
        print("age: "+str(self.Citizen_age))
        print("date of birth:"+self.Citizen_dob)
        print("citizen Id:"+self.Citizen_id)
        print("citizen added")
        
        
citizen1 = Citizen("peter",8,"19th october 2012","0198")
citizen1.add_citizen()

citizen2 = Citizen("sophia",10,"19th october 2010","0199")
citizen2.add_citizen()



        

