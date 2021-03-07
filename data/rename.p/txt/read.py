import os
filepath = './library.txt'
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
    display_chars('library.txt',5)
    display_line("library.txt")
    display_text('library.txt')

if __name__ == '__main__':
    run()