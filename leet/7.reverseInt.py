# reverse an integer.  x=123, rev(x)=321
# no coverting to other data structures and calling reverse()...

def rev(x):
    result = 0
    digit = 0
    while x > 0:
        digit += 1
        # get the lowest significant digit
        remainder = x % 10
        result *= 10
        result += remainder
        x = x / 10
    return result


# test

inp = {
        123:321,
        111:111,
        32:23,
        100:1,
        505:505,
        506:605,
        1234567:7654321,
        }

for i, expected in inp.iteritems():
    result = rev(i)
    assert result == expected, "%s %s %s" % ( i, result, expected )

