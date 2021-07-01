def sum_array_index(arr, num):
    #print(arr,num)
    result = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == num:
                result += i
                result += j
    return result 

assert sum_array_index([2,3,4,5,6,7,8], 23) == 0
assert sum_array_index([2,3,4,5,6,7,8], 7) == 6
assert sum_array_index([2,9,4,5,6,7,9], 16) == 17