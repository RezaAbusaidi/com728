cover_type = input('what is the cover type?')

if cover_type.strip() == 'soft':
    print('Is the book cover type perfect bound?')
    peferct_bound = input()
    if peferct_bound == 'yes':
        print('Soft cover, perfect bound books are very popular!')
    else:
        print('Soft covers with coils or stitches are great for short books')

else:
    print('Books with hard covers can be more expensive!')
    