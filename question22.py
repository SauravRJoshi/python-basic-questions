input_list = []
while True:
    a = ''
    a = input("Enter your inputs or press enter : ")
    if a:
        input_list.append(a)
    elif not a:
        break

print("Your input list is : ",input_list)
print("The list with duplicates removed is :",set(input_list))