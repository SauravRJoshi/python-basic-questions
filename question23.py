input_list = []
while True:
    a = ''
    a = input("Enter your inputs or press enter : ")
    if a:
        input_list.append(a)
    elif not a:
        break
    
if input_list == []:
    print("Empty")
else:
    print('Not empty')