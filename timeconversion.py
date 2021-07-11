#Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


def timeConversion(s):
    meridian=s[-2:] 
    if meridian=='PM' and s[:2]!='12':
        s=str(12 + int(s[:2]))+s[2:]
    if meridian=='AM' and s[:2]=='12':
        s='00'+s[2:]
    return s[:-2]
