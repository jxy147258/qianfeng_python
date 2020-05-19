import dns.resolver
import os
import httplib2


ipList = []
# appDomain = "www.dfyusys.com"
appDomain = "www.baidu.com"


def get_ipList(domain=""):
    try:
        A = dns.resolver.query(domain, "A")
    except Exception as e:
        print("dns resolver error1:" + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            ipList.append(j.address)
    return True


def checkIP(ip):
    checkUrl = ip + ":80"
    getContent = ""
    httplib2.socket.setdefaulttimeout(5)
    conn = httplib2.HTTPConnection(checkUrl)

    try:
        conn.request("GET", "/", headers={"Host": appDomain})
        r = conn.getresponse()
        getContent = r.read(15)
    finally:
        if getContent == "<!doctype html>":
            print(ip + "[ok]")
        else:
            print(ip + "[error]")


if __name__ == '__main__':
    if get_ipList(appDomain) and len(ipList) > 0:
        for ip in ipList:
            checkIP(ip)
    else:
        print("dns resolver error")
