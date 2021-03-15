import csv
records = []
headings = []

file_path = "titanic.csv"

def loadpath(file_path):
    print("Loading data...")
    with open (file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for i in (file):
            records.append(i)
        print("Done!")
def run():
    loadpath(file_path)
    print(f"Successfully loaded {len(records)} records")

if __name__ == "__main__":
    run()