import win32com
import win32com.client

def makePPT(path):
    # 创建ppt应用对象
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True
    # 创建文件
    pptFile = ppt.Presentations.Add()
    # 创建页
    page1 = pptFile.Slides.Add(1,1) # 1,1表示（页数，类型）
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "sunck "
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = " sunck is a good man !"

    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()





path = r"F:\python_G\python_shell\qianfeng_400\办公自动化和键盘鼠标模拟\aa16.ppt"
makePPT(path)