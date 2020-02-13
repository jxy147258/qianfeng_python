import os
import win32com
import win32com.client


def makeWordFile(path, name):
    # 创建word文档并写入内容
    # 创建以人名为名称的word文档
    mw1 = win32com.client.Dispatch("Word.Application")
    # 让文档可见
    mw1.Visible = True
    # 创建文档

    for i in name:
        doc = mw1.Documents.Add()
        # 写内容，分两步
        # 1，定位到开头
        r = doc.Range(0, 0)
        # 2，开始写
        r.InsertAfter("尊敬的" + i + "您好")
        topath = os.path.join(path, i)
        doc.SaveAs(topath)
        doc.Close()
    # 退出word
    mw1.Quit()

# 测试写入
names = []
with open(r"F:\python_G\python_shell\qianfeng_400\办公自动化和键盘鼠标模拟\allNames.txt","r",encoding="utf-8") as f:
    for item in f.readlines():
        names.append(item.split("\n")[0])
        print(names)
path1 = r"F:\python_G\python_shell\qianfeng_400\办公自动化和键盘鼠标模拟"
makeWordFile(path1,names)