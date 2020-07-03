def array_front9(nums):
    end_array = len(nums)
    if end_array > 4:
        end_array = 4
    for i in range(end_array):
        if nums[i] == 9:
            return True
    return False
        
