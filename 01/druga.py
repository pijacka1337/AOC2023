words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("01/in2.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        for i in range(len(line)):
            if(line[i].isdigit()):
                first_num = i
                break
        for i in range(len(line)):
            if(line[len(line)-1-i].isdigit()):
                last_num = len(line)-1-i
                break
        first_word = {}
        last_word = {}
        for word in words:
            if word in line:
                first_word[word] = line.index(word)
                last_word[word] = line.rindex(word)
                break
        
        print(first_word)
        print(last_word)

        if(first_word == {}):
            first = line[first_num]
        else:
            if(first_num < max(first_word.values())):
                first = line[first_num]
            else:
                max_key = max(first_word, key=first_word.get)
                first = words.index(max_key) + 1
        
        print(first)
        
        
    print(sum)
