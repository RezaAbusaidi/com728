import os

def cwd ():
    path = os.getcwd() #we define a variable called 'path' and based on that we ask the 'os' to give us the current working directory
    print(f'The current working directory is {path}')
    print('The directory contains the following files')
    for files in os.listdir(path):  # works like the ls command on Linux
        print(files)
cwd()