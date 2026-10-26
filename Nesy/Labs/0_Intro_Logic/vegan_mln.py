"""Exact inference for a two-person Markov Logic Network.

1.3: forall x, Vegan(x) -> Healthy(x)
0.7: forall x,y, Friends(x,y) -> (Vegan(x) <-> Vegan(y))

All four directed friendship atoms, including self-relations, are modeled.
"""
from itertools import product
from math import exp

PEOPLE = ('A', 'B')
ATOMS = (
    *(('Vegan', x) for x in PEOPLE),
    *(('Healthy', x) for x in PEOPLE),
    *(('Friends', x, y) for x in PEOPLE for y in PEOPLE),
)
W1, W2 = 1.3, 0.7


def features(world):
    # Material implication: P -> Q is equivalent to (not P) or Q.
    n1 = sum((not world['Vegan', x]) or world['Healthy', x]
             for x in PEOPLE)
    # Biconditional: P <-> Q is equivalent to (P == Q).
    n2 = sum((not world['Friends', x, y]) or
             (world['Vegan', x] == world['Vegan', y])
             for x in PEOPLE for y in PEOPLE)
    return n1, n2


def worlds_and_weights():
    for values in product((False, True), repeat=len(ATOMS)):
        world = dict(zip(ATOMS, values))
        n1, n2 = features(world)
        yield world, exp(W1 * n1 + W2 * n2)


WORLD_WEIGHTS = list(worlds_and_weights())
Z = sum(weight for _, weight in WORLD_WEIGHTS)


def probability(query, evidence=lambda world: True):
    """Return P(query | evidence), using exact enumeration."""
    denominator = sum(w for world, w in WORLD_WEIGHTS if evidence(world))
    if denominator == 0:
        raise ValueError('Conditioning event has zero probability')
    numerator = sum(w for world, w in WORLD_WEIGHTS
                    if evidence(world) and query(world))
    return numerator / denominator


if __name__ == '__main__':
    print('Ground atoms:', len(ATOMS))
    print('Possible worlds:', len(WORLD_WEIGHTS))
    print('Partition function Z:', round(Z, 6))

    vegan_A = lambda world: world['Vegan', 'A']
    vegan_B = lambda world: world['Vegan', 'B']
    healthy_A = lambda world: world['Healthy', 'A']
    friends_AB = lambda world: world['Friends', 'A', 'B']

    print('P(Vegan(A)) =', round(probability(vegan_A), 4))
    print('P(Healthy(A) | Vegan(A)) =',
          round(probability(healthy_A, vegan_A), 4))
    print('P(Vegan(B) | Vegan(A), Friends(A,B)) =',
          round(probability(vegan_B,
                            lambda w: vegan_A(w) and friends_AB(w)), 4))
    print('P(Vegan(B) | Vegan(A), not Friends(A,B)) =',
          round(probability(vegan_B,
                            lambda w: vegan_A(w) and not friends_AB(w)), 4))
    # Let ￼ be the world where ￼ and ￼ are vegan, unhealthy and have no friends.
    # compute P(X=x) ￼
    p = probability(
        lambda w: (
            all(w["Vegan", x] for x in PEOPLE)
            and all(not w["Healthy", x] for x in PEOPLE)
            and all(
                not w["Friends", x, y]
                for x in PEOPLE for y in PEOPLE
            )
        )
    )

    print("P(world) =", p)