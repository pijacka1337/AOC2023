import re

times = []
records = []

with open("in.txt", "r") as f:
    lines = f.readlines()
    times = lines[0].replace("Time:", "").replace("\n", "")
    times = re.split(r" {1,}", times)[1:]
    records = lines[1].replace("Distance:", "").replace("\n", "")
    records = re.split(r" {1,}", records)[1:]

times = [int(x) for x in times]
records = [int(x) for x in records]

print(times)
print(records)

result = 1
for i in range(len(times)):
    wins = 0
    for j in range(times[i]):
        v = j
        t = times[i] - j
        if(v*t > records[i]):
            wins += 1
    result *= wins

print(result)
    
