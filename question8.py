def nth_remove(input_str):
    print("Indexing in your string starts from 0 to " + str(len(input_str) - 1) + ' , which index would you like to remove ?')
    print("Please enter a value within your index range 0 to " + str(len(input_str) -1))
    nth_index = int(input())
    input_str.pop(nth_index)
    return input_str


final_str = []
while True:
    input_list = list(input("Enter a non empty string :"))
    if len(input_list) > 0:
        break
final_str = nth_remove(input_list)
print((''.join(final_str)))