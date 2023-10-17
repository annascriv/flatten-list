from flatten_list import flatten_list

def test_flatten_list():
    assert flatten_list([1,[2],[3,[4,5,[6]]],7]) == ([1,2,3,4,5,6,7])

def test_flatten_list2():
    assert flatten_list([1,2,[3,4,[5]],6]) == [1,2,3,4,5,6]

def test_flatten_list3():
    assert flatten_list([[1],[2,3],[4,[5],6,7],8,[9]]) == [1,2,3,4,5,6,7,8,9]

def test_flatten_list4():
    assert flatten_list([1,2,3,[4,5,6],7,[8,9],10,[11,12]]) == [1,2,3,4,5,6,7,8,9,10,11,12]