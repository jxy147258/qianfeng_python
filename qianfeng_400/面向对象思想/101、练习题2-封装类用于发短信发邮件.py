# #封装类，用于发短信发邮件
#
#
# # 发邮件的库
# import smtplib
# # 邮件文本的库
# from email.mime.text import MIMEText
#
#
# class Send163Email(object):
#     # 属性：
#     # 方法：
#     #   1，创建SMTP服务器
#     #   2，邮件正文
#     #   2，发送邮件
#
#
#
#
#     def __init__(self,sender,passwd):
#         # 发邮件的邮箱地址
#         self.sender = sender
#         # 发送者邮箱授权码
#         self.passwd = passwd
#
#     # 邮件正文
#     message = "qqqqqq"
#     msg = MIMEText(message)
#     # 邮件标题
#     msg["Subject"] = "一封信"
#     # 发送者
#     msg["From"] = sender
#     def sendmail(self):
#         # SMTP服务器地址
#         __SMTPServer = "smtp.163.com"
#         # 创建SMTP服务器
#          mailServer = smtplib.SMTP(__SMTPServer, 25)
#          # 登陆邮箱
#          mailServer.login(self.sender, self.passwd)
#         # 发送邮件
#          mailServer.sendmail(self.sender, ["18500639286@163.com", "1162591945@qq.com"], msg.as_string())
#         # 推出邮箱
#         mailServer.quit()
#
#
