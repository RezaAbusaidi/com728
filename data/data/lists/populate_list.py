def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction")
    # We call the first function and store the returned list in a local variable
    available_directions = directions()
    for i in range(len(available_directions)):
        print(f"{i} : {available_directions[i]}")
    # thats the input you get from the user, which is the integer set earlier.
    userdirection = int(input())
    # This links them together. Using user-input as an index.
    return available_directions[userdirection]


def run():
    route = []
    print("Working out escape route...")
    for i in range(5):  # remember when returning an object, call the relevant function, the desired object will be called automatically
        # menu fucntion will retun the user response and append to the mepty list "route". We do route.append(call the function that has the return)
        route.append(menu())
        print(f"Escape route: {route}")


if __name__ == '__main__':
    run()
