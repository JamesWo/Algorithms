#https://www.hackerrank.com/contests/indeed-prime-challenge/challenges/bells-or-waves

# Enter your code here. Read input from STDIN. Print output to STDOUT

def roundToNearestFive(x):
    remainder = x%5
    if remainder<3:
        return x-remainder
    else:
        return x+5-remainder

numPoints = input()
height = []
for i in range(numPoints):
    height.append( float(raw_input().split(" ")[1]) )

# you are a square wave if about half the points are above 0.98
above98 = filter(lambda x: x>=0.98, height)
len98 = len(above98)
if ( len98 < (numPoints/2.0)*1.1 ) and ( len98 > (numPoints/2.0)*.9 ):
    print "square-wave"
else:
    print "sine-wave"
    
hiCounter = 0
lo = False
for h in height:
    if h >= 0.98:
        if lo:
            lo = False
            hiCounter += 1
    if h <= -0.98:
        lo = True
 
print roundToNearestFive(hiCounter)


