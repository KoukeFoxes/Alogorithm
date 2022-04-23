def SIS(list: list) -> list:
    for j in range(1,len(list)):
        # print(list)
        i = j - 1
        x = list[j]
        while x < list[i] and i >= 0:
            list[i+1] = list[i]
            i -= 1
        list[i+1] = x
    
    return list

print(SIS([7,5,1,4,3,2,6]))        