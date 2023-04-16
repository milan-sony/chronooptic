from time import sleep
from notifypy import Notify


# work time is in minutes
work_time = 1
# rest time in in seconds
rest_time = 20


# function to convert minute to second
def convert_minute_to_second():
  second = work_time * 60
  return second


# function to display desktop notification
def notification(message):
  notification = Notify()
  notification.application_name = "CHRONOOPTIC"
  notification.title = "Remainder"
  notification.message = str(message)
  notification.icon = "./icon.png"
  notification.audio = "./notificationsound.wav"
  notification.send()

# function to track work_time
def minute_checker():
  worktime = convert_minute_to_second()
  while worktime:
    # timer
    mins, secs = divmod(worktime, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    sleep(1)
    worktime -= 1
  sleep(worktime)
  message = f"You have been using this system for {work_time} minute"
  notification(message)

minute_checker()