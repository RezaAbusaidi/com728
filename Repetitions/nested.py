#outer loop, repeats inner loop 3 times. The inner loop, prints 0-9. Use Print function for inner loop. 
#end = by deault, python adds a new line to the end of each print output, whuch we sometimes use \n. (end="") allows the output to be attached to another.

for count in range(0,3,1):
    for number in range(0,10,1):
        print(f"{number} |", end="")