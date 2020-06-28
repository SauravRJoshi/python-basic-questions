sample_tuple = [('Insight', 4), ('Workshop', 3), ('Assignment', 2), ('Due', 1)]
print("Our sample list of tuples is : ",sample_tuple)
sample_tuple.sort(key = lambda x: x[1])
print("After sorting : ",sample_tuple)