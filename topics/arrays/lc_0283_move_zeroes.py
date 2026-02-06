"""
Title: Move Zeroes
Source: LeetCode (LC-283)
Link: https://leetcode.com/problems/move-zeroes/description/
Topic: Arrays, Two Pointers
Tags: two-pointers, in-place, stable
Difficulty: Easy

Key idea:
Use a write pointer `l` for the next non-zero position. Scan with `r`; whenever nums[r]
is non-zero, swap it into position `l` and advance `l`. This compacts non-zeros to the
front while pushing zeros to the end via swaps.

Why it works:
At any point, indices [0..l-1] contain the non-zero elements seen so far in their original
relative order, because each non-zero is placed at the next available front slot. Elements
after l are the remaining items (including zeros). By the end, all non-zeros are packed
in-order and all zeros are necessarily after them.

Complexity:
Time: O(n)
Space: O(1)

Notes:
- The condition `if nums[r]:` treats only 0 as false; negative/positive values are true.
- Swapping when l == r is safe (no-op).
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r]=nums[r],nums[l]
                l+=1
        return nums        
