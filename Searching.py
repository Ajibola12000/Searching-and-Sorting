import random
import bisect

# Generate data
data = [random.randint(0, 1000) for _ in range(1000)]
target = random.choice(data)
sorted_data = sorted(data.copy())

# Linear Search
def linear(arr, x):
    return next((i for i, v in enumerate(arr) if v == x), -1)

# Binary Search (using bisect)
def binary(arr, x):
    i = bisect.bisect_left(arr, x)
    return i if i < len(arr) and arr[i] == x else -1

# Test
print(f"Linear: {linear(data, target)}")
print(f"Binary: {binary(sorted_data, target)}")