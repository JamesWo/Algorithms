#//www.hackerrank.com/challenges/fibonacci-modified

a, b, n = map(int, raw_input().split(" "))
lst = [a, b]
for i in range(2, n):
    lst.append(lst[i-1]**2 + lst[i-2])
print lst[-1]

