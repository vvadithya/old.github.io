# Importing necessary modules
import PySimpleGUI as sg
from os import chdir , listdir
import moviepy.editor 
# Defining main functions

    

    
layout = [
    [sg.Text('Made By Adithya')],
    [sg.Text('Input Folder:')],
    [sg.FolderBrowse('Select the folder' , key='input_files')],
    [sg.Text("Output Folder:")],
    [sg.FolderBrowse("Select the folder" , key='output_files')],
    [sg.Button('Convert .mp4 to .mp3')]
    ]

window = sg.Window('MP3 Converter', layout , size=(600,600) , resizable=True)
def convert_files(x,y):
    chdir(x)
    list_of_files = listdir()
    files_to_convert = []
    for file in list_of_files:
        if file.endswith('.mp4'):
            files_to_convert.append(file)
    # print(files_to_convert) 
    for video in files_to_convert:
        name = video.replace('.mp4' , '')
        video_file = moviepy.editor.VideoFileClip(video)
        audio = video_file.audio
        name = name + '.mp3'
        chdir(y)
        audio.write_audiofile(name)  
        chdir(x)      

        
    

while True:
    event, values = window.read() 
    input_path = values['input_files']
    output_path = values['output_files']
    if event == 'Convert .mp4 to .mp3':
        convert_files(input_path , output_path)
        layout2 = [
        [sg.Text('Completed,Enjoy!')]    
        ]   
        window = sg.Window('Done', layout2 , resizable=True) 
        
            
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    

window.close()