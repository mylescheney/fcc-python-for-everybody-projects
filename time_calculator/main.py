from time_calculator import add_time

start_time = input("Type the start time in hh:mm format > ")
am_or_pm = input("Type either AM of PM > ")
start_day = input("What day of the week does it begin on? > ")
duration = input("How long does the even last, in hh:mm format > ")

print(add_time(start_time + " " + am_or_pm, duration, start_day))