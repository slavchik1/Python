class Clock():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def show_time(self):
        print(str(self.hours) + ":" + str(self.minutes))

    def add_minutes(self, minutes):
        self.minutes += minutes
        self.hours += minutes // 60
        self.minutes %= 60
        self.hours %= 24

clock = Clock(10, 50)
clock.show_time()  # 10:50
clock.add_minutes(100)
clock.show_time()  # 11:10