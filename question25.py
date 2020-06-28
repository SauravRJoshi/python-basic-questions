sample_list1 = [{},{},{},{},{}]
sample_list2 = [{1,2},{},{}]

print("First list :",sample_list1)
print("Second list :",sample_list2)

count1 = 0
for i in range(0,len(sample_list1)):
    if not sample_list1[i]:
        pass
    else:
        count1 = count1+1
        
count2 = 0
for j in range(0,len(sample_list2)):
    if not sample_list2[j]:
        pass
    else:
        count2 = count2+1

        
        
if count1 == 0:
    print("The dictionaries in the first list are empty")
else:
    print("The dictionaries in the first list are not empty")

if count2 == 0:
    print("The dictionaries in the second list are empty")
else:
    print("The dictionaries in the second list are not empty")