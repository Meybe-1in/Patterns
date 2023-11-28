class Solution:
  def contains_duplicate(self, nums) -> bool:
      
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]: # if any two elements are the same, return true
          print (True)
    print (False) # if no duplicates are found, return false

if __name__ == '__main__':
  sol = Solution()
  nums1 = [1, 2, 3, 4]
  print(sol.contains_duplicate(nums1)) # Expected output: False

  nums2 = [1, 2, 3, 1]
  print(sol.contains_duplicate(nums2)) # Expected output: True

  nums3 = []
  print(sol.contains_duplicate(nums3)) # Expected output: False

  nums4 = [1, 1, 1, 1]
  print(sol.contains_duplicate(nums4)) # Expected output: True