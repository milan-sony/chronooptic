from tkinter import *

def create_window1():
  window1 = Tk()
  hours = 0
  minutes = 20
  secs = 0
  window1.attributes("-topmost", 1)
  window1.geometry("600x400")
  window1.title("ALERT | CHRONOOPTIC")
  window1.iconbitmap("./icon.ico")
  window1.resizable(False, False)
  window1.config(bg="#6886C5")
  # playsound('./notification.wav')
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
  window1.mainloop()

create_window1()