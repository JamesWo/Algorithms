#https://www.hackerrank.com/contests/epiccode/challenges/perfect-hiring

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, p, x = map(int, raw_input().split(" "))
scores = map(int, raw_input().split(" "))
for i in range(len(scores)):
    scores[i] = scores[i]*p
    p -= x
print scores.index(max(scores))+1
