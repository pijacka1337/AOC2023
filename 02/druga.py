with open("02/in1.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    num_red = 12
    num_green = 13
    num_blue = 14
    for line in lines:
        max_red = 0
        max_green = 0
        max_blue = 0
        
        data = line.replace("\n", "").replace(";", "").replace(",", "").split(" ")
        id = int(data[1][:-1])

        for i in range(2, len(data), 2):
            #print(data[i], data[i+1])
            if(data[i+1] == "red"):
                if(int(data[i]) > max_red):
                    max_red = int(data[i])
            if(data[i+1] == "green"):
                if(int(data[i]) > max_green):
                    max_green = int(data[i])
            if(data[i+1] == "blue"):
                if(int(data[i]) > max_blue):
                    max_blue = int(data[i])
        sum += max_red * max_green * max_blue

        print(id, max_red, max_green, max_blue)    

    print(sum)
