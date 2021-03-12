import csv
filepath = 'bots.csv'
def extract (filepath):
    with open('bots.csv') as f:
        csvreader = csv.reader(f)
        headings = next(csvreader) #the headings command need to be stated, it stores it in a variable and then we can use it or not.
        names = ""
        print('The extracted names are' )
        for i in csvreader:
            names += str(i) #make sure you write str(i) otherwise, error: cannot contanate list to str
            
            print(f'{names[1]}\n ')
            print(i[1])
def run():
    extract('bots.csv')


if __name__ == '__main__':
    run()