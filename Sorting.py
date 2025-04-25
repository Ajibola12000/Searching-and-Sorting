# Bubble Sort
def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Quick Sort (concise)
def quick(arr):
    return arr if len(arr) <= 1 else quick(
        [x for x in arr[1:] if x <= arr[0]]) + [arr[0]] + quick(
        [x for x in arr[1:] if x > arr[0]])

# Merge Sort (compact)
def merge(arr):
    if len(arr) <= 1: return arr
    mid = len(arr)//2
    return _merge(merge(arr[:mid]), merge(arr[mid:]))

def _merge(left, right):
    return (left and [left.pop(0)] + _merge(left, right)) or right

# Test
print(f"Bubble: {bubble(data.copy())[:5]}...")  # Show first 5 elements
print(f"Quick: {quick(data.copy())[:5]}...")
print(f"Merge: {merge(data.copy())[:5]}...")