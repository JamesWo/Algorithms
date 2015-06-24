# binary search practice

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
salaries = []
for i in range(n):
    salaries.append(input())
salaries.sort()
salariesLen = len(salaries)

numQ = input()
for _ in range(numQ):
    q = input()
    lo = 0
    hi = salariesLen
    while lo < hi:
        mid = (lo+hi)//2
        if salaries[mid] < q:
            lo = mid + 1
        else:
            hi = mid
    assert lo == hi
    print lo
    
