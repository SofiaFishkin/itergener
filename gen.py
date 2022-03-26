def flat_generator(nested_list): 
    for a in sum(nested_list,[]):
        yield a

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i'],
]
for item in  flat_generator(nested_list):
	print(item)