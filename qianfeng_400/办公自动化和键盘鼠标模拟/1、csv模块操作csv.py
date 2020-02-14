# 读CSV文件

import csv

# 读过程
readpath = r"aa11.csv"
def readCsvInfo(readpath):
    infoList = []
    with open(readpath,"r") as f:
        allFileInfo = csv.reader(f)
        for row in allFileInfo:
            infoList.append(row)
    return infoList

infolist = readCsvInfo(readpath)
for item in infolist:
    print(item)

# 写过程
def writeCsvInfo(path,data):
    with open(path,"w") as f:
        wirter = csv.writer(f)
        for rowData in data:
            wirter.writerow(rowData)

wirtePath = r"aa12.csv"
datalist = ["123","456","789"]
writeCsvInfo(wirtePath,datalist)
