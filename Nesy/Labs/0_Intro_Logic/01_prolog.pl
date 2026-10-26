% Run: swipl -s 01_prolog.pl
likes(alice,bob).
likes(bob,alice).
likes(alice,charlie).
friends(X,Y) :- likes(X,Y), likes(Y,X).
% At prompt: ?- friends(alice,bob).
% At prompt: ?- friends(X,Y).


