from collections import Counter

evencount = 0
oddcount = 0

first_num = input('enter first number')
second_num = input('enter second number')
third_num = input('enter third number')


if float(first_num)%2 == 0:
   evencount +=1
if float(second_num)%2 == 0:
   evencount +=1
if float(third_num)%2 == 0:
    evencount +=1

elif (float(first_num)%2 > 0):
    oddcount +=1
elif (float(second_num)%2 > 0):
    oddcount +=1
elif (float(third_num)%2 > 0):
    oddcount +=1




print(f'there are {evencount} even numbers and {oddcount} odd numbers entered')
