import math

count = 0
score = int(input("Enter your starting score:"))
target = int(input("Enter the target score:"))
frames = 0

startlevel = (score ** 0.5)/50
startlevel = math.ceil(startlevel)

if score <= 9999:
    startlevel = 1

while score < target:
    count += 1
    score += (count * 10)
    frames += 58

if score >= 99999999:
    score = 99999999

level = 0
if score <= 9999:
    level = 1

if level >= 99:
    level = 99
    
level = (score ** 0.5)/50
level = math.ceil(level)

frames += (level-startlevel) * 46
hours = (frames // 216000)
minutes = (frames // 3600) % 60
seconds = (frames % 3600)/60

if 0 <= seconds <= 9:
    seconds = "0" + str("%.2f" % seconds)
else:
    seconds = str("%.2f" % seconds)

if 0 <= minutes <= 9:
    minutes = "0" + str(minutes)

time = str(hours) + ":" + str(minutes) + ":" + seconds

print(count, "Bounces | Score:", score, "| Time Elapsed:", time)