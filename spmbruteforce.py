from copy import deepcopy
from copy import copy
from time import perf_counter
summaxpnts = 0
maxpnts = 0
def SimuQuickEnd(crntsquiglet,crntpoints,crntChain):
    global maxpnts
    for i in crntsquiglet:
        crntChain += 100
        crntpoints += crntChain
    if crntpoints > maxpnts:
        
        maxpnts = crntpoints
    
def BruteForce(crntEnemies,crntPoints,crntChain,depth=0,prnt=False):
    global maxpnts
    crntAttack = (crntPoints > 20000) + 1
    if crntPoints > maxpnts:
        if prnt:
            print(crntPoints)
        summaxpnts = sum(crntEnemies)
        maxpnts = crntPoints
    if crntEnemies == []:
        return
    if not (crntAttack >= max(crntEnemies)):
        for i in range(len(crntEnemies)):
            sq = copy(crntEnemies)
            sq[i] -= crntAttack #applies the damage: set to 1 since
            if sq[i] <= 0:
                newChain = crntChain + 100
                del sq[i]
            else:
                newChain = crntChain
            newpnts = crntPoints + newChain
            

            BruteForce(sq,newpnts,newChain,depth + 1)
    else:
        SimuQuickEnd(crntEnemies,crntPoints,crntChain)



for i in range(22):
    t = perf_counter()
    BruteForce([2] * i,0,0)
    print(maxpnts)
    t = perf_counter() - t
    print(t)
    print(i)

#BruteForce(deepcopy(squiglets),0,0)
print(maxpnts)

        
