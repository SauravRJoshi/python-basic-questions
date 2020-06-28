input_list = []
while True:
    a = ''
    a = input("Enter your inputs or press enter : ")
    if a:
        input_list.append(a)
    elif not a:
        break
    
    copy_list = []
for i in input_list:
    copy_list.append(i)

print("Your input list is : ",input_list)
print("Your copied list is : ",copy_list)