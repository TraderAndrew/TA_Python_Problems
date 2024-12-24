## This takes an integer and returns True if even
## and False if odd

def is_even(input):
    return input % 2 == 0


n = int(input('enter a number: '))
print(is_even(n))