#Create two base classes named clock and calendar. Based on these two classes define a class calendarclock, which inherits from both the classes which displays month details, date and time
class Clock:
    def show_time(self):
        hour = input("Enter hour: ")
        minute = input("Enter minute: ")
        second = input("Enter second: ")
        print("Time:", hour + ":" + minute + ":" + second)


class Calendar:
    def show_date(self):
        day = input("Enter day: ")
        month = input("Enter month: ")
        year = input("Enter year: ")
        print("Date:", day + "/" + month + "/" + year)


class CalendarClock(Clock, Calendar):
    def display(self):
        self.show_date()
        self.show_time()


# Driver code
obj = CalendarClock()
obj.display()