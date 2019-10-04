def intersect(list1,list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result
