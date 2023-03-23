def reverse(list):
    if list == []:
        return []
    else:
        return [list[-1]] + reverse(list[:-1])
        #return reverse(list[1:]) + [list[0]]
