def has_33(nums):
    doublethree = False
    for x in range(len(nums) - 1):
        if nums[x] == 3 and nums[x + 1] == 3:
            doublethree = True
    print(doublethree)

has_33([1, 3, 3]) 
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3]) 