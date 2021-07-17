#!/usr/bin/python
import os, sys
from wallaby import *
import actions as a

def main():
    print("Starting my program!")
    enable_servos()
    a.my_first_method()
    
    print("Ending my program. See you again soon!")
    

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
