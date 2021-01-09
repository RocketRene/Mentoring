import os 

search  = 'file'
replace = 'document'
filetype = '.docx'
renamed = 0 

dir_content =  os.listdir('.')
docs=[doc for doc in dir_content if os.path.isfile(doc)]

print(f"{len(docs)} of {len(dir_content)} elements are files ")

for doc in docs :

    filename, fileformat = os.path.splitext(doc)

    if fileformat == filetype:

        if search in filename:
            
            new_name = filename.replace(search,replace)+filetype
            os.rename(doc,new_name) 
            renamed += 1
            print(f"Renamed {renamed}: {doc} ----> {new_name}\n")

