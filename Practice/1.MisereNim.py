from functools import reduce
def misereNim(pile):
    if set(pile) == {1}:
        if len(pile)%2 == 0:
            return 'First'
        else:
            return 'Second'

    res = reduce((lambda x, y: x ^ y), pile)
    if res == 0:
        return 'Second'
    else:
        return 'First'