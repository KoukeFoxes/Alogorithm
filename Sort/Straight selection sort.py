def SSS(list: list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i],list[min_index] = list[min_index],list[i]
    
list = [7,5,1,4,3,2,6]
SSS(list)
print(list)