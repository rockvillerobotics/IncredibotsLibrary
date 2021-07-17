from wallaby import *
import movement as m
import sensors as s

def my_first_method():
    print("Starting my_first_method()")

    s.line_follow(0, 2000, 1000)
   
    

def my_second_method():
   print("Starting my_second_method()")
        
# This file is your central work place. 
# Working in a file other than "main" allows you to quickly move methods 
# in and out, which makes it easier to focus on one method at a time.