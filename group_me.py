
def mod_three(num):
    return num % 3


def group(f, x):
    dic = {}
    for i in range(0, len(x)):
        val = f(x[i])
        dic[val] = dic.get(val, []) + [x[i]]
    return dic


print(group(mod_three, [1, 3, 4, 5, 7, 9]))
