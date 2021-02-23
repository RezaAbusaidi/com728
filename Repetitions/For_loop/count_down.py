steps_left = int(input('how many steps left?'))

#depending which direction you want the loop to count, define start (in our case: user input eg 6). Then we want the count to stop at 0 and count backwards (-1)
for i in range(steps_left,0,-1):


    print(f'{i} steps remain')