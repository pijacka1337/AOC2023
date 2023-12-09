import re

times = []
records = []

with open("in.txt", "r") as f:
    lines = f.readlines()
    times = lines[0].replace("Time:", "").replace("\n", "").replace(" ", "")
    records = lines[1].replace("Distance:", "").replace("\n", "").replace(" ", "")
    times = int(times)
    records = int(records)

print(times)
print(records)

result = 1
for i in range(1):
    wins = 0
    for j in range(times):
        v = j
        t = times - j
        if(v*t > records):
            wins += 1
    result *= wins

print(result)
    
