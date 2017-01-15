k=6
list_k = [-2, 11, -4, 13, 1, -5, 6, -2, 1]
lisk_l = [-1, -2, -3]

def max_sub_suq(list_suq):
    sum, max_sum = 0, 0
    for i in list_suq:
        if sum + i >= 0:
            sum += i
        else:
            sum = 0

        max_sum = max(max_sum, sum)
    return max_sum

print(max_sub_suq(list_k))
print(max_sub_suq(lisk_l))