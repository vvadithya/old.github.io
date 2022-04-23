# Necessary Modules
from pyautogui import screenshot
import PySimpleGUI as sg
from os import chdir
import time
# Theme
sg.theme("TealMono")


layouts = [
    [sg.Text('Made By Adithya')],
    [sg.FolderBrowse('Select where you want to save the image' , key='file')],
    [sg.Text('Enter the Delay:')],
    [sg.InputText(key='delay')],
    [sg.Text('Enter the name of the file:')],
    [sg.InputText(key='name')],
    [sg.Button('Take a Screen Shot')]

]

window = sg.Window('Screen Shot taker', layouts , size=(600,600) , resizable=True)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Take a Screen Shot':
        path = values['file']
        delay = values['delay']
        delay = int(delay)
        name = values['name']
        data = name + '.jpg'
        chdir(path)
        time.sleep(delay)
        screenshot(data)

window.close()

