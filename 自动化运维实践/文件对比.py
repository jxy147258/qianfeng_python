import difflib

text1 = """123
abc
456
def
789
ghi"""
text1_lines = text1.splitlines()
text2 = """124
abc
454
def 3
789"""
text2_lines = text2.splitlines()

# d = difflib.Differ()
# diff = d.compare(text1_lines, text2_lines)
# print("\n".join(list(diff)))
d = difflib.HtmlDiff()
print(d.make_file(text1_lines,text2_lines))


#字符串所有的方法和属性
print("jixiaoyun".__getattribute__("join"))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
# 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
# 'title', 'translate', 'upper', 'zfill']