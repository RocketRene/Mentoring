#import Operatin System Libary
import os

#define Search term
search = 'document'
#define replacement term
replace = 'file'
#define file extention to filter files
type_fiter = '.docx'

#use a method to write all the filenames in the current directory in a list
dir_content = os.listdir('.')
#iterarte trough the items in the list and use a build in method to check if the element is a file
docs = [doc for doc in dir_content if os.path.isfile(doc)]
#initalize a counter variable
renamed = 0 

#print the number of files and elements in the current folder
print(f"{len(docs)} of {len(dir_content)} elements are files.")
#initialize a loop to iterate through all files 
for doc in docs:
    #split the filename into the pure filename variable and a filetype variable using a built in method 
    doc_name,filetype =  os.path.splitext(doc)
    # conditonal statement to filter out irrelevant files 
    if filetype == type_fiter:
        # membership test? , check if the search tearm appears in the item 
        if search in doc_name:
            #generate new filename and save it in a variable 
            new_name = doc_name.replace(search,replace)+filetype
            #rename the files using a built in function
            os.rename(doc,new_name)
            #increment counter variable 
            renamed +=1 
            # print the old and the new filename to the screen 
            print(f"Renamed file {doc} to {new_name}")
#print the number of files that where renamed 
print(f"Renamed {renamed} of  {len(docs)} files. ")
