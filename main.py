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
   
    first_part, second_part = [], []
    
    # random pivot index
    pivot_ind = random.randrange(0, len(array))
    pivot = array.pop(pivot_ind)
    # separates into less, more, equal
    # than pivot value
    for i in array:
        if i <= pivot:
            first_part.append(i)
        elif i > pivot:
            second_part.append(i)

    first_part = quick_sort(first_part)
    second_part = quick_sort(second_part)

    return first_part + [pivot] + second_part


def shell_sort(array, d=5):
    """
    Implementation of shell sort algorithm

    Attributes:
    array : list
    array to sort
    d : int
    d value, step of indexes to pick
    
    Returns:
    array : list
    New sorted array
    """
    array = array.copy()
    for x in range(d, 0, -1):
        for i in range(x):
            index = range(i, len(array), x)
            sub_arr = [array[k] for k in index]
            sorted_sub_arr = quick_sort(sub_arr)
            
            for j in range(len(sorted_sub_arr)):
                array[index[j]] = sorted_sub_arr[j]
    
    return array


def radix_sort(array, ascending=True):
    """
    Implementation of radix sort algorithm

    Attributes:
    array : list
    array to sort
    ascending : bool
    order of sorting 
    
    Returns:
    array : list
    New sorted array
    """

    def sort_positive_num(array, ascending=True):
        
        if len(array) < 2:
            return array
        
        divider = 10

        all_digits_through = False
        while not all_digits_through:
            
            all_digits_through = True
            
            # determines ascending, descending order
            digits0_9 = range(10)
            if not ascending:
                digits0_9 = range(9, -1,-1)

            d = {i: list() for i in digits0_9}

            for i in array:
                digit = int((i % divider) / (divider / 10))
                try:
                    d[digit].append(i)
                except KeyError:
                    print(f'Error causes {i} {digit} {divider}')
                    raise KeyError()

                if i // divider != 0:
                    all_digits_through = False

            divider = divider * 10
            array.clear()

            for _, l in d.items():
                array.extend(l)

            d.clear()
            
        return array

    array = array.copy()
    
    neg_num, pos_num = [], []
    for i in array:
        if i < 0:
            neg_num.append(-i)
        else:
            pos_num.append(i)
    
    # determines ascending, descending order of whole array
    neg_num = sort_positive_num(neg_num, False if ascending else True)
    neg_num = [-abs(i) for i in neg_num]
    pos_num = sort_positive_num(pos_num, True if ascending else False)
    
    # determines ascending, descending order of whole array
    if ascending:
        sorted_array = neg_num + pos_num
    else:
        sorted_array = pos_num + neg_num

    return sorted_array

    
if __name__ == "__main__":
    
    array = generate_rand_array(n=15)
    print(radix_sort(array, False))
    