filename = '/Users/user/Desktop/MSc AI and Data Science /DAT256x/Prepvirtualenvironment3.9.1/bin/python" "/Users/user/Desktop/MSc AI and Data Science /DAT256x/Prepvirtualenvironment3.9.1/com728/data/files/txt/library.txt'


def search(filename):
    print('searching ...')
    with open(filename) as file:
        for line in file:

            print(f'Looked in The {line.strip()}.')


def run():
    search('library.txt')
    print('..done')


if __name__ == '__main__':
    run()
