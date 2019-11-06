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


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    sizeNum1 = len(nums1)
    sizeNum2 = len(nums2)
    even = (sizeNum1 + sizeNum2) % 2 == 0
    newArray = []
    lenNewArray = (sizeNum1 + sizeNum2) // 2 + 1
    c1 = 0
    c2 = 0
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


def ex1():
    a = list(np.sort(np.random.randint(0, 100, np.random.randint(1, 20))))
    b = list(np.sort(np.random.randint(0, 100, np.random.randint(1, 20))))
    print()
    print(a)
    print(b)
    c = deepcopy(a)
    c.extend(b)
    assert findMedianSortedArrays(a, b) == np.median(c)


if __name__ == '__main__':
    for i in range(1000):
        ex1()
    # ex2()
