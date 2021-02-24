# we can use plan for the inside of the function, to be used as a local variable. but we have to tell the function, yo Im going to use this in the function, just so you know:
# then when we call the function, we're going to use the value that we set with if-statemnet for the plan variable, to see outcome of each, when passed to the function escape_by:
def escape_by (plan):
    if plan == 'jumping over':
        print('We cannot escape that way! The boulder is too big!')
    elif plan == 'running around':
        print('We cannot escape that way! The boulder is moving too fast!')
    elif plan == ('going deeper'):
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

escape_by('jumping over')
escape_by('running around')
escape_by('going deeper')    
    


    