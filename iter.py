
from itertools import chain
from typing import Collection

nested_list =[
 ['a', 'b', 'c'],
 ['d', 'e', 'f'],
 ['g', 'h', 'i'],
]
nested_list=list(chain(* nested_list))

class Iterator:
    def __init__(self, collection):
        self.collection = collection
    
    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.collection):
            raise StopIteration
        element = self.collection[self.cursor]
        return element

for item in Iterator(nested_list):
    print(item)