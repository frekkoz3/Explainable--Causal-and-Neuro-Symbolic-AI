
% =====================================
% DOMAIN
% =====================================

person(a;b;c;d).


% =====================================
% FACTS
% =====================================

% Dana likes Cody
rel(d,c).

% Abby does not like Dana
:- rel(a,d).

% Dana does not like Abby
:- rel(d,a).

% Bess likes Cody OR Dana
rel(b,c) | rel(b,d).


% =====================================
% RULES
% =====================================

% Abby likes everyone Bess likes
rel(a,X) :- rel(b,X).

% Cody likes everyone who likes her
rel(c,X) :- rel(X,c).

% Nobody likes herself
:- rel(X,X), person(X).


% =====================================
% OUTPUT
% =====================================

#show rel/2.
