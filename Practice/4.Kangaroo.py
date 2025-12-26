def kangaroo(x1, v1, x2, v2):
    if x1 > x2 and v1 >= v2:
        return "NO"
    elif x1 < x2 and v1 <=v2:
        return "NO"
    jump = 0
    previous_distance = abs(x1-x2)
    result = False
    while(True):
        distance = abs(x1 + v1*jump - (x2 + v2*jump))
        if distance > 0:
            jump += 1
        if distance == 0:
            result = True
            break
        if previous_distance >= distance:
            previous_distance = distance
        else:
            break
    return "YES" if result == True else "NO"
print(kangaroo(43, 2, 70, 2))
        