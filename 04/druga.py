import re

with open("in.txt", "r") as f:
    lines = f.readlines()

processed = [-1 for i in range(len(lines))]

def process(index):
    if(processed[index] != -1):
        return processed[index]
    if(index >= len(lines)):
        return 0
    line = lines[index]
    data = line.strip("\n").split("|")
    win = re.split(r" {1,}", data[0])
    del win[0]
    del win[0]
    del win[-1]
    win = [int(element) for element in win]
    #print(win)
    nums = re.split(r" {1,}", data[1])
    del nums[0]
    nums = [int(element) for element in nums]
    #print(nums)
    matching = 0
    for num in nums:
        if num in win:
            matching += 1
    if(matching != 0):
        s = 0
        for i in range(matching):
            #print("processing ", index + i + 1)
            s += process(index + i + 1)
        processed[index] = s + matching
        return s + matching
    if(matching == 0):
        return 0





sum = 0

for i in range(len(lines)):
    t = process(i)
    #print("processing ", i+1, "=", t)
    sum += t

print(sum + len(lines))
