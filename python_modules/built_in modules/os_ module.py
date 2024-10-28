import os
# working with dir

# getcwd() : Get the current working directory

current_directory = os.getcwd()
print(f'surrent working directory : {current_directory}')

# lisdir() : list all files and directories in the specific path
# r : raw  string : used to remove unicode escape errors in program

path=r'C:\Users\abish\PycharmProjects\Python-Basics\ak'
items=os.listdir(path)
print(items) # display list

#mkdir() : create a directory

new_dir=r'C:\Users\abish\PycharmProjects\Python-Basics\venv\kk'
os.mkdir(new_dir)
print(f'directory {new_dir} created')

# rmdir() : remove directory (omly works if directory is empty)
dir_remove=r'C:\Users\abish\PycharmProjects\Python-Basics\venv\kk'
os.rmdir(dir_remove)
print(f'directory {dir_remove} removed')