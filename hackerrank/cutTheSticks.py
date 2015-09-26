#https://www.hackerrank.com/challenges/cut-the-sticks

# Enter your code here. Read input from STDIN. Print output to STDOUT
numSticks = input()
print numSticks
remainingSticks = numSticks
sticks = map(int, raw_input().split(" "))
sticks.sort()
index = 0
while (index+1) < len(sticks):
    index += 1
    remainingSticks -= 1
    currCount = 0
    value = sticks[index]
    while sticks[index] == sticks[index-1]:
        index += 1
        remainingSticks -= 1
    print remainingSticks
    
    

