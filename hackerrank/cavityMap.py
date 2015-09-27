#https://www.hackerrank.com/challenges/cavity-map
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
mapList = []
for _ in range(n):
    mapList.append(map(int, list(raw_input())))

for i in range(n):
    for j in range(n):
        if i in (0, n-1) or j in (0, n-1):
            continue
        if all(map(lambda x: mapList[x[0]][x[1]] < mapList[i][j], ((i-1, j), (i+1,j), (i, j-1), (i, j+1)))):
            mapList[i][j] = 'X'
            
for row in mapList:
    print "".join(map(str, row))
        
