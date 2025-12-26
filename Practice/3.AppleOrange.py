def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    relativePos_apples = list(map(lambda apple: apple + a, apples))
    relativePos_orrange = list(map(lambda orange: orange + b, oranges))
    apples_count = 0
    oranges_count = 0
    for apple in relativePos_apples:
        if apple >= s and apple <= t:
            apples_count += 1
    for orange in relativePos_orrange:
        if orange >= s and orange <= t:
            oranges_count += 1
    print(f"{apples_count}\n{oranges_count}")
countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
countApplesAndOranges(7,10,4,12,[2,3,-4],[3, -2,-4])