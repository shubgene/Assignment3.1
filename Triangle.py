# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 00:46:27 2018

@author: shurastogi
"""

class Triangle:
    def __init__(self):
        self.first_side=0
        self.second_side=0
        self.third_side=0
    
    def input_param(self):
        self.first_side=float(input("enter first side length"))
        self.second_side=float(input("enter second side length"))
        self.third_side= float(input("enter third side length"))
        
        
class TriangleArea(Triangle):
    
    def __init__(self):
        Triangle.__init__(self)
        pass
    
    def area(self):
        first_side=self.first_side
        second_side=self.second_side
        third_side=self.third_side
        s = (first_side + second_side + third_side) / 2
        area = (s*(s-first_side)*(s-second_side)*(s-third_side)) ** 0.5
        print('The area of the triangle is %.2f' %area)
        

t=TriangleArea()
t.input_param()
t.area()
    