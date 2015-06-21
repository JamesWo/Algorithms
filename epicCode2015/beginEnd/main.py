#https://www.hackerrank.com/contests/epiccode/challenges/begin-end

# Enter your code here. Read input from STDIN. Print output to STDOUT
counts = {}
size = input()
string = raw_input()

for char in string:
    if char not in counts:
        counts[char]=0
    counts[char] += 1

total = 0
for count in counts.itervalues():
    # add n choose 2 ways
    total += (count)*(count-1)/2
    # add n since each letter is a satisfying substring by itself
    total += count
print total


