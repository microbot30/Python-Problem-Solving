import numpy as np


def random_array(n, max):
    return np.random.randint(max, size=n)


def median_sort(arr):
    for x in arr:
        greater = 0  # how many numbers are greater than x
        smaller = 0  # how many numbers are smaller than x
        if len(arr) % 2 != 0:  # array size odd or even
            for y in arr:  # comparing each element with others
                if x > y:
                    greater += 1
                elif x < y:
                    smaller += 1
            if greater == smaller:  # odd sized array has similar greater and smaller numbers
                return x
        else:
            for y in arr:
                if x > y:
                    greater += 1
                elif x < y:
                    smaller += 1
            if greater - smaller == -1:
                return x


def rec_median_sort(arr):
    median_list = []
    ele = median_sort(arr)
    if len(median_list) == 0:
        median_list.append(ele)
    else:
        for i in range(0, len(median_list)):
            switch = False
            if ele < median_list[i]:
                median_list.insert(0, ele)
                switch = True
        if switch is False:
            median_list.append(ele)
    if len(arr) == 0:
        return
    else:
        print(median_list)
        arr = np.delete(arr, np.where(arr == ele))
        return rec_median_sort(arr)


if __name__ == '__main__':
    arr = random_array(5, 100)
    print(rec_median_sort(arr))
    sorted_arr = sorted(arr)
    if len(sorted_arr) % 2 != 0:
        n = int(len(sorted_arr) // 2)
    else:
        n = len(sorted_arr) // 2 - 1
    print(sorted_arr)
    print("Sorted median: ", sorted_arr[n])
