count = 0
input_list = []

input_list = []
while True:
    a = ''
    a = input("Enter a string or press enter : ")
    if a:
        input_list.append(a)
    elif not a:
        break

for element in input_list:
    if len(element) >= 2 :
        if element[0] == element[-1]:
            count += 1
            
print("Your list : ",input_list)
print("The repeated ones are ",count)
