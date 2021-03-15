import csv
records = []
headings = []

file_path = "titanic.csv"


def loadpath(file_path):
    print("Loading data...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for i in (file):
            records.append(i)
        print("Done!")


def display_menu():
    print(
        """
    Please select one of the following options:
    [1] Display the names of all passengers
    [2] Display the number of passengers that survived
    [3] Display the number of passengers per gender
    [4] Display the number of passengers per age group
  
        """
    )
    response = int(input("Please select an option from above "))
    return response


def run():
    loadpath(file_path)
    print(f"Successfully loaded {len(records)} records")
    display_menu()
    selected_option = display_menu()
    print(f"You have selected option : {selected_option}")


if __name__ == "__main__":
    run()
