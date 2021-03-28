def pattern():
    sequence = {}
    sequence = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequence

def display_keys(data): # you have to define a parameter, so you can pass returned sequence in pattern() to it(data) in the run section. Creates a space for you later to pass what you created before. 
    print("\nKeys:")
    for key in data.keys():
        print(key)

def display_values(data):
    print("\nValues")
    for value in data.values():
        print(value)

def display_items(data):
    print("\n Dictionary")
    for key,value in data.items():
        print(key,value)
def run():
    display_keys(pattern())
    display_values(pattern())
    display_items(pattern())


if __name__ == "__main__":
    run()