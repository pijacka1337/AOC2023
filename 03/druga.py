field = []
sum = 0

with open("in.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        field.append(line.strip("\n"))

options = []
for n in range(-1,2):
    for m in range(-1,2):
        options.append([n,m])


for i in range(len(field)):
    for j in range(len(field[i])):
        if(field[i][j] == '*'):
            nums = []
            used = []
            for o in options:
                try:
                    if(field[i+o[0]][j+o[1]].isdigit() and [i+o[0],j+o[1]] not in used):
                        #print("i = ", i, "j = ", j, "o = ", o)
                        cur_num = field[i+o[0]][j+o[1]]
                        used.append([i+o[0],j+o[1]])
                        try:
                            k=1
                            while(field[i+o[0]][j+o[1]+k].isdigit() and [i+o[0],j+o[1]+k] not in used):
                                cur_num += field[i+o[0]][j+o[1]+k]
                                used.append([i+o[0],j+o[1]+k])
                                k += 1
                        except:
                            pass
                        try:
                            k=1
                            while(field[i+o[0]][j+o[1]-k].isdigit() and [i+o[0],j+o[1]-k] not in used):
                                cur_num = field[i+o[0]][j+o[1]-k] + cur_num
                                used.append([i+o[0],j+o[1]-k])
                                k += 1
                        except:
                            pass
                    
                        #print("cur_num = ", cur_num)
                        nums.append(int(cur_num))
                except:
                    pass
            if(len(nums) == 2):
                sum += nums[0] * nums[1]
print(sum)
