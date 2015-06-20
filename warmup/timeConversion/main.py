#https://www.hackerrank.com/challenges/time-conversion/

time = raw_input()
hour, rest = time.split(":", 1)
hour = int(hour)
pm = time[-2:] == 'PM'
if hour == 12:
    pm = not pm
if not pm:
    print time[:-2]
else:
    hour += 12
    if hour >= 24:
        hour -= 24
    print "%02d:%s" % (hour, str(rest[:-2]))


