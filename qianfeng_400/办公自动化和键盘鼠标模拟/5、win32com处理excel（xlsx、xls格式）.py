# 待测试
# from win32com.client import Dispatch
# import win32com.client
#
#
# class easyExcel:
#     """A utility to make it easier to get at Excel.    Remembering
#     to save the data is your problem, as is    error handling.
#     Operates on one workbook at a time."""
#
#     def __init__(self, filename=None):  # 打开文件或者新建文件（如果不存在的话）
#         self.xlApp = win32com.client.Dispatch('Excel.Application')
#         if filename:
#             self.filename = filename
#             self.xlBook = self.xlApp.Workbooks.Open(filename)
#         else:
#             self.xlBook = self.xlApp.Workbooks.Add()
#             self.filename = ''
#
#     def save(self, newfilename=None):  # 保存文件
#         if newfilename:
#             self.filename = newfilename
#             self.xlBook.SaveAs(newfilename)
#         else:
#             self.xlBook.Save()
#
#     def close(self):  # 关闭文件
#         self.xlBook.Close(SaveChanges=0)
#         del self.xlApp
#
#     def getCell(self, sheet, row, col):  # 获取单元格的数据
#         "Get value of one cell"
#         sht = self.xlBook.Worksheets(sheet)
#         return sht.Cells(row, col).Value
#
#     def setCell(self, sheet, row, col, value):  # 设置单元格的数据
#         "set value of one cell"
#         sht = self.xlBook.Worksheets(sheet)
#         sht.Cells(row, col).Value = value
#
#     def setCellformat(self, sheet, row, col):  # 设置单元格的数据
#         "set value of one cell"
#         sht = self.xlBook.Worksheets(sheet)
#         sht.Cells(row, col).Font.Size = 15  # 字体大小
#         sht.Cells(row, col).Font.Bold = True  # 是否黑体
#         sht.Cells(row, col).Name = "Arial"  # 字体类型
#         sht.Cells(row, col).Interior.ColorIndex = 3  # 表格背景
#         # sht.Range("A1").Borders.LineStyle = xlDouble
#         sht.Cells(row, col).BorderAround(1, 4)  # 表格边框
#         sht.Rows(3).RowHeight = 30  # 行高
#         sht.Cells(row, col).HorizontalAlignment = -4131  # 水平居中xlCenter
#         sht.Cells(row, col).VerticalAlignment = -4160  #
#
#     def deleteRow(self, sheet, row):
#         sht = self.xlBook.Worksheets(sheet)
#         sht.Rows(row).Delete()  # 删除行
#         sht.Columns(row).Delete()  # 删除列
#
#     def getRange(self, sheet, row1, col1, row2, col2):  # 获得一块区域的数据，返回为一个二维元组
#         "return a 2d array (i.e. tuple of tuples)"
#         sht = self.xlBook.Worksheets(sheet)
#         return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value
#
#     def addPicture(self, sheet, pictureName, Left, Top, Width, Height):  # 插入图片
#         "Insert a picture in sheet"
#         sht = self.xlBook.Worksheets(sheet)
#         sht.Shapes.AddPicture(pictureName, 1, 1, Left, Top, Width, Height)
#
#     def cpSheet(self, before):  # 复制工作表
#         "copy sheet"
#         shts = self.xlBook.Worksheets
#         shts(1).Copy(None, shts(1))
#
#     def inserRow(self, sheet, row):
#         sht = self.xlBook.Worksheets(sheet)
#         sht.Rows(row).Insert(1)
#
#     # 下面是一些测试代码。
#
#
# if __name__ == "__main__":
#     # PNFILE = r'c:/screenshot.bmp'
#     xls = easyExcel(r'd:\jason.li\Desktop\empty_book.xlsx')
#     # xls.addPicture('Sheet1', PNFILE, 20,20,1000,1000)
#     # xls.cpSheet('Sheet1')
#     xls.setCell('sheet1', 2, 'A', 88)
#     row = 1
#     col = 1
#     print("*******beginsetCellformat********")
#     # while(row<5):
#     #   while(col<5):
#     #       xls.setCellformat('sheet1',row,col)
#     #       col += 1
#     #       print("row=%s,col=%s" %(row,col))
#     #   row += 1
#     #   col=1
#     #   print("*******row********")
#     # print("*******endsetCellformat********")
#     # print("*******deleteRow********")
#     # xls.deleteRow('sheet1',5)
#     xls.inserRow('sheet1', 7)
#     xls.save()
#     xls.close()