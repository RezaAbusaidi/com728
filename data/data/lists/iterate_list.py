def directions():
   directionlist = ["Move Forward", "Move Backward", "Turn Left", "Turn Right" ]
   return directionlist

def menu():
    print("Please select a direction")
    directionv = directions() # we get whatever object is returend from the function above
    for index in range(len(directionv)):
       getindex = directionv[index] 
       print(f"{index}: {directionv[index]}")

def run():
    menu()

if __name__ == '__main__':
    run()