import csv
from typing import ValuesView


def read(filepath):
    with open('bots.csv') as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f'Headings:\n{headings}')
        for values in (file):
             print(values)
        
    
           


def run():
    read('bots.csv')


if __name__ == '__main__':
    run()
