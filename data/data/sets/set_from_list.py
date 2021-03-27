def observed():
    observations = []
    for i in range(0, 7, 1):
        print("please enter observations")
        values = input()
        observations.append(values)
    return observations


def run():
    print("couning observations...")

    finidngs = observed()
    empty_set= set()
    for i in finidngs:
        new_tuple =(i,finidngs.count(i)) # 0 for i(list content) and 1 for count
        empty_set.add(new_tuple)
    
    for i in empty_set:
        print(f"Observed {i[0]} {i[1]} times")

if __name__ == "__main__":

    run()

        
