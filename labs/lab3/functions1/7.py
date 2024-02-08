def has_33(nums):
    three = False
    doublethree = False
    
    for x in nums:
        if x == 3:
            m = nums[x]
            if nums[x + 1] == 3:
                doublethree = True
            
    return doublethree

has_33([1, 3, 3]) 
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3]) 