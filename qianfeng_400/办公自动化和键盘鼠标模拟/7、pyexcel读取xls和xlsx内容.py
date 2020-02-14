from collections import OrderedDict

# 可以读取xls和xlsx两种，但是只能写xls
from pyexcel_xls import  get_data

def readXlsAndXlsxFile(paht):
    dictXlsx = OrderedDict()

    #抓取数据
    xdata = get_data(path)
    for sheet in xdata:
        dictXlsx[sheet] = xdata[sheet]
    return dictXlsx




path = r"aa13.xlsx" # 也可以读xls文件
allData = readXlsAndXlsxFile(path)
print(allData)
print(len(allData))