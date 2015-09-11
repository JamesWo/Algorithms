"""
# [TheDeviceDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15489&pm=12399)
*Single Round Match 569 Round 1 - Division II, Level Two*

## Statement
Manao works at a laboratory on a highly classified project. From time to time, he is given a special device and has to determine its exact structure. Every such device operates on special plates. There are M bits written on each of the plates from left to right. The device has two inputs and a screen. Each input requires a plate. When two plates are connected to the device, M bits of output appear on the screen. Each bit of output is either a binary OR, AND or XOR of the corresponding bits of the input plates. Manao's task is to determine what operation is carried out for each of the bits.

Manao has N plates. He is going to test the device on each possible pair of these plates and determine its structure by the outputs on the screen. It might be that the plates Manao has are not enough to uniquely identify every possible device. You are given String[] *plates*, where each element describes a plate Manao has. If these plates are certainly sufficient to determine the structure of the device completely, return "YES". Otherwise, return "NO".

## Definitions
- *Class*: `TheDeviceDiv2`
- *Method*: `identify`
- *Parameters*: `String[]`
- *Returns*: `String`
- *Method signature*: `String identify(String[] plates)`

## Constraints
- *plates* will contain between 1 and 50 elements, inclusive.
- Each element of *plates* will be between 1 and 50 characters long, inclusive.
- All elements of *plates* will be of equal length.
- Each element of *plates* will contain characters from the set {'0', '1'} only.

## Examples
### Example 1
#### Input
<c>["010",<br /> "011",<br /> "000"]</c>
#### Output
<c>"NO"</c>
#### Reason
With these plates we cannot determine anything about the operation done on the first bit, because all of them give the same result. Also, we cannot be sure that we can determine the operation done on the third bit: if it is the AND operation, we can find this out (for example by using the first two plates), but we cannot distinguish between OR and XOR using the given plates.

### Example 2
#### Input
<c>["1",<br /> "0",<br /> "1",<br /> "0"]</c>
#### Output
<c>"YES"</c>
#### Reason
Manao will see the result for every possible combination of bits, which is enough to distinguish between AND, OR and XOR.

### Example 3
#### Input
<c>["11111"]</c>
#### Output
<c>"NO"</c>
#### Reason
A single plate is not enough for even one test.

### Example 4
#### Input
<c>["0110011",<br /> "0101001",<br /> "1111010",<br /> "1010010"]</c>
#### Output
<c>"NO"</c>
#### Reason
The operation done on the fifth bit from the left (1-based index) cannot be determined.

### Example 5
#### Input
<c>["101001011",<br /> "011011010",<br /> "010110010",<br /> "111010100",<br /> "111111111"]</c>
#### Output
<c>"YES"</c>

"""
def identify(plates):
    for i in range(len(plates[0])):
        ones = 0
        zeros = 0
        for plate in plates:
            if plate[i] == '1':
                ones += 1
            elif plate[i] == '0':
                zeros += 1
            else:
                assert False, plate[i]
        if ones >= 2 and zeros >= 1:
            continue
        else:
            return "NO"
    return "YES"
