#import Operatin System Libary
import os
import argparse


parser = argparse.ArgumentParser(description='Batch rename files in directory')

parser.add_argument("search",type=str,help="To be replaced text")
parser.add_argument("replace",type=str,help="Text to use for replacement")
parser.add_argument("--filetype",type=str,default=None,help="Only files with the given type will be renamed (e.g.  .txt)")
parser.add_argument("--path" ,type=str, default=".",help="Directory path that contains the to be renamed files ")

args = parser.parse_args()




#define Search term
search = args.search
#define replacement term
replace = args.replace 
#define file extention to filter files
type_fiter = args.filetype

path = args.path


print(f"Renaming files at path {path}")

#use a method to write all the filenames in the current directory in a list
dir_content = os.listdir(path)

path_dir_content = [os.path.join(path,doc) for doc in dir_content]
#iterarte trough the items in the list and use a build in method to check if the element is a file
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
#initalize a counter variable
renamed = 0 

#print the number of files and elements in the current folder
print(f"{len(docs)} of {len(dir_content)} elements are files.")
#initialize a loop to iterate through all files 
for doc in docs:
    #split the filename into the pure filename variable and a filetype variable using a built in method 
    full_doc_path,filetype =  os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)
    # conditonal statement to filter out irrelevant files 
    if filetype == type_fiter or type_fiter is None:
        # membership test? , check if the search tearm appears in the item 
        if search in doc_name:
            #generate new filename and save it in a variable 
            new_doc_name = doc_name.replace(search,replace)

            new_doc_path = os.path.join(doc_path,new_doc_name)+filetype
            os.rename(doc,new_doc_path)
            #rename the files using a built in function
            #os.rename(doc,new_name)
            #increment counter variable 
            renamed +=1 
            # print the old and the new filename to the screen 
            print(f"Renamed file {doc} to {new_doc_path}")
#print the number of files that where renamed 
print(f"Renamed {renamed} of  {len(docs)} files. ")
