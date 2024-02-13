def spy_game(nums):
    zerozeroseven = False
    for x in range(len(nums) - 1):
        if nums[x] == 0 and nums[x+1] == 0 and nums[x+2] == 7:
            zerozeroseven = True
    
    print(zerozeroseven)
    

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 