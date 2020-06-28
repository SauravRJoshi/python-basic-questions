sample_dicts = [{'Insight':'Workshop', 'Class':10,'index':9}, {'start':'1', 'Software':'Engineering', 'mont':1,'index':4}]
print("Sample dictionaries :",sample_dicts)
sorted_dicts = sorted(sample_dicts, key = lambda x: x['index'])
print("\nAfter sorting the dictionaries :",sorted_dicts)