import os
filepath = ('/Users/user/Desktop/MSc AI and Data Science /DAT256x/Prepvirtualenvironment3.9.1/com728/data/files/txt/library.txt')
def display_chars(filepath,chars):
    with open (filepath) as file:
        data = file.read(chars)  
    print(f'the first 5 characters are \n {data}')

def display_line(filepath):
    with open (filepath) as file:
       line = file.readline()
    print(f'the full line is \n {line}')
        
def display_text(filepath):
    with open (filepath) as file:
        display = file.read().split('\n')
    print (f'the full text is \n {display}')

def run():
    display_chars(filepath,5)
    display_line(filepath)
    display_text(filepath)

if __name__ == '__main__':
    run()