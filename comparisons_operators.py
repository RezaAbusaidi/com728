get_firstnumber = input("please enter 1st number")

get_secondnumber = input("Please enter 2nd number")

if (float(get_firstnumber) > (float(get_secondnumber))):
    print("second number is smallest")
elif (float(get_firstnumber) < (float(get_secondnumber))):
    print("first number is smallest")
else:
    print("both are equal")