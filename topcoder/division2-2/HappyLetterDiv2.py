def getHappyLetter(letters):
    counts = {}
    maxCountLetter = None
    maxCount = 0
    for letter in letters:
        if letter in counts:
            counts[letter]+=1
        else:
            counts[letter]=1
        if counts[letter] > maxCount:
            maxCount = counts[letter]
            maxCountLetter = letter
    counts.pop(maxCountLetter)
    rest = sum( counts.values() )
    if maxCount > rest:
        return maxCountLetter
    else:
        return "."
