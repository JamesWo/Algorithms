# source from
# https://www.hackerrank.com/contests/springsprint/challenges/the-time-in-words
# 2015 hackerrank spring sprint

# Enter your code here. Read input from STDIN. Print output to STDOUT'
hour = input()
minute = input()

intToStr = {0:"",
            1:"one",
            2:"two",
            3:"three",
            4:"four",
            5:"five",
            6:"six",
            7:"seven",
            8:"eight",
            9:"nine",
            10:"ten",
            11:"eleven",
            12:"twelve",
            13:"thirteen",
            14:"fourteen",
            15:"fifteen",
            16:"sixteen",
            17:"seventeen",
            18:"eighteen",
            19:"nineteen",
            20:"twenty",
            21:"twenty one",
            22:"twenty two",
            23:"twenty three",
            24:"twenty four",
            25:"twenty five",
            26:"twenty sx",
            27:"twenty seven",
            28:"twenty eight",
            29:"twenty nine"
            }

intToStrHour = {0:"",
            1:"one",
            2:"two",
            3:"three",
            4:"four",
            5:"five",
            6:"six",
            7:"seven",
            8:"eight",
            9:"nine",
            10:"ten",
            11:"eleven",
            12:"twelve",
            13:"one"
            }

if minute == 0:
    print "%s o' clock" % intToStrHour[hour]
elif minute==1:
    print "%s minute past %s" % ("one", intToStrHour[hour])
elif minute == 15:
     print "quarter past %s" % (intToStrHour[hour])
elif minute==30:
    print "half past %s" % intToStrHour[hour]        
elif minute == 45:
     print "quarter to %s" % (intToStrHour[hour+1])    
    
elif minute <= 29:
    print "%s minutes past %s" % (intToStr[minute], intToStrHour[hour])
elif minute >= 31:
    minLeft = 60-minute
    print "%s minutes to %s" % (intToStr[minLeft], intToStrHour[hour+1])


#print intToStr
