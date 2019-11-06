from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    sizeNum1 = len(nums1)
    sizeNum2 = len(nums2)
    even = (sizeNum1 + sizeNum2) % 2 == 0

    if even:
        threshold = int((sizeNum1 + sizeNum2) / 2)
    else:
        threshold = (sizeNum1 + sizeNum2) // 2 + 1

    print(sizeNum1, sizeNum2, even, threshold)
    iter = 0
    while len(nums1) + len(nums2) > threshold:
        print(iter)
        print(nums1, nums2)
        if nums1[0] < nums2[0]:
            nums1.pop(0)
        else:
            nums2.pop(0)
        print(nums1, nums2)
        print("\n")
        iter += 1

    if not even:
        median = min([nums1[0], nums2[0]])
    else:
        median = min([(nums1[0] + nums2[0]) / 2,
                      (nums1[0] + nums1[1]) / 2,
                      (nums2[0] + nums2[1]) / 2])
    return median


def ex1():
    a = [1, 3]
    b = [2]

    assert findMedianSortedArrays(a, b) == 2


def ex2():
    a = [1, 1, 1, 1, 1, 1, 30]
    b = [1, 1, 1, 1, 2, 10]

    assert findMedianSortedArrays(a, b) == 1

if __name__ == '__main__':
    # ex1()
    ex2()
