class FlatIterator:
    def __init__(self, collection) -> None:
        self.collection = collection
        self.current = 0
        self.inner_current = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.current <= len(self.collection):
                next_list = self.collection[self.current]
                if self.inner_current == len(next_list):
                    self.inner_current = 0
                    self.current += 1
                next_val = self.collection[self.current][self.inner_current]
                self.inner_current += 1
                return next_val
        except:
            raise StopIteration

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


for item in FlatIterator(nested_list):
    print(item) #


print([v for v in FlatIterator(nested_list)])

