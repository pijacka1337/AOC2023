seeds = []

with open("in.txt", "r") as f:
    data = f.readlines()
    seeds = data[0].replace("seeds: ", "").replace("\n", "")
    seeds = seeds.split(" ")
    seeds = [int(x) for x in seeds]
    seeds2 = []
    #print(len(seeds))
    for i in range(0, len(seeds), 2):
        for j in range(seeds[i+1]):
            seeds2.append(seeds[i]+j)
    
    seeds = seeds2

    print(seeds)

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
            temp = []
            maps.append(temp)
            continue
        values = line.replace("\n"," ").split(" ")
        if(values[-1]==''):
            del values[-1]
        #print("val1", values)
        values = [int(x) for x in values]
        #print("val2", values)
        maps[mi].append(values)
    #na koncu fila ni endl in presledka (?)

    #print(maps)
    results = []
    print("tu sem")
    for seed in seeds:
        print(seed)
        cur = seed
        #print(seed)
        for i in range(len(maps)):
            #print(i)
            #print(type(maps[i]))
            f = 0
            for el in maps[i]:
                #print("maps[i] = ", maps[i])
                if(cur >= el[1] and cur < el[1] + el[2]):
                    cur += el[0] - el[1]
                    break
            #print("mapping ", seed, "to", cur)
        #print(cur)
        results.append(cur)

    print(min(results))


