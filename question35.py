dict1={1:10, 2:20,3:30, 4:40,5:50,6:60}
print("Our dictionary :",dict1)
a=0
b=0
for items in dict1.items():
    print("key",a,":","value",b,"->",items)
    a+=1
    b+=1