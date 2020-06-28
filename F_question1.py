def find_max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "NONE, because max inputs are equal."

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your third number : "))

print("Your inputs are : ",num1,' ,',num2,' ,',num3)
print('The max of the three inputs is : ',find_max(num1,num2,num3))