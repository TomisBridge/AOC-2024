class data_string():
    def __init__(self, string, start, end):
        self.string = string
        self.start = start
        self.end = end

    def swap(self):
        first = self.string[self.start]
        self.string = self.string[:self.start] + self.string[self.end] + self.string[self.start + 1:] 
        self.string = self.string[:self.end] + first + self.string[self.end + 1:] 

    def move(self, target):
        if target == "start":
            self.start += 1
        elif target == "end":
            self.end -= 1

    def at(self, target):
        return self.string[target]
        
