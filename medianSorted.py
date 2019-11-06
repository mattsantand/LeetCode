"""
Code to solve the challenge
`4. Median of Two Sorted Arrays <https://leetcode.com/problems/median-of-two-sorted-arrays/>`_

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    sizeNum1 = len(nums1)
    sizeNum2 = len(nums2)
    even = (sizeNum1 + sizeNum2) % 2 == 0
    c1 = 0
    c2 = 0
    found = False
    if even:
        positionMedian = (sizeNum1 + sizeNum2) // 2 - 1
    else:
        positionMedian = (sizeNum1 + sizeNum2) // 2
    while not found:
        if nums1[c1] > c2[]:

    return median


def ex1():
    a = [1, 3]
    b = [2]

    assert findMedianSortedArrays(a, b) == 2


def ex2():
    a = [1, 2]
    b = [3, 4]

    assert findMedianSortedArrays(a, b) == 1


if __name__ == '__main__':
    # ex1()
    ex2()
