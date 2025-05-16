class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self
    def __next__(self):
        if MyGen.current < self.last:
            result = MyGen.current
            MyGen.current += 1
            return result
        raise StopIteration
gen = MyGen(0,100)
for i in gen:
    print(i) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9