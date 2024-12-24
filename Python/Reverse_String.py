## This takes your string value and reverses the order

def reverse_string(string):
    return string[::-1]

string = input('enter a string value: ')
print('this is your string in reverse: ', reverse_string(string))