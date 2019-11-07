"""
Code to solve the challenge
`4. Median of Two Sorted Arrays <https://leetcode.com/problems/median-of-two-sorted-arrays/>`_

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""
from typing import List
import numpy as np
from copy import deepcopy
import timeit
import matplotlib.pyplot as plt


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    sizeNum1 = len(nums1)
    sizeNum2 = len(nums2)
    even = (sizeNum1 + sizeNum2) % 2 == 0

    # new array where we store the values
    newArray = []
    # length of the array. the last element (or two) will be used to calculate the median
    lenNewArray = (sizeNum1 + sizeNum2) // 2 + 1

    # counters to keep track of the position in nums1 and nums2
    c1 = 0
    c2 = 0

    # check if we reached the end of either of the lists
    end1 = False
    end2 = False
    while len(newArray) < lenNewArray:
        if end1:
            newArray.append(nums2[c2])
            c2 += 1
        elif end2:
            newArray.append(nums1[c1])
            c1 += 1
        else:
            if nums1[c1] > nums2[c2]:
                newArray.append(nums2[c2])
                if c2 < (len(nums2) - 1):
                    c2 += 1
                else:
                    end2 = True
            else:
                newArray.append(nums1[c1])
                if c1 < (len(nums1) - 1):
                    c1 += 1
                else:
                    end1 = True
    # print(newArray)
    if even:
        return (newArray[-1] + newArray[-2]) / 2
    else:
        return newArray[-1]


def ex1(length):
    a = list(np.sort(np.random.randint(0, 10000, np.random.randint(1, length))))
    b = list(np.sort(np.random.randint(0, 10000, np.random.randint(1, length))))
    # c = deepcopy(a)
    # c.extend(b)
    findMedianSortedArrays(a, b)
    # assert findMedianSortedArrays(a, b) == np.median(c)


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


if __name__ == '__main__':
    I = np.arange(10, 8001, 500)
    time1 = []
    for i in I:
        print(i)
        f = wrapper(ex1, i)
        time1.append(timeit.timeit(f, number=1000))
    plt.plot(I, time1, "o")
    plt.show()
