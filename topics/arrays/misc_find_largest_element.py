"""
Title: Find the Largest Element in an Array
Source: Misc / DSA Practice
Link:
Key idea:
The largest element can be found in several ways as shown bellow. Sorting the complete array places
the maximum at the end, while a single pass Bubble Sort is enough to move the maximum
to the final position. The optimal approach simply tracks the largest value during
one linear scan whihc doesn't requirw any swaping.
Topic: Arrays
Tags: linear-scan, sorting
Difficulty: Easy

...
"""



"""
Complexity:
Time: O(n²)

"""
#Complete Bubble sort approach (brute force)
def largest_element_bruteforce(nums: list):

    if not nums:
        raise ValueError("Array Empty")
    n = len(nums)
    for i in range(0, n):
        isswapped=False
        for j in range( 0, n-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                isswapped= True
        if not isswapped:
            break
        
               
    print( f" sorted array is {nums}")       
    print( f" Largest element is  {nums[-1]}")
    

# we can use Merge sort or Tim sort for better time complexity comapred to bubble sort. 


"""
Complexity:
Time: O(n)

"""    
#One-pass Bubble sort approach (better )

def largest_element_One_pass_Bubble(nums: list):

    if not nums:
        raise ValueError("Array Empty")
    n = len(nums)
    
    for j in range( 0, n-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            
    
        
               
    print( f" sorted array is {nums}")       
    print( f" Largest element is  {nums[-1]}")
    

"""
Complexity:
Time: O(n)

"""
#Better approach Linear scan - no swapping required 


def largest_element_linear(nums: list):
    if not nums:
        raise ValueError("Array Empty")
    n = len(nums)
    largest = nums[0]

    for i in range (1,n):
        if nums[i]>largest:
            largest=nums[i]
    
    print( f" Largest element is {largest}")









if __name__ == "__main__":
    arr = [2, 5, 1, 69, 3, 0, 73]

    largest_element_bruteforce(arr.copy())
    largest_element_One_pass_Bubble(arr.copy())
    largest_element_linear(arr.copy())