
"""
Title: Remove Duplicates from Sorted Array
Source: LeetCode (LC-26)
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Topic: Arrays
Difficulty: Easy

"""
#brute_force
#here look up for set is muh faster compared to list

#Time: O(n) average

def  remove_duplicate_brute_set(nums:list):
     check= set()
     index = 0

     for i in nums:
        if i not in check:
            check.add(i)
            nums[index]=i #Overwrite the original list's contents
            index+=1
     print(nums)       
     print(index)        
     



#brute_force
#Time: O(n²)

def  remove_duplicate_brute(nums:list):

     output =[]

     for i in nums:
         if i not in output:
             output.append(i)
     new_diff = len(nums) - len(output)
     for j in range(0, new_diff):
         output.append(0)
     nums[:] = output #Overwrite the original list's contents   
     print(output)             

    

#optimal
#Time: O(n)

def removeDuplicates(nums:list):
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1

        return i + 1