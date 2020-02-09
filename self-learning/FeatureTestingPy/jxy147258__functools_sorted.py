L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#
#
# 自己的想法是先拿到列表里每一个元素的第一个值，就是名字，
# 然后排序，根据排序结果，再重新组装
# L1 = []
# def by_name(t):
#     for t_key in t:
#         L1.append(t_key[0])
#         L2 = sorted(L1)
#     return L2
#
#
# L2 = sorted(L, key=by_name)
# print(L2)


# 通过名字排序的正确做法
# def by_name(t):
#     return t[0]  # t[0]的值是('Adam',92)
#
#
# L2 = sorted(L, key=by_name)
# print(L2)


# 通过分数排序的正确做法
# def by_score(t):
#     return t[1]
#
#
# L2 = sorted(L, key=by_score)
# print(L2)