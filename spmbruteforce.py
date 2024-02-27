from copy import deepcopy
from copy import copy
from time import perf_counter
chainGain = 100


def pntsToLevel(points):
    if points >= 20000:
        if points >= 60000:
            if points >= 120000:
                return 4
            return 3
        return 2
    return 1

def hitsNeeded(enemy,crntAttack):
    return enemy // crntAttack + ((enemy % crntAttack) != 0)
def quicksimLevelup(enemies,crntPoints,crntChain,crntPath=""):
    """return (newpoints,iflevelup)"""
    m = max(enemies)
    newPoints = crntPoints
    atk = pntsToLevel(crntPoints)
    while enemies != []:
        crntPath = crntPath + str(enemies[0])
        enemies[0] -= atk
        if enemies[0] <= 0:
            crntChain += chainGain
            del enemies[0]
        newPoints += crntChain
    return ((newPoints,crntPath),hitsNeeded(m,pntsToLevel(newPoints)) != hitsNeeded(m,atk))       

assert pntsToLevel(10 * 1000) == 1
assert pntsToLevel(30000) == 2
assert quicksimLevelup([2] * 22,0,0) == ((48400,"21" * 22),True),quicksimLevelup([2]*22,0,0)



maxpnts = 0

Count = 0
def BruteForce(crntEnemies,crntPoints,crntChain, count=False,crntPath=""):
    """crntenemies: enemies left to brute force through
    crntpoints: current player points
    crntchain: current amount of points gained per enemy hit
    count: whether the code should track all bruteforce executions in the Count variable"""
    if count:
        global Count
        Count += 1
   
    crntAttack = pntsToLevel(crntPoints)
    if crntEnemies == []:
        
        return (crntPoints,crntPath)
    #if mindlessly jumping on the squiglet never leads to an attack level up that changes the amounts of hits needed to kill the strongest enemy, its always most optimal to simply kill them in order.
    qsl = quicksimLevelup(deepcopy(crntEnemies),copy(crntPoints),copy(crntChain),copy(crntPath))
    if not qsl[1]:
        return qsl[0]

    #start the standard bruteforce routine
    seenHPs = []
    HPindex = []
    #gather all different hp amounts in the current enemy list and save their indices
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
    CurrentMaxPath = ""
    for i in HPindex:
           sq = copy(crntEnemies)
           crntPathtemp = crntPath + str(sq[i])
           sq[i]-= crntAttack #applies the damage
           if sq[i] <= 0:
                newChain = crntChain + chainGain
                del sq[i]
           else:
               newChain = crntChain
               
           newpnts = crntPoints + newChain
           t = BruteForce(sq,newpnts,newChain,count,crntPathtemp)
           if CurrentMax < t[0]:
               CurrentMax = t[0]
               CurrentMaxPath = t[1]
    return (CurrentMax,CurrentMaxPath)
from time import sleep
import sys


def progressbar(target):
    x = 99999
    while True:
        sleep(1)
        if Count == x:
            if(input("\ndo you want to quit? (y/n): ") == "y"):
                quit()
        x = Count
        if Count != 0:
            sys.stdout.write("\r" + str(100 * (Count/target)) + "%")
            if Count/target >= 1:
                return

t = perf_counter()
BruteForce([1] * 10,0,0,count=True)
t = perf_counter() - t
cycleCount = t / Count
maxpnts = 0
Count = 0
amount = "a"
while type(amount) != int or amount <= 0:
    try:
        amount = int(input("enter the amount of enemies: "))
    except:
        print("please enter a number over 0.")
   

hp = "a"
while type(hp) != int or hp <= 0:
    try:
        hp = int(input("enter their HP: "))
    except:
        print("please enter a number over 0.")

starting_hp = "a"
while type(starting_hp) != int or starting_hp <= -1:
    try:
        starting_hp = int(input("enter the starting amount of points: "))
    except:
        print("please enter a number over 0.")


chainGain = "a"
while type(chainGain) != int or chainGain <= -1:

    try:
        chainGain = int(input("enter the chain gained from each enemy: "))
    except:
        print("please enter a number over 0.")

import threading

cycleCountEstimate = (hp ** 1.5) ** float(amount)
timeEstimate = cycleCountEstimate * cycleCount
print("time estimation:",timeEstimate)
x = threading.Thread(target=progressbar, args=(cycleCountEstimate,))
x.start()
t = perf_counter()
maxpnts = BruteForce([hp] * amount,starting_hp,0,True)
print("\nmax points  ", maxpnts[0])
print("path: ", maxpnts[1])
t = perf_counter() - t
print("time taken  ",t)
print("-------------")

#BruteForce(deepcopy(squiglets),0,0)

        
