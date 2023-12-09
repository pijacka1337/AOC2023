seeds = []

with open("in.txt", "r") as f:
    data = f.readlines()
    seeds = data[0].replace("seeds: ", "").replace("\n", "")
    seeds = seeds.split(" ")
    seeds = [int(x) for x in seeds]
    mi = -1
    maps = []
    del data[0]
    for line in data:
        #print([x for x in line][-5:-1])
        #print(line)
        if(line=="\n"):
            continue
        if(line[-5:-1]=="map:"):
            #print("bla")
            mi += 1
            temp = {}
            maps.append(temp)
            continue
        values = line.replace("\n"," ").split(" ")
        if(values[-1]==''):
            del values[-1]
        #print("val1", values)
        values = [int(x) for x in values]
        #print("val2", values)
        src = values[0]
        dest = values[1]
        l = values[2]
        for i in range(l):
            maps[mi][dest+i] = src+i
    #na koncu fila ni endl in presledka (?)

    #print(maps)
    results = []

    for seed in seeds:
        cur = seed
        print(seed)
        for i in range(len(maps)):
            #print(i)
            #print(type(maps[i]))
            if(cur in maps[i]):
                cur = maps[i][cur]
            #print("mapping ", seed, "to", cur)
        #print(cur)
        results.append(cur)

    print(min(results))


