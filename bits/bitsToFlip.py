
def bitsToFlip(x, y):
    count = 0
    xor = x ^ y
    while xor:
        xor &= xor-1
        count += 1
    return count


assert bitsToFlip(3,4)==3
assert bitsToFlip(3,5)==2
assert bitsToFlip(3,7)==1
assert bitsToFlip(5,1)==1
assert bitsToFlip(5,13)==1
assert bitsToFlip(29,29)==0
