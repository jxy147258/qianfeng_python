# !/home/jixy2/pycharm_projects/qianfeng_python-master/venv/bin/python
# -- coding:utf-8 --


import sys
import difflib


def readFile(filename):
    with open(filename) as finalhandler:
        text = finalhandler.read().splitlines()
        return text


try:
    textFile1 = sys.argv[1]
    textFile2 = sys.argv[2]
except Exception as e:
    print("Error: "+str(e))
    sys.exit()


if textFile1 == "" or textFile2 == "":
    print("Uage is :python3 file1 file2")
    sys.exit()
else:
    textLines1 = readFile(textFile1)
    textLines2 = readFile(textFile2)

d = difflib.HtmlDiff()
print(d.make_file(textLines1, textLines2))


    
