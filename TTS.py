import tkinter 
from tkinter import filedialog
from tkinter import *

from path import Path
import pyttsx3
import os
from time import sleep


def text_to_speech(): #basically this code segment opens a new window, and gives you a place to type in the string you want to convert to speech (Pops up after you press 'Convert Text to Speech')

    global textBox
    wn1 = tkinter.Tk() 
    wn1.title("Text to Speech converter")
    wn1.geometry('500x500')
    wn1.config(bg='Ivory')
    
    Label(wn1, text='Text to Speech converter',fg='black', font=('Montserrat', 15)).place(x=130, y=10)
    
    v=Scrollbar(wn1, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    textBox=Text(wn1, font=("Calibre, 14"), yscrollcommand=v.set)
    textBox.focus()
    textBox.place(x=20, y=80,width=450,height=300)
    
    v.config(command=textBox.yview)
    Button(wn1, text="Convert", bg='ivory3',font=('Montserrat', 13),command=speak).place(x=230, y=400)
    
    wn1.mainloop()

def speak(): #this code segment makes the program to dictate the entered text after converting it from tect to speech
    global textBox
    text=textBox.get(1.0, "end-1c")
    voiceEngine.say(text)
    voiceEngine.runAndWait()
    voiceEngine.setProperty('rate', 50)
    

voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)
rate=voiceEngine.getProperty('rate')


wn = tkinter.Tk() 
wn.title("Text to Speech Converter")
wn.geometry('700x150')
wn.config(bg='LightBlue')
  
Label(wn, text='Text to Speech Converter', fg='Black', font=('Montserrat', 15)).place(x=225, y=10)

global textBox,showText,command
go=1

Button(wn, text="Convert Text to Speech", bg='LightGrey',font=('Montserrat', 15),command=text_to_speech).place(x=230, y=80)

wn.mainloop()



