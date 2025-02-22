class data_list():
    def __init__(self, data, start, end):
        self.data = data
        self.start = start
        self.end = end

    def swap(self):
        first = self.data[self.start]
        self.data = self.data[:self.start] + [self.data[self.end]] + self.data[self.start + 1:] 
        self.data = self.data[:self.end] + [first] + self.data[self.end + 1:] 

    def mel(self):
        self.end += -1

    def mer(self):
        self.end += 1
        
    def msl(self):
        self.start += -1
        
    def msr(self):
        self.start += 1

    def at(self, target):
        return self.data[target]
    
    def breakup(self):

        end_len = len(self.data[self.end]) - 1
        start_len = len(self.data[self.start]) - 1

        if end_len < start_len:
            strings = [self.data[self.start][:end_len], self.data[self.start][end_len:]]

            new_start = self.data[:self.start]

            for i in range(len(strings), 0, -1):
                new_start.append(strings[i - 1])

            self.data = new_start + (self.data[self.start + 1:])

