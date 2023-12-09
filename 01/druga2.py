with open("01/in1.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
        print(line)
        for i in range(len(line)):
            if(line[i].isdigit()):
                first = line[i]
                break
        for i in range(len(line)):
            if(line[len(line)-1-i].isdigit()):
                last = line[len(line)-1-i]
                break
        print(first, last)
        sum += 10*int(first) + int(last)
    print(sum)
