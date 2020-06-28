#!/usr/bin/python3
def get_string(first,second,second_last,last):
    final_string = str(first) + str(second) + str(second_last) + str(last)
    return final_string

your_string = list(input("Enter your string :"))
if len(your_string) >= 2:
    final = get_string(your_string[0],your_string[1],your_string[-2],your_string[-1])
else:
    final = ""

print(final)