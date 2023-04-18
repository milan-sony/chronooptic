import datetime
import time
from notifypy import Notify
import pyttsx3

start_time = datetime.datetime.now()

def notification(message):
  timediff = message
  notification = Notify()
  notification.application_name = "CHRONOOPTIC"
  notification.title = "Remainder"
  notification.message = f"You have been using this system for {timediff}"
  notification.icon = "./icon.png"
  notification.audio = "./notificationsound.wav"
  notification.send()

def display1():
  print("Alert of 20 min")
  counter()

def display2():
  print("Alert of 1 hr")
  timefn()

time_count = 1
def counter():
  global time_count
  time_count += 1
  print(time_count)
  if time_count <= 2:
    timefn()
  else:
    time_count = 1
    display2()


def tts(message):
  timediff = message
  engine = pyttsx3.init()
  # getting details of current speaking rate
  engine.setProperty('rate', 200)
  voices = engine.getProperty('voices')
  #changing index, changes voices. o for male
  #changing index, changes voices. 1 for female
  engine.setProperty('voice', voices[0].id)
  engine.say(f"Hey, you have been using this system for{timediff}. Relax and take some rest")
  engine.runAndWait()
  display1()

def timefn():
    print("start time: ", start_time)
    time.sleep(60)
    end_time = datetime.datetime.now()
    print("end time: ", end_time)
    time_diff = end_time - start_time
    print("Time difference:", time_diff)
    alert = time_diff
    notification(alert)
    tts(alert)

timefn()