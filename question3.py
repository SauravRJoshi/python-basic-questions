def change_string(user_string):
    list1 = []
    for i in user_string:
        if i == user_string[0]:
            i = '$'
            list1.append(i)
        else:
            list1.append(i)
    list1[0] = user_string[0]
    return list1


user_string = list(input("Enter your string : "))
final_string = ''.join(change_string(user_string))
print(final_string)