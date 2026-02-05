"""
Title: Rotate Array
Source: LeetCode (LC-189)
Link: https://leetcode.com/problems/rotate-array/description/
Topic: Arrays
Tags: in-place, reversal, rotation
Difficulty: Medium

Key idea:
Use the triple-reversal trick:
1) Reverse the whole array.
2) Reverse the first k elements.
3) Reverse the remaining n-k elements.
This produces a right rotation by k.

Why it works:
A right rotation by k moves the last k elements to the front while preserving their order,
and shifts the first n-k elements to the right while preserving their order.
Reversing the whole array places the last k elements at the front but reversed; reversing
the first k segment restores their order. Similarly, reversing the remaining segment restores
the order of the shifted prefix.

Complexity:
Time: O(n)
Space: O(1)

Notes:
- Always reduce k with k % n to handle k >= n.
- Works for k = 0 as well (second reversal becomes a no-op segment).
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
