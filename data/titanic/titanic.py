import csv
records = []
headings = []

file_path = "titanic.csv"


def loadpath(file_path):
    print("Loading data...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        # you should not forget to put (csv_reader) instead of (file) in the brackets
        for i in (csv_reader):
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


def display_passenger_names():
    print("The names of the passengers are... \n")
    for i in records:
        passenger_name = i[3]  # iterate the 3rd column rowns
        print(passenger_name)


def display_num_survivors():
    num_survived = 0

    for i in records:
        survival_status = int(i[1])
        if survival_status == 1:
            num_survived += 1
    print(f"{num_survived} passengers survived")

def display_passenger_per_gender():
    females = 0
    males = 0
    for i in records:
        gender = i[4]
        if gender == "male":
            males += 1
        if gender == "female":
            females += 1
    print(f"females:{females}, males:{males}")

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children +=1
            elif age < 65:
                adults += 1
            else:
                elderly +=1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")

        


def run():
    loadpath(file_path)
    print(f"Successfully loaded {len(records)} records")
    display_menu()
    selected_option = display_menu()
    print(f"You have selected option : {[selected_option]}")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
       display_passenger_per_gender()
    elif selected_option ==4:
        display_passengers_per_age_group()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run()
