import random
import time

# Insertion Sort (Best for Small Datasets)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort (Stable Sorting for Medium Datasets)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Quick Sort (Best for Large Datasets)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# AI-Based Sorting Decision
def smart_sort(arr):
    n = len(arr)
    
    # Analyze dataset to decide best sorting algorithm
    if n < 50:
        print("Using Insertion Sort (Best for Small Data)")
        return insertion_sort(arr)
    elif 50 <= n <= 5000:
        print("Using Merge Sort (Stable for Medium Data)")
        return merge_sort(arr)
    else:
        print("Using Quick Sort (Best for Large Data)")
        return quick_sort(arr)

# Testing the Algorithm
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = [random.randint(1, 10000) for _ in range(n)]
    
    print("\nUnsorted Array:", arr[:10], "...")  # Display only first 10 elements for readability

    start_time = time.time()
    sorted_arr = smart_sort(arr)
    end_time = time.time()
    
    print("\nSorted Array:", sorted_arr[:10], "...")  # Display first 10 elements of sorted array
    print(f"\nSorting Time: {end_time - start_time:.6f} seconds")


