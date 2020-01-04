def brute(array, item):
    for i in range(len(array)):
        message = 'The item is not contained in the list'
        if array[i] == item:
            message = 'The item is in position ' + str(i)
            break
    return message

def binary(array, item):
    message = 'The item is not contained in the list'
    u = len(array)
    l = 0
    while l < u:
        mid = l + int((u - l - 1)/2)
        if array[mid] == item:
            message = 'The item is in position ' + str(mid)
            break
        elif array[mid] < item:
            l = mid + 1
        else:
            u = mid
    return message

test0 = [-3, 1, 3, 9, 11, 14, 22, 123, 302, 304, 434, 501, 1230, 5412, 381923]
searchItem0 = 13
print(brute(test0, searchItem0))
print(binary(test0, searchItem0))
test1 = [1, 7, 9, 12, 22, 43, 104]
searchItem1 = 9
print(brute(test1, searchItem1))
print(binary(test1, searchItem1))
test2 = [-20, -5, 0, 0, 30, 100]
searchItem2 = 31
print(brute(test2, searchItem2))
print(binary(test2, searchItem2))
test3 = [4, 17, 28, 30, 52, 61, 666, 1001]
searchItem3 = 666
print(brute(test3, searchItem3))
print(binary(test3, searchItem3))