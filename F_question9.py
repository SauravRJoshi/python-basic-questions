def find_prime(num1):
    for i in range(2,num1):
        if i%2 == 0:
            return 'prime'
            print(i)
        else:
            return "not prime"    

print(find_prime(int(input("Enter a number : "))))