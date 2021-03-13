def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1 ]
    return path # if you dont return you wont access later - TypeError: 'NoneType' object is not subscriptable
def run():
    print ("Moving...")
    pathology = movements()
    print(f"{pathology[0]} for {pathology[1]} steps")
    print(f"{pathology[2]} for {pathology[3]} steps")
    print(f"{pathology[4]} for {pathology[5]} steps")
    print(f"{pathology[6]} for {pathology[7]} steps")

if __name__ == '__main__':
    run()