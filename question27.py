first_list = [1,3,5,7,9,10]
second_list = [2,4,6,8]

for i in range(0,len(second_list)):
    first_list.append(second_list[i])
    
print(first_list)