input_str = input("Enter a string : ")
sample_list = [1,2,3,4]

for i in range(0,len(sample_list)):
    sample_list[i] = input_str + str(sample_list[i])

print(sample_list)