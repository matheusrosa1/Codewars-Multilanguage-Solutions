class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    if not nums:
      return 0
    
    unique_index = 0
    for j in range(1, len(nums)):
      if nums[j] != nums[unique_index]:
        unique_index += 1
        # Movendo o elemento único para a posição correta
        nums[unique_index] = nums[j]
    
    # Retornando o número de elementos únicos
    return unique_index + 1
        