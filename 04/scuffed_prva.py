import re

def process(index):
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
            s += process(index + i + 1)
        return s + matching
    if(matching == 0):
        return 0

sum = 1

cards = [0 for i in range(0, 214)]
wins = [0 for i in range(0, 214)]
cards[1] = 1

lines = []
with open("in.txt", "r") as f:
    lines = f.readlines()


max_card = 1
cur_card = 0
for line in lines:
    cur_card += 1
    if(cur_card > max_card):
        break

    if(matching != 0):
        if(max_card < cur_card + matching):
            max_card = cur_card + matching
        for i in range(matching):
            cards[cur_card + i + 1 - 1] += 1
        wins[lines.index(line)] += matching



print(cards)
for i in range(len(cards)):
    sum += cards[i] * wins[i]

print(sum)
