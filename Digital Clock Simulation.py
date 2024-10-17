import time

class Clock():
    def __init__(self, hour, minutes, seconds, clock_type=0):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        self.clock_type = clock_type
    
    def __str__(self):
        if self.clock_type == 1:
            hour_display = self.hour % 12 if self.hour % 12 != 0 else 12
            am_pm = "am" if self.hour < 12 else "pm"
            return f'{hour_display:02d}:{self.minutes:02d}:{self.seconds:02d} {am_pm}'
        else:
            return f'{self.hour:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
                    
clock = Clock(0, 0, 0, 1)

while True:
    try: 
        clock.hour = int(input('What is the current hour ==> '))
        if 0 <= clock.hour <= 23:
            break
        else:
            raise ValueError
    except ValueError:
        print('Please enter an integer between 0 and 23.')

while True:
    try:
        clock.minutes = int(input('What is the current minute ==> '))
        if 0 <= clock.minutes <= 59:
            break
        else:
            raise ValueError
    except ValueError:
        print('Please enter an integer between 0 and 59.')

while True:
    try:
        clock.seconds = int(input('What is the current second ==> '))
        if 0 <= clock.seconds <= 59:
            break
        else:
            raise ValueError
    except ValueError:
        print('Please enter an integer between 0 and 59.')

start_time = time.time()
while time.time() - start_time < 5:
    print(clock)
    clock.tick()
    time.sleep(1)
