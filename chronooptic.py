from time import sleep
from notifypy import Notify
import pyttsx3
import webbrowser
import pyautogui

# work time is in minutes
work_time = 1
# rest time in in seconds
rest_time = 20
# flag = 0

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
  notification.audio = "./notification.wav"
  notification.send()

# open web browser function
def webpage1():
  try:
    webbrowser.open_new_tab("page1.html")
    flag = 1
    if flag == 1:
      sleep(rest_time)
      pyautogui.hotkey('ctrl', 'w')
      sleep(0.5)
      pyautogui.hotkey('alt', 'tab')
      hour_checker()
  except webbrowser.Error:
    message = "Someting went wrong with the browser"
    notification(message)

def webpage2():
  try:
    webbrowser.open_new_tab("page2.html")
    flag = 1
    if flag == 1:
      # 15 min = 900 sec
      sleep(rest_time)
      pyautogui.hotkey('ctrl', 'w')
      sleep(0.5)
      pyautogui.hotkey('alt', 'tab')
      minute_checker()
  except webbrowser.Error:
    message = "Someting went wrong with the browser"
    notification(message)

time_count = 1

def hour_checker():
  global time_count
  time_count += 1
  print(time_count)
  if time_count <=2:
    minute_checker()
  else:
    time_count = 1
    webpage2()

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
  webpage1()

# function to track work_time
def minute_checker():
  worktime = convert_minute_to_second()
  sleep(worktime)
  message = f"You have been using this system for {work_time} minute"
  notification(message)
  tts()

minute_checker()