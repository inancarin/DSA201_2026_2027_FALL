class Clock:
    def __init__(self, hour, minute, second):
        self.h = hour
        self.m = minute
        self.s = second
    
    def __str__(self):
        hour = str(self.h) 
        if len(hour) == 1:
            hour = "0" + hour
        minute = str(self.m)
        if len(minute) == 1:
            minute = "0" + minute
        second = str(self.s)
        if len(second) == 1:
            second = "0" + second
    
        return hour + ":" + minute + ":" + second
    
    def tick(self):
        self.s += 1
        if self.s == 60:
            self.s = 0
            self.m += 1
            if self.m == 60:
                self.m = 0
                self.h += 1
                if self.h == 24:
                    self.h = 0