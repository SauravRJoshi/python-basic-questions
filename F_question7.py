def letter_count():
    count_lowercase = 0
    count_uppercase = 0
    input_str = list(input("Enter the string : "))
    for i in input_str:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            count_lowercase += 1
        elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count_uppercase += 1
        
    return count_lowercase,count_uppercase

counts = letter_count()
print("No. of Upper case characters : ",counts[1])
print("No. of Lower case characters : ",counts[0])