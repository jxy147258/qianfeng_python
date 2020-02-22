#L = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
L = list(range(2,100))
L1 = []
for each_iterm in L:
    if each_iterm % L[0] == 0:
        L.remove(each_iterm)
print(L)