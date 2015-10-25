# Enter your code here. Read input from STDIN. Print output to STDOUT
def rot13(s, n):
    indexToChar = dict(enumerate(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")))
    charToIndex = {v:k for k,v in indexToChar.items()}
    mod = len(indexToChar)
    new = []
    for char in s[::-1]:
        new.append(indexToChar[(charToIndex[char]+n)%mod])
    return "".join(new)

while True:
    inp = raw_input().strip()
    if inp == '0':
        break
    n, s = inp.split(" ")
    n = int(n)
    print rot13(s, n)
