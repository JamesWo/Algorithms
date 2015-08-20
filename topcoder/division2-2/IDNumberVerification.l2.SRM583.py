"""
# [IDNumberVerification](http://community.topcoder.com/tc?module=ProblemDetail&rd=15503&pm=12610)
*Single Round Match 583 Round 1 - Division II, Level Two*

## Statement
This problem statement contains superscripts and/or subscripts. These may not display properly outside the applet.

In People's Republic of China, every citizen has a unique ID string. The length of the ID is 18 characters. The first 17 characters (called the body code) are all digits, the last character (called the checksum code) can be either a digit or 'X'.

The body code is then divided into three parts: from left to right, these are the region code, the birthday code, and the sequential code. They look as follows:

The region code has 6 digits. Some 6-digit strings represent regions, other 6-digit strings are invalid. You are given the valid region codes as a String[] *regionCodes*.
The birthday code has 8 digits. It gives the citizen's birthday in the form YYYYMMDD. That is, the first 4 digits is the year of birth, the next 2 is the month (01 to 12, with a leading zero if necessary), and the last 2 digits is the day. When verifying the birthday code, you should consider leap years (see the Notes). Additionally, a valid birthday code must represent a date between Jan 1, 1900 and Dec 31, 2011, inclusive.
The sequential code has 3 digits. These 3 digits may be arbitrary, with one exception: the sequential code "000" is invalid. If the sequential code represents an odd number (e.g., "007"), the person is a male. Otherwise (e.g., "420") the person is a female.

The last character of an ID string is the checksum code. This is derived from the first 17 digits. Let a1, a2, ..., a17 denote the body code from left to right. Consider the following modular equation: x + a1*2^(17) + a2*2^(16) + a3*2^(15) + ... + a16*2^(2) + a17*2^(1) = 1 (mod 11). This equation always has exactly one solution x such that 0 <= x <= 10. If x=10, the checksum code is 'X'. Otherwise, the checksum code is the corresponding digit. (E.g., if x=5, the checksum code is '5'.)

You are given a String *id*. If this is not a valid ID string, return "Invalid" (quotes for clarity). If *id* represents a valid ID string of a male citizen, return "Male". Finally, if *id* represents a valid ID string of a female citizen, return "Female".

## Definitions
- *Class*: `IDNumberVerification`
- *Method*: `verify`
- *Parameters*: `String, String[]`
- *Returns*: `String`
- *Method signature*: `String verify(String id, String[] regionCodes)`

## Notes
- A year is a leap year if and only if it satisfies one of the following two conditions: A: It is a multiple of 4, but not a multiple of 100. B: It is a multiple of 400. Therefore, 1904 and 2000 are leap years, while 1900 and 2011 are not.

## Constraints
- *id* will be 18 characters long.
- First 17 characters of *id* will be between '0' and '9', inclusive.
- Last character of *id* will be 'X' or between '0' and '9', inclusive.
- *regionCodes* will contain between 1 and 50 elements, inclusive.
- Each element of *regionCodes* will be 6 characters long.
- Each element of *regionCodes* will consist of characters between '0' and '9', inclusive.
- For each element of *regionCodes*, its first character will not be '0'.
- Elements of *regionCodes* will be pairwise distinct.

## Examples
### Example 1
#### Input
<c>"441323200312060636",<br />["441323"]</c>
#### Output
<c>"Male"</c>
#### Reason
As you can see, region code, birthday code and sequential code are all valid. So we just need to check the equation of checksum code:
6 + 4*2^(17) + 4*2^(16) + 1*2^(15) + 3*2^(14) + 2*2^(13) + 3*2^(12) + 2*2^(11) + 0*2^(10) + 0*2^(9) + 3*2^(8) + 1*2^(7) + 2*2^(6) + 0*2^(5) + 6*2^(4) + 0*2^(3) + 6*2^(2) + 3*2^(1) = 902276. It's easy to verify that 902276 mod 11 = 1. The sequential code ("063") is odd, thus this is a male.

### Example 2
#### Input
<c>"62012319240507058X",<br />["620123"]</c>
#### Output
<c>"Female"</c>
### Example 3
#### Input
<c>"321669197204300886",<br />["610111","659004"]</c>
#### Output
<c>"Invalid"</c>
#### Reason
Region code '321669' is invalid.

### Example 4
#### Input
<c>"230231198306900162",<br />["230231"]</c>
#### Output
<c>"Invalid"</c>
#### Reason
Birthday code '19830690' is invalid.

### Example 5
#### Input
<c>"341400198407260005",<br />["341400"]</c>
#### Output
<c>"Invalid"</c>
#### Reason
Sequential code '000' is invalid.

### Example 6
#### Input
<c>"520381193206090891",<br />["532922","520381"]</c>
#### Output
<c>"Invalid"</c>
#### Reason
Checksum code is incorrect.


"""
def isLeapYear( year ):
    #- A year is a leap year if and only if it satisfies one of the following two conditions: 
    #A: It is a multiple of 4, but not a multiple of 100. 
    #B: It is a multiple of 400.
    if year % 400 == 0:
        return True
    if ( year % 4 == 0 ) and ( year % 100 != 0 ):
        return True
    return False

def verifyDate( year, month, day ):
    if not ( 1900 <= year <= 2011 ):
        return False
    if not ( 1 <= month <= 12 ):
        return False
    if not 1 <= month <= 12:
        return False
    if not 1 <= day <= 31:
        return False
    if month in ( 1, 3, 5, 7, 8, 10, 12 ):
        return day <= 31
    if month in ( 4, 6, 9, 11 ):
        return day <= 30
    assert month == 12 or month == 2, month
    if isLeapYear( year ):
        return day <= 29
    else:
        return day <= 28

def computeSum( ID ):
    total = 0
    mult = 2
    m = 11
    for i in range( len( ID )-2, -1, -1 ):
        n = int( ID[i] )
        total += n*mult
        total %= m
        mult *= 2
        mult %= m
    return total

def verify(ID, regionCodes):
    region = ID[ 0:6 ]
    if region not in regionCodes:
        return "Invalid"
    bday = ID[ 6:6+8 ]
    year = int( bday[ 0:4 ] )
    month = int( bday[ 4:6 ] )
    day = int( bday[ 6:8 ] )
    if not verifyDate( year, month, day ):
        return "Invalid"
    code = int( ID[ 14:17 ] )
    if code == 0:
        return "Invalid"
    isMale = ( code % 2 == 1 )
    errorCode = ID[ -1 ]
    if errorCode == 'X':
        errorCode = 10
    else:
        errorCode = int( errorCode )
    s = computeSum( ID ) + errorCode
    s %= 11
    if s == 1:
        return "Male" if isMale else "Female"
    else:
        return "Invalid"
