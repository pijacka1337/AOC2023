import functools

def isFiveOfAKind(a):
    if a[0] == a[1] == a[2] == a[3] == a[4]:
        return True
    else:
        return False

def isFourOfAKind(a):
    if a[0] == a[1] == a[2] == a[3]:
        return True
    elif a[1] == a[2] == a[3] == a[4]:
        return True
    else:
        return False

def isFullHouse(a):
    if a[0] == a[1] == a[2] and a[3] == a[4]:
        return True
    elif a[0] == a[1] and a[2] == a[3] == a[4]:
        return True
    else:
        return False

def isThreeOfAKind(a):
    if a[0] == a[1] == a[2]:
        return True
    elif a[1] == a[2] == a[3]:
        return True
    elif a[2] == a[3] == a[4]:
        return True
    else:
        return False

def isTwoPair(a):
    if a[0] == a[1] and a[2] == a[3]:
        return True
    elif a[0] == a[1] and a[3] == a[4]:
        return True
    elif a[1] == a[2] and a[3] == a[4]:
        return True
    else:
        return False

def isOnePair(a):
    if a[0] == a[1]:
        return True
    elif a[1] == a[2]:
        return True
    elif a[2] == a[3]:
        return True
    elif a[3] == a[4]:
        return True
    else:
        return False

def highCard(a,b):
    if a > b:
        return 1
    if a < b:
        return -1
    if a == b:
        return 0



def compare(arra, arrb):
    a = arra[0]
    b = arrb[0]
    a = ''.join(sorted(a, reverse=True))
    b = ''.join(sorted(b, reverse=True))


    if(isFiveOfAKind(a) and isFiveOfAKind(b)):
        return highCard(arra[0],arrb[0])
    if(isFiveOfAKind(a) and not isFiveOfAKind(b)):
        return 1
    if(not isFiveOfAKind(a) and isFiveOfAKind(b)):
        return -1
    
    if(isFourOfAKind(a) and isFourOfAKind(b)):
        return highCard(arra[0],arrb[0])
    if(isFourOfAKind(a) and not isFourOfAKind(b)):
        return 1
    if(not isFourOfAKind(a) and isFourOfAKind(b)):
        return -1
    
    if(isFullHouse(a) and isFullHouse(b)):
        return highCard(arra[0],arrb[0])
    if(isFullHouse(a) and not isFullHouse(b)):
        return 1
    if(not isFullHouse(a) and isFullHouse(b)):
        return -1
    
    if(isThreeOfAKind(a) and isThreeOfAKind(b)):
        return highCard(arra[0],arrb[0])
    if(isThreeOfAKind(a) and not isThreeOfAKind(b)):
        return 1
    if(not isThreeOfAKind(a) and isThreeOfAKind(b)):
        return -1
    
    if(isTwoPair(a) and isTwoPair(b)):
        return highCard(arra[0],arrb[0])
    if(isTwoPair(a) and not isTwoPair(b)):
        return 1
    if(not isTwoPair(a) and isTwoPair(b)):
        return -1
    
    if(isOnePair(a) and isOnePair(b)):
        return highCard(arra[0],arrb[0])
    if(isOnePair(a) and not isOnePair(b)):
        return 1
    if(not isOnePair(a) and isOnePair(b)):
        return -1
    
    return highCard(arra[0],arrb[0])


with open("in.txt") as f:
    lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace("T", "a").replace("J", "b").replace("Q", "c").replace("K", "d").replace("A", "e")
        lines[i] = lines[i].strip("\n").split(" ")


    lines = sorted(lines, key=functools.cmp_to_key(compare))

    res = 0
    for i in range(len(lines)):
        res += (i+1) * int(lines[i][1])
    
    print(lines)
    print(res)

    
