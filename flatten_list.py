def flatten_list(lst):

    if len(lst) == 0:
        return lst
    if isinstance(lst[0],list):
        return flatten_list(lst[0]) + flatten_list(lst[1:])
    return lst[:1] + flatten_list(lst[1:])

    

print(flatten_list([1,[2],[3],[4,5], [6],7]))     

    