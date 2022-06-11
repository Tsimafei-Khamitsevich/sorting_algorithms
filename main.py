"""
Contains sorting algorithms
"""
import random


def generate_rand_array(n=1000, min=0, max=100):
    """
    Generates a list of random numbers by given parameters.

    Attributes:
    n : int
    number of elements in list
    min : int
    smallest value in list
    max : int
    largest value in list
    
    Returns:
    : list
    list of random values
    """
    return [random.randint(min, max) for _ in range(n)]


def simple_sort(array):
    """
    Implementation of simple sort algorithm

    Attributes:
    array : list
    array to sort
    
    Returns:
    array : list
    New sorted array
    """

    arr = array.copy()

    sortedArr = []
    for _ in range(len(arr)):
        ind = 0
        smallest = arr[ind]
        
        # search for smallest value
        for index, j in enumerate(arr[1:], start=1):
            if j < smallest:
                ind, smallest = index, j
        
        # removing from unsorted and adding to sorted array 
        arr.pop(ind)        
        sortedArr.append(smallest)

    return sortedArr


def selection_sort(array):
    """
    Implementation of selection sort algorithm

    Attributes:
    array : list
    array to sort
    
    Returns:
    array : list
    New sorted array
    """

    arr = array.copy()
    for i in range(len(arr)):
        ind = i
        smallest = arr[ind]

        # search for smallest value
        for index, j in enumerate(arr[i:]):
            if j < smallest:
                smallest = j
                ind = index + i
        
        # swap smallest with 
        # first of unsorted partion of array
        arr[i], arr[ind] = smallest, arr[i]

    return arr


def bubble_sort(array):
    """
    Implementation of bubble sort algorithm

    Attributes:
    array : list
    array to sort
    
    Returns:
    array : list
    New sorted array
    """

    arr = array.copy()
    swap = True
    j = 0
    while swap:
        swap = False
        # single iteration over array
        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                # swaps two consecutive values 
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        j += 1
    
    return arr
    

def insertion_sort(array):
    """
    Implementation of insertion sort algorithm

    Attributes:
    array : list
    array to sort
    
    Returns:
    array : list
    New sorted array
    """

    sortedArr = array[0:1]
    for i in array[1:]:
        
        # searches for value position in sorted list 
        for j in range(len(sortedArr))[::-1]:
            
            if sortedArr[j] <= i:
                sortedArr.insert(j + 1, i)
                break
        else:
            sortedArr.insert(0, i)

    return sortedArr


def merge_sort(array):
    """
    Implementation of merge sort algorithm

    Attributes:
    array : list
    array to sort
    
    Returns:
    array : list
    New sorted array
    """

    if 0 <= len(array) <= 1:
        return array
    elif len(array) >= 2:
        middle= len(array)//2
        sub_arr1 = merge_sort(array[:middle])
        sub_arr2 = merge_sort(array[middle:])

    sort_arr = []
    i, j = 0, 0
    
    # sorts 2 subarrays
    while True:
        if sub_arr1[i] <= sub_arr2[j]:
            sort_arr.append(sub_arr1[i])
            i += 1
        elif sub_arr1[i] > sub_arr2[j]:
            sort_arr.append(sub_arr2[j])
            j += 1

        if len(sub_arr1) == i:
            sort_arr.extend(sub_arr2[j:])
            break
        elif len(sub_arr2) == j:
            sort_arr.extend(sub_arr1[i:])
            break
    
    return sort_arr


def quick_sort(array):
    """
    Implementation of quick sort algorithm

    Attributes:
    array : list
    array to sort
    
    Returns:
    array : list
    New sorted array
    """

    if len(array) < 2:
        return array
    else:
        first_part, second_part, pivot = [], [], []
        
        # random pivot index
        pivot_ind = random.randrange(0, len(array))
        
        # separates into less, more, equal
        # than pivot value
        for i in array:
            if i < array[pivot_ind]:
                first_part.append(i)
            elif i > array[pivot_ind]:
                second_part.append(i)
            else:
                pivot.append(i)

        first_part = quick_sort(first_part)
        second_part = quick_sort(second_part)

        return first_part + pivot + second_part


if __name__ == "__main__":
    
    array = generate_rand_array(num_elem=15)
    array = []
    print(simple_sort(array))
    