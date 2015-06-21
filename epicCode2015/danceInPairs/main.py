#https://www.hackerrank.com/contests/epiccode/challenges/dance-in-pairs

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, k = map(int, raw_input().split(" "))
boys = map(int, raw_input().split(" "))
girls = map(int, raw_input().split(" "))
boys.sort()
girls.sort()

totalMatches = 0
girlIndex = 0
boyIndex = 0

while(True):
    if girlIndex >= n or boyIndex >= n:
        break
    boy = boys[boyIndex]
    girl = girls[girlIndex]
    if girl + k < boy:
        #girl is too short
        girlIndex += 1
        continue
    if boy + k < girl:
        # boy is too short
        boyIndex += 1
        continue
    assert abs(girl-boy) <= k
    girlIndex += 1
    boyIndex += 1
    totalMatches += 1
    
print totalMatches
