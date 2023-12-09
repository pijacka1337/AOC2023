with open("01/in1.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        for i in range(len(line)):
            if(line[i].isdigit()):
                first = line[i]
                break
        for i in range(len(line)):
            if(line[len(line)-1-i].isdigit()):
                last = line[len(line)-1-i]
                break
        sum += 10*int(first) + int(last)
    print(sum)
