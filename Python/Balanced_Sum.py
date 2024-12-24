## This method checkes to see if a list is balanced at a certain index.
## For example arr = [5, 6, 8, 11]
## on the left of index [2] = 8, 5 + 6 = 11. And to the right of index [2], [3] = 11.
## This list is balanced.

def balanced_sum(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return True, i
        left_sum += num

    return False

arr = [5, 6, 8, 11]
# arr = list(map(int, input('enter a list of numbers. Use a space: ').split())) ## This would take a dynamic list created by the user
print(balanced_sum(arr))