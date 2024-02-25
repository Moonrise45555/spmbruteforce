import math

count = 0
score = int(input("Enter your starting score:"))
frames = 0

while score < 99999999:
    count += 1
    score += (count * 10)
    frames += 58

level = (score ** 0.5)/50
level = math.ceil(level)

frames += (level-1) * 46
hours = (frames // 216000)
minutes = (frames // 3600) % 60
seconds = (frames % 3600)/60

if score >= 99999999:
    score = 99999999

if 0 <= score <= 9999:
    level = 1

if level >= 99:
    level = 99

time = str(hours) + ":" + str(minutes) + ":" + str("%.2f" % seconds)

print(count, "Bounces | Score:", score, "| Time Elapsed:", time)