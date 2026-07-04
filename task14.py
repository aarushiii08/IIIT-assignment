# to convert milisec to hour , minutes and seconds.
def time(milisecond):
    total_second = milisecond // 1000
    hour = total_second // 3600
    minutes = (total_second % 3600) // 60
    seconds = total_second % 60
    print(hour,"hour(s)",minutes,"minute(s)",seconds,"second(s)")
milisecond = int(input("enter milisecond = "))
time(milisecond) 