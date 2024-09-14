import random
from enum import Enum
import time
import sys

class PivotSelection(Enum):
    RANDOM = 1
    DETERMINISTIC = 2

def partition(source, low, high, pivot_selection):
    if pivot_selection == PivotSelection.RANDOM: # If the pivot_selection is random
        pivot_index = random.randint(low, high) # Choose a random pivot_index
    elif pivot_selection == PivotSelection.DETERMINISTIC:
        pivot_index = high # Choose the last element as the pivot_index
    else:
        raise ValueError("Invalid pivot selection")
    pivot = source[pivot_index] # Get the pivot value
    source[pivot_index], source[high] = source[high], source[pivot_index] # Swap the pivot value with the last element
    i = low - 1 

    for j in range(low, high): # For each element in the source
        if source[j] <= pivot: # If the element is less than the pivot
            i += 1 # Move the index of the smaller element
            source[i], source[j] = source[j], source[i] # Swap the smaller element with the element at the index

    source[i + 1], source[high] = source[high], source[i + 1] # Swap the pivot value with the element at the index
    return i + 1

def quicksort(source, low, high, pivot_selection):
    if low < high: # If the source has more than one element
        pivot_index = partition(source, low, high, pivot_selection) # Partition the source
        quicksort(source, low, pivot_index - 1, pivot_selection) # Sort the left side of the source
        quicksort(source, pivot_index + 1, high, pivot_selection) # Sort the right side of the source

def quick_sort(source, pivot_selection=PivotSelection.RANDOM): 
    copy = source.copy() # Create a copy of the source
    quicksort(copy, 0, len(source) - 1, pivot_selection) # Sort the copy
    return copy

# Example usage:
# source = [9, 5, 1, 8, 3, 7, 4, 6, 2]
# sortedRandom = quick_sort(source, pivot_selection=PivotSelection.RANDOM)
# sortedDeterministic = quick_sort(source, pivot_selection=PivotSelection.DETERMINISTIC)

# print(source)
# print(sortedRandom)
# print(sortedDeterministic)

array_length = 10000

# 1. A random array of 100000 elements
random_array = random.sample(range(1, array_length + 1), array_length)

# 2. A sorted array
already_sorted = quick_sort(random_array)

# 3. A reverse sorted array
reverse_sorted = already_sorted[::-1]

# 4. An array with repeated elements: 100 elements randomly selected from the first 25 elements of the random array
repeated_elements = [random.choice(random_array[:50]) for _ in range(array_length)]

# 5. An array with all elements equal
all_elements_equal = [1 for _ in range(array_length)]


# Ok, all of our arrays are ready. Let's compare the running time of quick_sort with random and deterministic pivot selection for each of the arrays.


def test_quick_sort(name, array, pivot_selection):
    start_time = time.time()
    sorted_array = quick_sort(array, pivot_selection=pivot_selection)
    end_time = time.time()
    print(name, "with", pivot_selection,": ", end_time - start_time)
    return end_time - start_time

def test_both_pivot_selections(name, array):
    random_time = test_quick_sort(name, array, PivotSelection.RANDOM)
    deterministic_time = test_quick_sort(name, array, PivotSelection.DETERMINISTIC)
    diff_in_ms = (random_time - deterministic_time) * 1000
    if diff_in_ms > 0:
        print("Deterministic pivot selection is faster by ", diff_in_ms, " milliseconds")
    else:
        print("Random pivot selection is faster by ", -diff_in_ms, " milliseconds")
    print()

# Increase the recursion limit, otherwise the code will throw RecursionError for large arrays
sys.setrecursionlimit(20000)

# Random array
test_both_pivot_selections("Random array", random_array)
test_both_pivot_selections("Already sorted array", already_sorted)
test_both_pivot_selections("Reverse sorted array", reverse_sorted)
test_both_pivot_selections("Repeated elements array", repeated_elements)
test_both_pivot_selections("All elements equal array", all_elements_equal)