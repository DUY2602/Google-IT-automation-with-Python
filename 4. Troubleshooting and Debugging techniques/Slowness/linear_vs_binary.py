# Slowness can also be reduced by the the logic and approach of our code

import time

def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

def compare(list, key):
    linear_start = time.time()
    linear_search(list, key)
    linear_end = time.time()
    linear_time = linear_end - linear_start

    print(f"Linear searching execution time: {linear_time:.6f} seconds")

    binary_start = time.time()
    binary_search(list, key)
    binary_end = time.time()
    binary_time = binary_end - binary_start

    print(f"Binary searching execution time: {binary_time:.6f} seconds")

    if linear_time < binary_time:
        return "Linear search is better for this case"
    elif linear_time > binary_time:
        return "Binary search is better for this case"
    else:
        return "Both are fine"
    
lst = list(range(10_000_000))
key = 123456
result = compare(lst, key)
print(result)
