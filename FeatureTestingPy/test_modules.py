def test_self(inargv):
    print(inargv)

def test_pro():
    test_self(90)

if __name__ == "__main__":
    test_pro()
