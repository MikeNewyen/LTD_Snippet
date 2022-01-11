
#!/usr/bin/env python3
# Path: FindDrawing.py
#This python file is used to find the drawing in a folder from an excel list


from pathlib import Path


def search_in_file(path,searchstring):
    with open(path, 'r') as file:
        if searchstring in file.read():
            print(f'  found drawing in file {path.name}')
        else:
            print('drawing not found')



user_input = input('What is the name of your directory') #set as constant for drawing directory

searchstring = input('What word are you trying to find?') #import from excel

dir_content = sorted(Path(user_input).iterdir())

for path in dir_content: 
    
    if not path.is_dir():
    
        search_in_file(path, searchstring) 