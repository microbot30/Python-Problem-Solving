arr = [1, 5, 2, 8, 4]  # un-sorted array
print(arr)
for x in arr:
    greater = 0     # how many numbers are greater than x
    smaller = 0     # how many numbers are smaller than x
    if len(arr) % 2 != 0:   # array size odd or even
        for y in arr:   # comparing each element with others
            if x > y:
                greater += 1
            elif x < y:
                smaller += 1
        if greater == smaller:  # odd sized array has similar greater and smaller numbers
            print("Median: ", x)
            break
    else:
        for y in arr:
            if x > y:
                greater += 1
            elif x < y:
                smaller += 1
        if greater - smaller == 1:
            print("median", x)
            break

sorted_arr = sorted(arr)
if len(sorted_arr) % 2 != 0:
    n = int(len(sorted_arr)//2)
else:
    n = len(sorted_arr)//2
print(sorted_arr)
print("Sorted median: ", sorted_arr[n])
