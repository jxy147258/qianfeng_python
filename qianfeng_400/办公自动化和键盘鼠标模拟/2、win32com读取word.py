import win32com
import win32com.client
import os

def readWordfile(path):
    # 先调用word应用
    mw = win32com.client.Dispatch("Word.Application")
    # 再用word应用打开word文档
    doc = mw.Documents.Open(path)
    # 最后读取word内容
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    # 另存为
    doc.SaveAs(toPath,2)  # 2表示另存为的格式为普通txt
    # 关闭文件
    doc.Close()
    # 退出word
    mw.Quit()



# 测试读取
path = r"F:\python_G\python_shell\qianfeng_400\办公自动化和键盘鼠标模拟\sunk.doc"
toPath = r"F:\python_G\python_shell\qianfeng_400\办公自动化和键盘鼠标模拟\a.txt"
readWordfile(path)



