def remove_dipls(reference, removable):
    for i in reference:
        for j in removable:
            if i == j:
                removable.remove(j)
                break
    return removable


def union(toret, otro):
    for i in otro:
        is_diferent = True
        for j in toret:
            if j == i:
                is_diferent = False
                break
        if is_diferent:
            toret.add(i)
    return toret
