import numpy as np


def doubleSumSlice(a):
    sums = []
    for x in range(len(a)):
        for y in range(x + 1, len(a)):
            for z in range(y + 1, len(a)):
                part_1 = a[x + 1:y]
                part_2 = a[y + 1:z]
                sum_list = part_1 + part_2
                sum_ = np.sum(np.array(sum_list))
                sums.append(sum_)

    max_sum = max(sums)
    return max_sum


print(doubleSumSlice([3, 2, 6, -1, 4, 5, -1, 2]))
