"""
Title: Second Largest and Second Smallest Element in an Array
Source: Misc / DSA Practice
Link:
Topic: Arrays
Tags: sorting, linear-scan, comparison, tracking
Difficulty: Easy


Notes:
- In the current implementation, second_largest starts at -1, so arrays containing
  only negative values may not produce the intended result. If array contains -1 we can take integer min in that case.

"""








# Complexity:
# Time: O(n log n) because Python list.sort() uses Timsort


def second_large_small_element_bruteforce(arr: list):

      
    n = len(arr)
    if n == 0 or n == 1:
        print(-1, -1)
    arr.sort()

    largest = arr[-1]
    smallest = arr[0]


    second_smallest = -1
    second_largest = -1
    for i in range(1,n):
        if arr[i] != smallest:
            second_smallest= arr[i]
            break

    for i in range (n-2, -1, -1 ):
                if arr[i] != largest:
                    second_largest=arr[i]
                    break
                      
                      


                
    print("Sorted array is: ", arr)
    print("Second Smallest and Second largest is: ", second_smallest, second_largest) 



# Complexity:
# Time: O(n)

#better solution

def better_approach_two_passes(arr:list):
    n = len(arr)
    if n == 0 or n == 1:
        print(-1, -1)

    #find the largest 
        
    largest = arr[0]
    for i in range(0,n):
        if arr[i] > largest:
            largest=arr[i]

    #find the second largest
    second_largest = -1

    for i in range(0,n):
        if arr[i]>second_largest and arr[i] != largest:
            second_largest=arr[i]

    # find the smallest
    smallest = arr[0]
    for i in range(1,n):
         if arr[i]<smallest:
              smallest= arr[i]

    #find the second smallest number
    second_smallest = float('inf')
    for i in range(0,n):
         if arr[i]<second_smallest and arr[i]!=smallest:
              second_smallest=arr[i]
         
    print(f" Second largest is {second_largest}\n Second smallest is {second_smallest}")



# Complexity:
# Time: O(n)

# optimal solution
def optimal_second_large_small_element(arr:list):
      
      n = len(arr)
      if n == 0 or n == 1:
           print(-1, -1)

     
      largest = arr[0]
      sec_largest=-1

      for i in range(1,n):
        
        if arr[i]>largest:
             sec_largest=largest
             largest=arr[i]
        elif arr[i]==largest:
             pass
        elif arr[i]<largest and arr[i]>sec_largest:
             sec_largest=arr[i]
      print(f"Second Largest is {sec_largest}")


      smallest = arr[0]
      sec_smallest = float('inf')

      for i in range(1, n):
          if arr[i] < smallest:
              sec_smallest = smallest
              smallest = arr[i]
          elif arr[i] == smallest:
              pass
          elif arr[i] > smallest and arr[i] < sec_smallest:
              sec_smallest = arr[i]

      print(f"Second Smallest is {sec_smallest}")




if __name__ == "__main__":
    nums = [2, 5, 1, 73, 69, 3, 0, 73]

    second_large_small_element_bruteforce(nums.copy())
    better_approach_two_passes(nums.copy())
    optimal_second_large_small_element(nums.copy())
        