def timeConversion(s):
    # Write your code here
    hour = int(s[:2])
    timeInfo = s[-2:]
    remaingInfo = s[2:-2]
    print(hour)
    print(timeInfo)
    time24h = ""
    if timeInfo == "PM":
        if hour < 12:
            time24h = str(hour + 12) + remaingInfo
        else: time24h = str(hour) + remaingInfo
    else:
        if hour == 12:
            time24h = "00" + remaingInfo
        else: time24h = s[: -2]

    return (time24h)


timeConversion("02:01:00PM")