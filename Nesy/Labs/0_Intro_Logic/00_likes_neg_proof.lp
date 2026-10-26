
% ============================================
% 1. DOMAIN
% ============================================

person(a;b;c;d).


% ============================================
% 2. FACTS
% ============================================

% Dana likes Cody
rel(d,c).

% Abby does not like Dana
-rel(a,d).

% Dana does not like Abby
-rel(d,a).

% Bess likes Cody OR Dana
rel(b,c) | rel(b,d).


% ============================================
% 3. LOGICAL RULES
% ============================================

% Abby likes everyone Bess likes
rel(a,X) :- rel(b,X).

% Cody likes everyone who likes her
rel(c,X) :- rel(X,c).

% Nobody likes herself
-rel(X,X) :- person(X).


% ============================================
% 4. NEGATIVE INFERENCE
% ============================================

% Contrapositive:
% If Abby does not like X,
% then Bess cannot like X.

-rel(b,X) :- -rel(a,X), person(X).


% ============================================
% 5. OUTPUT
% ============================================

#show rel/2.
#show -rel/2.
