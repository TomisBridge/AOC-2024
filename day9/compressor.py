class data_list():
    def __init__(self, data, start, end):
        self.data = data
        self.start = start
        self.end = end

    def swap(self):
        first = self.data[self.start]
        self.data = self.data[:self.start] + [self.data[self.end]] + self.data[self.start + 1:] 
        self.data = self.data[:self.end] + [first] + self.data[self.end + 1:] 

    def move(self, target):
        if target == "start":
            self.start += 1
        elif target == "end":
            self.end -= 1

    def at(self, target):
        return self.dat[target]
        
