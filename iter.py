class Iterator:
    def __init__(self, nested_list):
        self.collection = nested_list
    
    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.collection):
            raise StopIteration
        element = self.collection[self.cursor]
        return element

nested_list =[
 ['a', 'b', 'c'],
 ['d', 'e', 'f'],
 ['g', 'h', 'i'],
]

for item in Iterator(nested_list):
    print(item)