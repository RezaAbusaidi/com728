numbers = input('How many numbers should I sum up?')

iterations = 0
total = 0
print()

while iterations<int(numbers):
    inputs = int(input((f'Please enter number {iterations} of {numbers}'))) #must place 'int' at beginning of input, otherwise TypeError: unsupported operand type(s) for +: 'int' and 'str'
    
    iterations=iterations+1
    total=total+inputs #make sure you know what you are adding 
    print (f'The result is {total}')