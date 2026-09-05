"""
Title: Check if an Array Is Sorted
Source: Misc / DSA Practice
Link:
Topic: Arrays
Tags: linear-scan, sorted-array, comparison
Difficulty: Easy


Complexity:
Time: O(n)

"""


def if_sorted(num:list):
    n = len(num)
    if n == 0 or n == 1:
        print("Give proper array to check sorting")

    check_sort= True
    for i in range(0,n-1):
        if num[i]>num[i+1]:
            check_sort= False
            break
    
    if check_sort:
        print("Array sorted")

    else:
        print("Array not sorted")    



if __name__ == "__main__":
    nums = [1, 5, 5, 6, 8, 6, 8, 73]

    if_sorted(nums.copy())