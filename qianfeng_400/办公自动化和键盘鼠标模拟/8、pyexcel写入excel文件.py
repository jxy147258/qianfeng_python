from collections import OrderedDict

# 可以读取xls和xlsx两种，但是只能写xls
from pyexcel_xls import  save_data

def makeExcelFile(path,data):
    dictXlsx = OrderedDict()

    for sheetNmame,sheetValue in data.items():
        d = {}
        d[sheetNmame] = sheetValue # 把整张表一下就整体写入
        dictXlsx.update(d)
    save_data(path,dictXlsx)

path = r"aa15.xls" # 也可以读xls文件
makeExcelFile(path,{"表1":[[1,2,3],[4,5,6],[7,8,9]],"表2":[[11,22,33],[44,55,66],[77,88,99]]})