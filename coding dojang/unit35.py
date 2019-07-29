class Time:
    
    
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return cls(hour, minute, second)
        
        
    @staticmethod
    def is_time_valid(time_string):
        a, b,c = list(map(int, time_string.split(':')))
        if a <25 and b <60 and c <61:
            return True

time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
