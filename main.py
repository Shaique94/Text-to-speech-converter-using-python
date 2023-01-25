import tkinter as tk
from tkinter import *
import pyttsx3

engine = pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()







root = Tk()
#written for line number 17
textv = StringVar()
#main text with frame 
obj = LabelFrame(root,text="Text to speech",font=15,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

#inside text before the box
lbl = Label(obj, text="Text",font=20)
lbl.pack(side=tk.LEFT,padx=5)

#getting box to enter the words
text = Entry(obj,textvariable=textv,font=25,width=20,bd=3)
text.pack(side=tk.LEFT,padx=10)

#button
btn= Button(obj, text="Speak",bg="green",fg="black",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)

#creating a frame
root.title("Text to Speech converter")
root.geometry("400x300")
root.resizable(False,False)
root.mainloop()