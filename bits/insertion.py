def insertion( x, y, i, j ):
    # create mask with 0's between i and j
    # all 1s
    ones = -1
    # all 1s up to j, then 0s
    # 111110000000
    ones << j
    #all 1s up to j, 0s up to i, 1s to end
    # 111110000011
    ones |= ( -1 << j )
    # mask x with this newly created mask
    x &= ones
    # shift y by i and or with x
    x |= ( y << i )
    return x

# test

result = insertion(int('110000011',2), int('01011',2), 2, 7 ) 
assert result == int('110101111',2), "result:%d ( %s )" % (result, bin(result))
