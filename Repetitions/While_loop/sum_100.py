print('Calculating the sum of the first 100 numbers..')

iterations = 1 # set iteration to 1 this time, as we start dding from 1+2+3... and not 0+1+2
total = 0 #also we need to set the total variable and initiate it at with a value of 0, so that the iterator adds to the total(0)each time it moves up (iterations=iteration + 1) which becomes before the total = total + iteration

while iterations <= 100:
    iterations += 1
    total = total + iterations

print(f'...Done! The answer is {total}')