from copy import deepcopy
from copy import copy
from time import perf_counter

maxpnts = 0

Count = 0
def BruteForce(crntEnemies,crntPoints,crntChain, count=False):
    """crntenemies: enemies left to brute force through
    crntpoints: current player points
    crntchain: current amount of points gained per enemy hit
    count: whether the code should track all bruteforce executions in the Count variable"""
    if count:
        global Count
        Count += 1
   
    global maxpnts
    global summaxpnts
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
        minHP = 99999999 
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
           
           BruteForce(sq,newpnts,newChain,count)

t = perf_counter()
BruteForce([1] * 10,0,0,count=True)
t = perf_counter() - t
cycleCount = t / Count
maxpnts = 0



for i in range(1000):
    i = 22
    if i == 0:
        continue
    print("# of squigs ",i)

    #VERY rough time estimation for the calculation
    cycleCountEstimate = (2.0 ** 1.5) ** float(i)
    timeEstimate = cycleCountEstimate * cycleCount
    print("time estimation:",timeEstimate)

    t = perf_counter()
    BruteForce([2] * i,0,0)
    print("max points  ", maxpnts)
    t = perf_counter() - t
    print("time taken  ",t)
    print("-------------")

#BruteForce(deepcopy(squiglets),0,0)

        
