from typing import get_origin

print('what phrase do you see')
phrase = input()

for i in range(len(phrase)-1,-1,-1): #dont forget to say i in range, NOT i in phrase otherwise, Type Error: str obj not callable
### does not make sense to reverse an index by putting (-) next to the stop
    print(phrase[i])
   
    