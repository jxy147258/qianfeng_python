L = list(range(101))
def ge_jiu(l):
    n = 0
    for i in list(l):
        if n == 9:
            print("\n")
            n = 0
        else:
            print(i,end=" ")
            n += 1
if __name__ == "__main__":
    ge_jiu(L)
