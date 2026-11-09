class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.xUpper = x1
        self.yUpper = y1
        self.xLower = x2
        self.yLower = y2
        self.side1 = abs(self.xUpper - self.xLower)
        self.side2 = abs(self.yUpper - self.yLower)
    
    def __str__(self): # must always returns a string to be printed
        rect = ""
        rect += self.side1 * "*" + "\n"
        for i in range(self.side2-2):
            rect += "*" + " " * (self.side1 - 2) + "*\n"
        
        rect += self.side1 * "*" + "\n"
        return rect

    def calculateArea(self):
        return self.side1 * self.side2
    
    def calculatePerimeter(self):
        return 2 * (self.side1 + self.side2)