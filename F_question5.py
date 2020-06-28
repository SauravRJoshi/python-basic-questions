def find_fact(your_input):
    fact = 1
    for i in range(1,your_input+1):
        fact *= i
    return fact    

input_number = int(input("Enter the number to find the factorial : "))

print('The factorial of ',input_number,' is ',find_fact(input_number))