class a_map:
    def __init__(self, grid):
        self.grid = grid


class position(a_map):
    def __init__(self, grid, direction, x, y):
        super().__init__(grid)
        self.x = x
        self.y = y
        self.direction = direction
        
    def move(self):
        match self.direction:
            case "<":
                self.y += -1
            case "^":
                self.x += -1
            case ">":
                self.y += 1
            case "v":
                self.x += 1
                
    def turn(self):
        match self.direction:
            case "<":
                self.direction = "^"
            case "^":
                self.direction = ">"
            case ">":
                self.direction = "v"
            case "v":
                self.direction = "<"
                
    def nextp(self):
        match self.direction:
            case "<":
                return [self.x, self.y - 1]
            case "^":
                return [self.x - 1, self.y]
            case ">":
                return [self.x, self.y + 1]
            case "v":
                return [self.x + 1, self.y]

    def in_map(self, test_point):
        if not(0 <= test_point[0] < len(self.grid)):
            return False
        elif not(0 <= test_point[1] < len(self.grid[1])):
            return False
        else:
            return True

    def block(self, target):
        self.grid[target[0]][target[1]] += "#"
            
    def mark(self):
        self.grid[self.x][self.y] += self.direction
                
    def location(self):
        return [self.x, self.y]

    def at_location(self, test_point):
        return self.grid[test_point[0]][test_point[1]]

    def print_map(self):
        for line in self.grid:
            print(line)
        print("")

