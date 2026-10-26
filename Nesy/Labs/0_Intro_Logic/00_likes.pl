
% ====================================
% KNOWLEDGE BASE
% ====================================

% Known positive facts
rel(d, c).

% Known negative facts
neg_rel(a, d).
neg_rel(d, a).

% Nobody likes herself
neg_rel(X, X) :- person(X).

person(a).
person(b).
person(c).
person(d).

% Abby likes everyone Bess likes
rel(a, X) :- rel(b, X).

% Cody likes everyone who likes her
rel(c, X) :- rel(X, c).


% ====================================
% INFERENCE RULES
% ====================================

% Modus tollens:
% If B likes X implies A likes X,
% and A does not like X,
% then B does not like X.

neg_rel(b, X) :- neg_rel(a, X).

% Disjunctive syllogism:
% B likes C or D.
% If B does not like D, conclude B likes C.

rel(b, c) :- neg_rel(b, d).
rel(b, d) :- neg_rel(b, c).
