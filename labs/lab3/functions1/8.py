def spy_game(nums):
    found_zero = False
    found_double_zero = False
    for num in nums:
        if num == 0:
            if found_zero:  
                found_double_zero = True  
        elif num == 7:
            if found_double_zero:  
                return True  
        else:
            found_zero = False  

    return False  
    

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 