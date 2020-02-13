#xls
# openpyxl 处理xlsx格式

from openpyxl.reader.excel import load_workbook


def readXlsxFile(path):
    # 得到整张表
    file = load_workbook(filename=path)
    print(file.get_sheet_names())




path = r"GeoLite2-ASN-Blocks-IPv4.xlsx"
readXlsxFile(path)