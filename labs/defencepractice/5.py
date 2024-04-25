def find_common_elements(lsta, lstb):
    lstc = []
    for x in lsta:
        for y in lstb:
            if x == y:
                lstc.append(x)
    print(lstc)
    
lsta = [2, 3, 5, 9]
lstb = [2, 7, 9, 8]

find_common_elements(lsta, lstb)