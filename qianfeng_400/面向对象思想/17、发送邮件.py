#发邮件的库
import  smtplib
#邮件文本的库
from email.mime.text import MIMEText



#SMTP服务器地址
SMTPServer = "smtp.163.com"
#发邮件的邮箱地址
sender = "18500639286@163.com"
#发送者邮箱授权码
passwd = "147258jxy"

#邮件正文
message = "qqqqqq"
msg = MIMEText(message)
#邮件标题
msg["Subject"] = "一封信"
#发送者
msg["From"] = sender

#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer,25)
#登陆邮箱
mailServer.login(sender,passwd)
#发送邮件
mailServer.sendmail(sender,["18500639286@163.com","1162591945@qq.com"],msg.as_string())
#推出邮箱
mailServer.quit()

