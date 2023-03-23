def minimum(list):
    if len(list) == 1:
        return list[0]
    else:
        if list[0] < minimum(list[1:]):
            return list[0]
        else:
            return minimum(list[1:])
