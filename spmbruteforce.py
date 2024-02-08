from copy import deepcopy
from copy import copy
from time import perf_counter
squiglets = [2] * 10
summaxpnts = 0
maxpnts = 0
def SimuQuickEnd(crntsquiglet,crntpoints,crntChain):
    global maxpnts
    for i in crntsquiglet:
        crntChain += 100
        crntpoints += crntChain
    if crntpoints > maxpnts:
        
        maxpnts = crntpoints
    
def BruteForce(crntsquiglet,crntPoints,crntChain,depth=0,prnt=False):
    global maxpnts
    crntAttack = (crntPoints > 20000) + 1
    if crntPoints > maxpnts:
        if prnt:
            print(crntPoints)
        summaxpnts = sum(crntsquiglet)
        maxpnts = crntPoints
    if crntAttack != 2:
        for i in range(len(crntsquiglet)):
            sq = copy(crntsquiglet)
            sq[i] -= 1 #applies the damage: set to 1 since
            if sq[i] <= 0:
                newChain = crntChain + 100
                del sq[i]
            else:
                newChain = crntChain
            newpnts = crntPoints + newChain
            

            BruteForce(sq,newpnts,newChain,depth + 1)
    else:
        sq = copy(crntsquiglet)
        sq[0] -= 2 #applies the damage: set to 2 since
        
        newChain = crntChain + 100
        del sq[0]
        
        if newpnts < maxpnts and summaxpnts > sum(squiglets):
            #doesnt continue bruteforce if its already "fallen behind"
            return

        BruteForce(sq,newpnts,newChain,depth + 1)



for i in range(10):
    t = perf_counter()
    BruteForce([2] * i,0,0)
    t = perf_counter() - t
    print(t)
    print(i)

#BruteForce(deepcopy(squiglets),0,0)
print(maxpnts)

        
