class data_list():
    def __init__(self, data, start, end):
        self.data = data
        self.start = start
        self.end = end

    def swap(self):
        if len(self.start)
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

    def breakup(self, string, i):
        strings = [string[:i], string[i:]]

        def insall(self, break_string):
            for i in range(len(break_string)):
                new_start = self.data[:self.start - 1].append(break_string[i])
            return new_start


