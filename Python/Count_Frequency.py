## this takes a list which is a string value, and returns the number of items
## are in the list. If the same item is in the list it increaments by one.

def count_frequency(lst):
    frequency = {}
    for i in lst:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    return frequency

lst = list(input('enter a list of items. use a space between items: ').split())
print(count_frequency(lst))