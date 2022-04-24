from ctypes.wintypes import RGB
from tkinter import Image
import PySimpleGUI as ps

ps.theme("")

layout = [[ps.Text("Min andra gui")],
          [ps.Input (key = "-IN-")],
          [ps.Button("ok"), ps.Button("avsluta")],
          [ps.CloseButton("KILL KILL KILL KILL")],
          [Image("C:\Users\jacob.hell\Desktop\python\pygame&pysimplegui\maxresult.jpg")]]

window = ps.Window("window", layout)

while True :
    event, values = window.read()
    print(event, values)

    if event in (None, "avsluta") :
        break

window.close()