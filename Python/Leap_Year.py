## This is a simple method that determines whether or not the year the user inputs
## is a leap year or not.

def leap_year(year):
    if year % 4 == 0 and year % 100 == 0:
        return False
    elif year % 4 == 0 or year % 400 == 0:
        return True

boolean = True
while boolean:
    try:
        year = int(input('enter a year: '))

        if 1900 < year < 10**5:
            boolean = False
            print(leap_year(year))
        else:
            print('year must be between 1900 and 10^5.')

    except ValueError:
            print('you must enter a number.')