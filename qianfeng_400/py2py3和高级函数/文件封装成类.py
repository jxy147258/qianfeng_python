import  csv
import win32com
import win32com.client

class DealFile(object):

    # 读CSV文件
    def readCsvInfo(self,readpath):
        infoList = []
        with open(readpath, "r") as f:
            reader = csv.reader(f)
            for rowData in reader:
                infoList.append(rowData)
        return infoList


    # 写CSV过程
    def writeCsvInfo(self,writepath, data):
        with open(writepath, "w") as f:
            wirter = csv.writer(f)
            for rowData in data:
                wirter.writerow(rowData)

    def readWordfile(self,path,topath=""):
        mw = win32com.client.Dispatch("Word.Application")
        doc = mw.Documents.Open(path)
        for paragraph in doc.Paragraphs:
            line = paragraph.Range.Text
        if topath == "":
            return line
        else:
            doc.SaveAs(path, 2)  # 2表示另存为的格式为普通txt
            # 关闭文件
            # doc.Close()
            # 退出word
            mw.Quit()



readpath = r"F:\python_G\python_shell\qianfeng_400\办公自动化和键盘鼠标模拟\aa11.csv"
wirtePath = r"aa12.csv"
datalist = [["123", "456", "789"],["aaa","bbb","ccc"]]
d = DealFile()
print(d.readCsvInfo(readpath))
