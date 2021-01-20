import os
from datetime import datetime
import tkinter as tk


import tkinter as tk 


window = tk.Tk()

window.title("ULTRA-FAIRWORKER")

window.geometry('300x200')


title = tk.Label(text="Hallo Ludolf")
title.grid()






images = [] # List in witch all images are stored with there full path as a string
renamed = 0 

#Path of the demo directory
fairworker_path = '/Users/renekuhn/Downloads/Demo/Fairworker/'
project_path = '/Users/renekuhn/Downloads/Demo/Projekte/'

# Function witch gets all new images and stores them in the images list
def get_images(fairworker_path):
    for subdirectories, directories,files in os.walk(fairworker_path):

        for file_name in files :
            file_loc = subdirectories + os.path.sep + file_name
            #adding .png and .jpg files to the images list
            if file_loc.endswith(".png") or file_loc.endswith(".jpg"):
                images.append(file_loc)
    print("All images are in the List now") 

#Function witch renames all images in the list 
def rename_images(project_path):
    global renamed
    os.chdir(project_path)
    for image in images : 
        all_parts = []
        path = os.path.normpath(image)
        path = path.split(os.sep)
        all_parts.append(path)
        creator = all_parts[0][6]
        project = all_parts[0][7]
        full_doc_path,filetype = os.path.splitext(all_parts[0][8])
        day_created =(datetime.utcfromtimestamp(os.path.getctime(image)).strftime('%Y-%m-%d'))
        renamed += 1
        new_path = project+'/'+day_created+'-'+creator+str(renamed)+filetype
        os.rename(image,new_path)
    print(f"All {renamed} Images are renamed and moved to the new location")

def run():
    get_images(fairworker_path)
    rename_images(project_path)
    print("Great job")
    

button1 = tk.Button(text="Feuer Frei!", bg="red",command=run)
button1.grid(column=0,row=2)

window.mainloop()