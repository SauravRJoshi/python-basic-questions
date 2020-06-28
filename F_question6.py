def num_in_range_check(your_num,your_range):
    if int(your_range[0]) < your_num and int(your_range[-1]) > your_num:
        return "in range"
    else:
        return "outside range"

input_num = int(input("Enter a number : "))
input_range = list(input("Enter the lower limit : "))
input_range.append(input("Enter the upper limit : "))

print("The number",input_num,"is",num_in_range_check(input_num,input_range),input_range)