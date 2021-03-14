def steps():
    likelihoods = [("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)] #list of tuples 
    return likelihoods

def run():
    listtup = steps() # return 1st function
    good_steps = [] # empty list of bad steps
    bad_steps = [] # empty list of bad steps
    for _ in listtup:
        if _[1] >= 50: # this is how to access the index1 of the likelihoods list mentioned in the first function above. If I say i[0], then it will call the string "step". Its either 0 or 1, as the tuples contain 2 items.
            good_steps.append(_)
        else:
            bad_steps.append(_)
    print(f"good steps : {len(good_steps)} bad steps : {len(bad_steps)}") # if I dont include len, then it wont return the number of appended iterations in the list

if __name__ == '__main__':
    run()