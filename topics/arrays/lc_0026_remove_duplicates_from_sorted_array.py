"""
Title: Remove Duplicates from Sorted Array
Source: LeetCode (LC-26)
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Topic: Arrays, Two Pointers
Tags: two-pointers, in-place, sorted-array, duplicates
Difficulty: Easy

Key idea:
Use two pointers: `r` scans the array, and `l` tracks the position to write the next
unique value. Whenever nums[r] differs from the previous value, write it at nums[l]
and increment l.

Why it works:
Because nums is sorted (non-decreasing), duplicates appear in contiguous blocks.
Every time we encounter a new value at r (nums[r] != nums[r-1]), it must be the next
unique value in sorted order, so writing it to nums[l] preserves order and compacts
unique values into the first l positions. At the end, l equals the number of unique
elements k.

Complexity:
Time: O(n)
Space: O(1)

Notes:
- Works with duplicates and negative values since it relies only on adjacent comparisons.
- The judge ignores elements beyond the returned k.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1

        for r in range(1, len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l        
