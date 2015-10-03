#https://www.hackerrank.com/challenges/kaprekar-numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
def isKaprekar(num):
    square = num**2
    numDigits = len(str(square))
    for split in range((numDigits)/2, -1, -1):
        if split == 0 or split == numDigits:
            left = 0
            right = square
        else:
            left = square / (10**(numDigits-split))
            # for odd values, add 1 to the right split
            right = square % (10**(split+(numDigits%2)))
        if left + right == num:
            return True
    return False
            
start = input()
end = input()
found = []
for num in range(start, end+1):
    if isKaprekar(num):
        found.append(num)

if found:
    print " ".join(map(str, found))
else:
    print "INVALID RANGE"
