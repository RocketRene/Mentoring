# My first Python Program 

### Whats my Skill Level ?

Until I started working with a mentor I learned Python myself mostly with the book _Learn Python 3 the Hard Way_ and _Python for Everybody_ on Youtube. I haven't  finised one of them, because I made the mistake to switch my learning recourses insead of sticking to one. Only my Mentor told me to stop doing one exercice after the other and use what I have learned so far and apply it to my own project I stared feeling like a programmer who is solving problems. 
### What Problem can I solve with my really basic skills ?
I thought about my old boss who is almost 60, he runs a small constuction business with round about 10 construction workers and two people in the office. All of his so called Fairworkers use their smartphones to take pictures of the constuction site and upload them in a Dropbox folder every day. I remember how much time Ludolf, my old boss is investing to check each folder, rename all of these pictures every morning and move them in the right folder. He does that for a lot of pictures, every single workday, and without any shortcut. I don't want to know how much of his valuble lifetime went into renaiming images during the last 20 Years. This is a great task that can be automated with Python, I thought.
### What variables, lists, loops and operations do I need for that ?
Let's Imagine a folder Stucture like this : 
- Dropbox
    - **Upload Folders**
        - _Fair Worker 1_
            - Construction Site A
                - Image123.jpg
                - Image123.jpg
                - Image123.jpg
            - Construction Site B
                - Image123.jpg
                - Image123.jpg
                - Image123.jpg
            - Construction Site C             
        - _Fair Worker 2_ 
            - Construction Site A
                - Image123.jpg
                - Image123.jpg

            - Construction Site B
            - Construction Site C
        - _Fair Worker 3_
            - Construction Site A
            - Construction Site B
            - Construction Site C
                - Image123.jpg
                - Image123.jpg
            
    - **Project Folders**
        - Construction Site A
        - Construction Site B
        - Construction Site C


So Let's start by importing the modules we need 

```python
import os 
from datetime import datetime
import tkinter as tk
```
Then we create the List called **images** and initialize the counter variable **renamed**.
For now I also hardcoded the Path of my demo directory.
```python
images = [] # List in witch all images are stored with there full path as a string
renamed = 0 

#Path of the demo directory
fairworker_path = '/Users/renekuhn/Downloads/Demo/Fairworker/'
project_path = '/Users/renekuhn/Downloads/Demo/Projekte/'
```
In the first function called **get_images** , I loop trough the uopload folder and all the subdirectories.
After that I initialize a nested loop witch loops trough all files. Next ,I create the variable **file_loc** witch is a string that stores the complete file location including the path and the file name. With a contidional statement can I check if the file is a photo, if it is I add the string I just created as an item to my **images** list.
Now I have a list full of images that need to be renamed and moved to another path.

```python
# Function witch gets all new images and stores them in the images list
def get_images(fairworker_path):
    for subdirectories, directories,files in os.walk(fairworker_path):

        for file_name in files :
            file_loc = subdirectories + os.path.sep + file_name
            #adding .png and .jpg files to the images list
            if file_loc.endswith(".png") or file_loc.endswith(".jpg"):
                images.append(file_loc)
    print("All images are in the List now") 
```
I define another function called **rename_images** witch renames the image itself and moved it to another folder be renaming the path.
In order to do that, I  create a list called **all_parts** where I will store 





```python
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
```

```python
def run():
    get_images(fairworker_path)
    rename_images(project_path)
    print("Great job")
    

window = tk.Tk()

window.title("ULTRA-FAIRWORKER")

window.geometry('300x200')

window.config(bg='yellow')

title = tk.Label(text="Hallo Ludolf! \n Ich  bin der Ultra Fairworker. \n Soll ich einfach alle Bilder auf einmal \n umbennen und in die BV Ordner schieben ? ")
title.pack()

button1 = tk.Button(window, text="Feuer Frei!", background='black',fg='blue',command=run)
button1.pack()



window.mainloop()
```

### Roadmap 
- Bringing Output to the GUI
- Let the User Choose the Upload Folder Path and the Project Path
- Display the Image that is renamed for a few seconds 