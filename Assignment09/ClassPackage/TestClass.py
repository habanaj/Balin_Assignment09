'''
Name: Group Balin
email:earleyja@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can collaborate on a project using github and know how to use Object Oriented programming.
Citations:
Anything else that's relevant:
'''
class Hamburger(): # Creating a class based on an object in the real world that I really love
    def __init__(self, cheese, pattynumber): 
        self.cheese = cheese
        self.pattynumber = pattynumber
         
        
    def setpattynumber(self, pattynumber):
        self.validatePatty(pattynumber)
        
    def validatePatty(self, pattynumber): # this non dunder method checks to make sure the patty is no less than 1 
        if pattynumber<1:
            print(" What are you, vegan? ")
        else:
            self.pattynumber = pattynumber
            
        
            
            
    def __repr__(self):
        return " The number of patties on your order: " + str(self.pattynumber)
    
    def __str__(self):
        return " You ordered " + self.cheese + " on your burger. "