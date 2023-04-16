from time import sleep


# work time is in minutes
work_time = 1
# rest time in in seconds
rest_time = 20


# function to convert minute to second
def convert_minute_to_second():
  second = work_time * 60
  return second


def tracker():
  worktime = convert_minute_to_second()
  while worktime:
    # timer
    mins, secs = divmod(worktime, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    sleep(1)
    worktime -= 1
  sleep(worktime)
  print("You have been working for 1 min")

tracker()