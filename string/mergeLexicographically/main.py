#


def merge(str1, str2):
    str1Len = len(str1)
    str2Len = len(str2)
    pos1 = 0
    pos2 = 0
    # construct the new string in a list, and concat at end
    newStr = []
    while True:
	if pos1 >= str1Len:
	    newStr.append(str2[pos2:])
	    break
	if pos2 >= str2Len:
	    newStr.append(str1[pos1:])
	    break
	if ord(str1[pos1]) < ord(str2[pos2]):
	    newStr.append(str1[pos1])
	    pos1 += 1
	elif ord(str1[pos1]) > ord(str2[pos2]):
	    newStr.append(str2[pos2])
	    pos2 += 1
	else:
	    # the character is the same.  we increment
	    # the pointer that gives us the lowest next char
	    newStr.append(str1[pos1])
	    tempPos1 = pos1 + 1
	    tempPos2 = pos2 + 1
	    while True:
		if tempPos2 >= str2Len or ord(str1[tempPos1]) < ord(str2[tempPos2]):
		    pos1 = tempPos1
		    break
		elif tempPos1 >= str1Len or ord(str1[tempPos1]) > ord(str2[tempPos2]):
		    pos2 = tempPos2
		    break
		else:
		    newStr.append(str1[tempPos1])
		    tempPos1 += 1
		    tempPos2 += 1
    return "".join(newStr)



numCases = input()
for _ in range(numCases):
    str1 = raw_input()
    str2 = raw_input()
    print merge(str1, str2)
		    
