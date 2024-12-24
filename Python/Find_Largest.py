## This take a list of integers and returns the highest value

def find_largest(n):
    return max(n)

n = list(map(int, input('enter some numbers. Use a space between numbers: ').split()))
print('this is the largest element: ', find_largest(n))