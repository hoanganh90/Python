def dayOfProgrammer(year):
    # Write your code here
    if year <= 1917 and year >= 1700:
        if year %4 == 0:
            day256th = 256 - 244
            result = str(day256th) + ".09." + str(year)
            return result
        else:
            day256th = 256 - 243
            result = str(day256th) + ".09." + str(year)
            return result
    elif year == 1918:
        day256th = 256 - (31 + 15 + 31 + 30 + 31 + 30 + 31 + 31) 
        result = str(day256th) + ".09." + str(year)
        return result 
    else:   
        if year % 400 == 0 or (year %4 == 0 and not year % 100 == 0):
            day256th = 256 - 244
            result = str(day256th) + ".09." + str(year)
            return result
        else:
            day256th = 256 - 243
            result = str(day256th) + ".09." + str(year)
            return result
print(dayOfProgrammer(1918))