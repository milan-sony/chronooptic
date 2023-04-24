from tkinter import *
import datetime
import time
from playsound import playsound
import pyttsx3

"""
--------------------NOTES--------------------

## The work_time value should be in seconds
# formula to convert minute to second - mutiply the time value by 60
# eg: 20 minutes = 1200 seconds
# formula to convert hour to second - multiply the time value by 3600
# eg: 1 hour = 3600 seconds, 1 hour and 30 minutes = 5400 seconds

## The rest_time value should be in milliseconds
# formula to convert second to millisecond - multiply the time value by 1000
# eg: 5 second = 5000 milliseconds
# formula to convert minute to millisecond - multiply the time value by 60000
# eg: 5 minute = 300000 milliseconds

"""

work_time = 5
rest_time = 5000
# work_time = 1200 # 20 minute in second
# rest_time = 20000 # 20 second in millisecond

start_time = datetime.datetime.now()

def start():
  # print("started")
  # print("start time: ", start_time)
  time.sleep(work_time)
  end_time = datetime.datetime.now()
  # print("end time: ", end_time)
  time_diff = end_time - start_time
  # print("time difference:", time_diff)
  time_format(time_diff)

def time_format(time_diff):
  # Define the time as a string
  time_str = str(time_diff)
  # Parse the string to a datetime object
  time_obj = datetime.datetime.strptime(time_str, '%H:%M:%S.%f')
  # Extract hours, minutes, seconds, and milliseconds
  hours = time_obj.hour
  minutes = time_obj.minute
  seconds = time_obj.second
  tts(hours, minutes, seconds)

# text to speech function
def tts(hr, min, sec):
  hours = hr
  minutes = min
  seconds = sec
  engine = pyttsx3.init()
  # getting details of current speaking rate
  engine.setProperty('rate', 200)
  voices = engine.getProperty('voices')
  #changing index, changes voices. o for male
  #changing index, changes voices. 1 for female
  engine.setProperty('voice', voices[0].id)
  engine.say(f"Hey, you have been using this system for {hours} hours {minutes} minutes and {seconds} seconds")
  engine.runAndWait()
  create_window1(hours, minutes, seconds)

# define the function to create the first window
def create_window1(hr, min, sec):
  window1 = Tk()
  hours = hr
  minutes = min
  secs = sec
  window1.attributes("-topmost", 1)
  window1.geometry("600x400")
  window1.title("ALERT | CHRONOOPTIC")
  window1.iconbitmap("./icon2.ico")
  window1.resizable(False, False)
  window1.config(bg="#6886C5")
  playsound('./notification.wav')
  lb1 = Label(
    window1, 
    text="B R E A K T I M E",
    font="Impact 30",
    fg="#F9F9F9",
    bg="#6886C5",
    height=4
  )
  lb1.pack()
  lb2 = Label(
    window1, 
    text=f"You have been using this system for {hours} hours {minutes} minutes and {secs} seconds",
    font=("SegoeUI 10"),
    fg="#F9F9F9",
    bg="#6886C5",
  )
  lb2.pack()
  lb3 = Label(
    window1,
    text="Relax and take some rest",
    font=("Impact 20"),
    fg="#F9F9F9",
    bg="#6886C5",
    height=2
  )
  lb3.pack()
  lb4 = Label(
    window1,
    text="NB: This window will be closed automatically after 20 seconds",
    font=("SegoeUI 10"),
    fg="#F9F9F9",
    bg="#6886C5",
  )
  lb4.pack()
  # start the timer for the next window
  window1.after(rest_time, lambda: next_window(window1, start))
  # redirect to a function if X is clicked
  window1.protocol("WM_DELETE_WINDOW", lambda: next_window(window1, start))
  window1.mainloop()

# define the function to start the next window
def next_window(current_window, next_function):
  # destroy the current window
  current_window.destroy()
  # start the next window
  next_function()

start()