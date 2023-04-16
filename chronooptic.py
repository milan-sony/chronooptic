from time import sleep
from notifypy import Notify
import pyttsx3
import webbrowser
import pyautogui


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


# open web browser function
def web():
  try:
    webbrowser.open_new_tab("index.html")
    flag = 1
    if flag == 1:
      sleep(rest_time)
      pyautogui.hotkey('ctrl', 'w')
      sleep(0.5)
      pyautogui.hotkey('alt', 'tab')
      minute_checker()
  except webbrowser.Error:
    message = "Someting went wrong with the browser"
    notification(message)

# text to speech function
def tts():
  engine = pyttsx3.init()
  # getting details of current speaking rate
  engine.setProperty('rate', 200)
  voices = engine.getProperty('voices')
  #changing index, changes voices. o for male
  #changing index, changes voices. 1 for female
  engine.setProperty('voice', voices[0].id)
  engine.say(f"Hey, you have been using this system for {work_time} minute. Relax and take some rest")
  engine.runAndWait()

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
  tts()

minute_checker()