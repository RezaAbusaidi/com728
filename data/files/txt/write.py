filepath = 'books.txt'


def search(filepath):
    print('searching ...')
    
    sections = ''
    books = 'Books:\n'

    with open(filepath) as file:
        for line in filepath:
           
            if line.startswith('Section'):
                sections +=line
            else:
                books += line
    print('Done')
   
    return f'{sections}\n\n{books}'


def save(filepath, data):
    print('Saving...')
    with open(filepath, "w") as file:
        file.write(data)
    print('Done')


def run():
    data = search('books.txt')
    save('booksectionz.txt', data)


if __name__ == '__main__':
    run()
