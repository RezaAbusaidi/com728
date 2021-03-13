import json

filename = ("robocity.json")

def read(filename):
    print("Reading...")
    with open (filename) as file:
        data = json.load(file)
        print("Done!")
        return data

def save (savefilename, sdata):
    print("Exporting...")
    with open(savefilename, "w") as file:
        json.dump(sdata, file, indent=4) 
    print("done!")


def run():
    json_data = read(filename) #Calling the function "read" and pass it the value "robocity.json". Then store the value returned from calling the function read in a variable named json_data
    save("exported.json", json_data) #The function should then call the function save and pass it the value "exported.json" for the file_path parameter and json_data for the parameter data.
    
    

if __name__ == "__main__":
    run()