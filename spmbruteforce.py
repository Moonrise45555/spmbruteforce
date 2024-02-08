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
    crntAttack = (crntPoints > 20000) + 1 + (crntPoints > 60000)
   
    if crntEnemies == []:
        if crntPoints > maxpnts:
            maxpnts = crntPoints
        return
    if (crntAttack >= max(crntEnemies)):
        #all enemies will go down in one hit anyway: it doesnt matter which one we choose
        SimuQuickEnd(crntEnemies,crntPoints,crntChain)
    else:
        for i in range(len(crntEnemies)):
            seenHPs = []
            HPindex = []
            if crntEnemies[i] in seenHPs:
                continue
            else:
                seenHPs.append(crntEnemies[i])
                HPindex.append(i)







        for i in range(len(seenHPs)):
            sq = copy(crntEnemies)
            sq[HPindex[i]] -= crntAttack #applies the damage
            if sq[HPindex[i]] <= 0:
                newChain = crntChain + 100
                del sq[HPindex[i]]
            else:
                newChain = crntChain
            newpnts = crntPoints + newChain
            

            BruteForce(sq,newpnts,newChain,depth + 1)
    



for i in range(22):
    print(i)
    t = perf_counter()
    BruteForce([2] * i,0,0)
    print(maxpnts)
    t = perf_counter() - t
    print(t)

#BruteForce(deepcopy(squiglets),0,0)

        
