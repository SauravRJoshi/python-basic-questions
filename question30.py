dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144,13: 169, 14: 196, 15: 225}
print("Our sample dictionary is :",dict1)
if int(input("\nEnter a number to check if its in our sample dictionary ")) in dict1.keys():
    print("Key already exists")
else:
    print("Key doesn't exist inside dictionary")