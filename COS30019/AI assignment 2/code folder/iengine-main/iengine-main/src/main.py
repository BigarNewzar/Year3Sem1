#!/usr/bin/env python3
import sys
#import time
#import psutil
from PLAgent import PLAgent


#testing start time
#tm0 = time.time_ns()
method = sys.argv[1]
filename = sys.argv[2]

#printing to ensure parameters passed to proper variables
#print(filename)
#print(method)

# Spawn an agent
agent = PLAgent(filename)

#make agent interpret method
agent.interpret(method)



#part of time and memory collection, decided to use directly from tt,fc and bc instead
#tm1 = time.time_ns()
#mem = psutil.virtual_memory().available
#print('Runtime from Main: ' + str(tm1 - tm0))
#print('Memory from Main: ' + str(mem))
