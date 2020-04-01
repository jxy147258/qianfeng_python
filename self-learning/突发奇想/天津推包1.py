import os
import sys
import re
import poplib
import base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import email
import time


def get_email_content():
    useraccount = 'jixy2@yusys.com.cn'
    password = 'Yusys@123'
    # useraccount = 'yxjfyw@yusys.com.cn'
    # password = '1qaz!QAZ'

    # 邮件服务器地址
    pop3_server = 'mail.yusys.com.cn'

    # 开始连接到服务器
    server = poplib.POP3(pop3_server)

    # 打开或者关闭调试信息，1为打开，会在控制台打印客户端与服务器的交互信息
    server.set_debuglevel(1)

    # 打印POP3服务器的欢迎文字，验证是否正确连接到了邮件服务器
    print(server.getwelcome().decode('utf8'))

    # 开始进行身份验证
    server.user(useraccount)
    server.pass_(password)

    # 返回是一个列表，第一项是一共有多少封邮件，第二项是共有多少字节
    # email_num, email_size = server.stat()
    # print("消息的数量: {0}, 消息的总大小: {1}".format(email_num, email_size))

    # 使用list()返回所有邮件的编号，默认为字节类型的串
    rsp, msg_list, rsp_siz = server.list()
    # print("服务器的响应: {0},\n消息列表： {1},\n返回消息的大小： {2}".format(rsp, msg_list, rsp_siz))
    print('邮件总数： {}'.format(len(msg_list)))

    # 下面单纯获取最新的一封邮件
    # total_mail_numbers = len(msg_list)
    rsp, msglines, msgsiz = server.retr(len(msg_list))
    # linux下是\n
    print()
    # TODO 现在是原始邮件变成二进制的时候编码有问题
    msg_content = b'\n'.join(msglines).decode(visualcharset)
    msg = Parser().parsestr(text=msg_content)

    # print("服务器的响应: {0},\n邮件内容：{1},\n该封邮件所占字节大小： {2}".format(rsp, msglines, msgsiz))

    # msg_content = b'\r\n'.join(msglines).decode('gbk')  # windows下是\r\n
    # msg_content = b'\n'.join(msglines).decode('utf-8')  # linux下是\n
    # msg = Parser().parsestr(text=msg_content)
    # print('解码后的邮件信息:\n{0}'.format(msg))

    # 关闭与服务器的连接，释放资源
    server.close()

    return msg


# 解析主题
def parser_subject(msg):
    subject = msg['Subject']
    value, charset = decode_header(subject)[0]
    if charset:
        value = value.decode(charset)
    print('邮件主题： {0}'.format(value))
    return value


# 解析发件人
def parser_address(msg):
    hdr, addr = parseaddr(msg['From'])
    # name 发送人邮箱名称， addr 发送人邮箱地址
    name, charset = decode_header(hdr)[0]
    if charset:
        name = name.decode(charset)
    print('发送人邮箱名称: {0}，发送人邮箱地址: {1}'.format(name, addr))
    cclist = decode_header(msg.get("Cc", ""))
    for m in range(len(cclist)):
        if cclist[m][1]:
            print(cclist[m][0].decode(cclist[m][1]), end="\n")
        else:
            print(cclist[m][0], end="\n")


# 解析内容
def parser_content(msg):
    content = msg.get_payload()
    text = content[0].as_string().split('base64')[-1]
    base64text = base64.b64decode(text)
    visualcharset = re.search(r"^charset=(.*?):$")
    visualtext = base64text.decode(visualcharset)
    print(visualtext)




while True:
    msg = get_email_content()
    parser_subject(msg)
    parser_address(msg)
    parser_content(msg)
    time.sleep(10)

