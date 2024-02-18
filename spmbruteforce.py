from copy import deepcopy
from copy import copy
from time import perf_counter


def pntsToLevel(points):
    if points > 20000:
        if points > 60000:
            if points > 120000:
                return 4
            return 3
        return 2
    return 1

def hitsNeeded(enemy,crntAttack):
    return enemy // crntAttack + ((enemy % crntAttack) != 0)
def quicksimLevelup(enemies,crntPoints,crntChain):
    """return (newpoints,iflevelup)"""
    m = max(enemies)
    newPoints = crntPoints
    atk = pntsToLevel(crntPoints)
    while enemies != []:
        enemies[0] -= atk
        if enemies[0] <= 0:
            crntChain += 100
            del enemies[0]
        newPoints += crntChain
    return (newPoints,hitsNeeded(m,pntsToLevel(newPoints)) != hitsNeeded(m,atk))       

assert pntsToLevel(10 * 1000) == 1
assert pntsToLevel(30000) == 2
assert quicksimLevelup([2] * 22,0,0) == (48400,True),quicksimLevelup([2]*22,0,0)



maxpnts = 0

Count = 0
def BruteForce(crntEnemies,crntPoints,crntChain, count=False,):
    """crntenemies: enemies left to brute force through
    crntpoints: current player points
    crntchain: current amount of points gained per enemy hit
    count: whether the code should track all bruteforce executions in the Count variable"""
    if count:
        global Count
        Count += 1
   
    crntAttack = pntsToLevel(crntPoints)
    if crntEnemies == []:
        
        return crntPoints
    #if mindlessly jumping on the squiglet never leads to an attack level up that changes the amounts of hits needed to kill the strongest enemy, its always most optimal to simply kill them in order.
    qsl = quicksimLevelup(deepcopy(crntEnemies),copy(crntPoints),copy(crntChain))
    if not qsl[1]:
        return qsl[0]

    #start the standard bruteforce routine
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
        minHP = 99999999 
        for i in range(len(seenHPs)):
            if seenHPs[i] < minHP:
                minHP = seenHPs[i]
                minIndex = HPindex[i]
        seenHPs = [minHP]
        HPindex = [minIndex]
                
        





    CurrentMax = 0
    for i in HPindex:
           sq = copy(crntEnemies)
           sq[i]-= crntAttack #applies the damage
           if sq[i] <= 0:
                newChain = crntChain + 100
                del sq[i]
           else:
               newChain = crntChain
               
           newpnts = crntPoints + newChain
           t = BruteForce(sq,newpnts,newChain,count)
           if CurrentMax < t:
               CurrentMax = t
    return CurrentMax
               

t = perf_counter()
BruteForce([1] * 10,0,0,count=True)
t = perf_counter() - t
cycleCount = t / Count
maxpnts = 0



for i in range(100):
    if i == 0:
        continue
    print("# of squigs ",i)

    #VERY rough time estimation for the calculation
    cycleCountEstimate = (2.0 ** 1.5) ** float(i)
    timeEstimate = cycleCountEstimate * cycleCount
    print("time estimation:",timeEstimate)

    t = perf_counter()
    maxpnts = BruteForce([2] * i,0,0)
    print("max points  ", maxpnts)
    t = perf_counter() - t
    print("time taken  ",t)
    print("-------------")

#BruteForce(deepcopy(squiglets),0,0)

        
