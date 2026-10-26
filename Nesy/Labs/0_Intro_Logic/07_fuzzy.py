"""Fuzzy truth degrees with Zadeh operators and Lukasiewicz implication."""
a = 0.8  # truth degree of charged(robot)
b = 0.6  # truth degree of door_open(robot)
print('charged:', a)
print('door_open:', b)
print('NOT charged (1-a):', 1-a)
print('charged AND door_open (min):', min(a,b))
print('charged OR door_open (max):', max(a,b))
print('Lukasiewicz implication charged -> door_open:', min(1,1-a+b))
