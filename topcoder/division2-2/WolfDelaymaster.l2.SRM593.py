def countLetter(word, index, letter):
    count = 0
    while index < len( word ) and word[index] == letter:
        count += 1
        index += 1
    return count

def check(word):
    count = countLetter(word, 0, "w")
    index = count
    for letter in ("o", "l", "f"):
        ct = countLetter(word, index, letter)
        if ct != count:
            return "INVALID"
        index += ct
    if index == len(word):
        return "VALID"
    return check(word[index:])
