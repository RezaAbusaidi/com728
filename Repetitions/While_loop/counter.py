live_cable=input('How many live cables must I avoid?')

iterations = 0

while iterations < int(live_cable):
    iterations = iterations+1 
    
    print(f'Avoiding...Done! {iterations} live cables avoided')
    #I removed the \n for new line, and it worked, displaying iteration each time and in a new line also. 

print('All live cables have been avoided')