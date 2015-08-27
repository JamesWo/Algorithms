"""
# [UndoHistory](http://community.topcoder.com/tc?module=ProblemDetail&rd=15499&pm=12523)
*Single Round Match 579 Round 1 - Division I, Level One*

## Statement
Bob is using a peculiar text editor to write a sequence of lines of text.
The editor consists of three parts: a results window, a text buffer and an undo history.
More details about the three parts follow.
The results window contains a sequence of strings: the lines of text you already wrote. Initially, the results window is empty.
The text buffer contains a string: the line you are writing at the moment. Initially, the string in the text buffer is empty.
The undo history contains a sequence of strings: all the past states of the text buffer. Initially, the undo history contains a single element: an empty string.

You are given a String[] *lines*.
Bob would like to print the contents of *lines* into the results window.
(At the end, the sequence of strings stored in the results window must be precisely equal to *lines*. Order of elements matters.)
Additionally, Bob would like to do so as quickly as possible.
He is able to take the following actions:

Bob may type a lowercase letter. The letter is appended to the text buffer. The new text buffer is then added as a new element of the undo history. (For example, if the text buffer currently contains "do", then pressing 'g' changes the text buffer to "dog" and then stores "dog" into the undo history.)
Bob may press Enter. When he does so, the current content of the text buffer is printed to the results window as a new line, after the lines that were printed earlier. The text buffer remains unmodified. (For example, if the text buffer contains "dog" and Bob presses Enter, "dog" will be appended to the results window, and the results buffer still contains "dog".)
Bob may use two mouse clicks to restore any entry from the undo history to the text buffer. This operation does not modify the undo history.

Return the minimum total number of button presses (keyboard and mouse) that Bob needs to print all the given lines into the results window.

## Definitions
- *Class*: `UndoHistory`
- *Method*: `minPresses`
- *Parameters*: `String[]`
- *Returns*: `int`
- *Method signature*: `int minPresses(String[] lines)`

## Constraints
- *lines* will contain between 1 and 50 elements, inclusive.
- Each element of *lines* will contain between 1 and 50 characters, inclusive.
- Each element of *lines* will contain only lowercase letters ('a'-'z').

## Examples
### Example 1
#### Input
<c>["tomorrow", "topcoder"]</c>
#### Output
<c>18</c>
#### Reason
Type 't'. The text buffer now contains "t", and the undo history now contains "" and "t".
Type 'o'. The text buffer now contains "to", and the undo history now contains "", "t", and "to".
Using six more keypresses, type the letters in "morrow". The text buffer now contains "tomorrow" and the undo history contains all prefixes of "tomorrow". The results window is still empty.
Press Enter. The results window now contains one string: "tomorrow".
Click the mouse twice to restore "to" from undo history.
Using another six keypresses, type the letters in "pcoder".
Press Enter. The results window now contains "tomorrow" and "topcoder", in this order, and we are done.
The total number of button presses was 8 (typing "tomorrow") + 1 (Enter) + 2 (mouse) + 6 (typing "pcoder") + 1 (Enter) = 18.

### Example 2
#### Input
<c>["a","b"]</c>
#### Output
<c>6</c>
#### Reason
After typing "a" and pressing enter, we need to restore the empty string (which is always present at the top of the undo buffer) before typing "b".

### Example 3
#### Input
<c>["a", "ab", "abac", "abacus" ]</c>
#### Output
<c>10</c>
#### Reason
There are times when it is not necessary to use the undo history at all.

### Example 4
#### Input
<c>["pyramid", "sphinx", "sphere", "python", "serpent"]</c>
#### Output
<c>39</c>
### Example 5
#### Input
<c>["ba","a","a","b","ba"]</c>
#### Output
<c>13</c>

"""
def useBuf(word, seen, buf):
    if not word.startswith(buf):
        return float("inf")
    count = 0
    for j in range(len(buf)+1, len(word)+1):
        seen.add(word[0:j])
        count += 1
    return count+1 # hit enter

def useHistory(word, seen):
    count = 0
    for i in range(len(word), -1, -1):
        if word[0:i] in seen:
            for j in range(i+1, len(word)+1):
                seen.add(word[0:j])
                count += 1
            return count + 3
    assert False

def bestWay(word, seen, buf):
    newSeen = seen.copy()
    c1 = useBuf(word, newSeen, buf)
    c2 = useHistory(word, seen)
    return min(c1, c2)

def minPresses(lines):
    seen = set()
    seen.add("")
    count = 0
    buf = ""
    for word in lines:
        count += bestWay(word, seen, buf)
        buf = word
    return count

