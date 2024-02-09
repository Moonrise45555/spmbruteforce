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
    seenHPs = []
    HPindex = []
    for i in range(len(crntEnemies)):
        
        
        if seenHPs.count(crntEnemies[i]) > 0:
            continue
        else:
            seenHPs.append(crntEnemies[i])
            HPindex.append(i)
    if crntChain == 0:
        #if you have 0 chain, you jump on the one with the least HP, since jumping on anything that wouldnt die would be a waste anyway
        #maybe kills the completeness of the program? 
        minHP = 100000
        for i in range(len(seenHPs)):
            if seenHPs[i] < minHP:
                minHP = seenHPs[i]
                minIndex = HPindex[i]
        seenHPs = [minHP]
        HPindex = [minIndex]
                
        






    for i in HPindex:
           sq = copy(crntEnemies)
           sq[i]-= crntAttack #applies the damage
           if sq[i] <= 0:
               newChain = crntChain + 100
               del sq[i]
           else:
               newChain = crntChain
           newpnts = crntPoints + newChain
           
           BruteForce(sq,newpnts,newChain,depth + 1)
    



for i in range(1000):
    print("# of squigs ",i)
    t = perf_counter()
    BruteForce([2] * i,0,0)
    print("max points  ", maxpnts)
    t = perf_counter() - t
    print("time taken  ",t)

#BruteForce(deepcopy(squiglets),0,0)

        
