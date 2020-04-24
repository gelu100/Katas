def get_min_max(seq):
#Implement a function that returns the minimal and the maximal value of a list (in this order).
    list=[]
    list.append(min(seq))
    list.append(max(seq))
    return tuple(list)