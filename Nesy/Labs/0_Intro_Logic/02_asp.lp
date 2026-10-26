% Run: clingo 02_asp.lp 0
robot(r1;r2).
task(t1;t2).
1 { assign(R,T) : robot(R) } 1 :- task(T).
:- assign(r1,t2).
#show assign/2.

