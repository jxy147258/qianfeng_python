'''
人
类名：Person
属性：姓名 身份证号 电话号 卡
方法：开户 查询 取款 存储 转账 改密 锁定 解锁 补卡 销户

卡
类名：Card
属性：卡号 密码  余额
方法：

银行
类名：Bank
属性：用户列表 提款机
方法：

提款机
类名：ATM
属性：卡号 密码  余额
方法：开户 查询 取款 存储 转账 改密 锁定 解锁 补卡 销户 退出

界面
类名：View
属性：
行为：管理员届满 管理员登陆 系统功能界面
'''
import time
import random
import  pickle
import os

class Admin(object):
    #开机界面
    def printAdminview(self):
        print("**************************")
        print("****银行自动提款机系统****")
        print("**************************")

    def printsysFunctionview(self):
        print("**************************")
        print("*****开户(1)**查询(2)*****")
        print("*****取款(3)**存款(4)*****")
        print("*****转账(5)**改密(6)*****")
        print("*****锁定(7)**解锁(8)*****")
        print("*****补卡(9)**销户(0)*****")
        print("**********退出(t)*********")
        print("**************************")

    def adminOption(self):
        admin = "1"
        passwd = "1"
        inputadmin = input("输入管理员账号：")
        if not admin == inputadmin :
            print("用户名错误！！")
            return  -1

        inputpasswd = input("输入管理员密码：")
        if not passwd == inputpasswd :
            print("密码错误！！")
            return  -1
        time.sleep(2)
        print("操作成功，请稍后。。。。")
        return 0

class ATM(object):
    def __init__(self,allUsers):
        self.allUsers = allUsers
    def createUser(self): # 向用户字典中写入键值对（卡号-用户）
        name = input("姓名：")
        idCard = input("身份证号：")
        phone = input("电话号：")
        prestoreMoney = int(input("预存款："))
        if prestoreMoney < 0 :
            print("预存款有误,开户失败")
            return -1
        #两次输入密码，并且一致才行
        onePasswd = input("第一次输入密码：")
        if not self.checkPasswd(onePasswd):
            print("密码错误，开户失败")
            return -1
        cardStr = self.randomCardId()

        card = Card(cardStr,onePasswd,prestoreMoney)
        user = Users(name,idCard,phone,card)
        #存入字典
        self.allUsers[cardStr]  = user
        print("开户成功，卡号：%s"%(cardStr))
    def searchUser(self):
        # 输入一个卡号，验证以下存在与否
        cardNum = input("输入要查询的卡号：")
        user = self.allUsers.get(cardNum)
        if not user:
            print("卡号不存在")
            return -1
        if user.card.cardLock:
            print("该卡已经被锁定，请先解锁")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码错误，该卡已经被锁定，请先解锁")
            user.card.cardLock = True
            return -1
        print("账号：%s  余额：%s"%(user.card.cardID,user.card.cardMoney))
    def getMoney(self):
        # 输入一个卡号，验证以下存在与否
        cardNum = input("输入要查询的卡号：")
        user = self.allUsers.get(cardNum)
        if not user:
            print("卡号不存在，取款失败")
            return -1
        if user.card.cardLock:
            print("该卡已经被锁定，请先解锁")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码错误")
            user.card.cardLock = True
            return -1
        money = int(input("请输入取款数:"))
        if money > user.card.cardMoney:
            print("余额不足，取款失败")
            return -1
        if money <= 0:
            print("取款金额输入错误")
            return -1
        #取款
        user.card.cardMoney -= money
        print("取款成功，余额：%d"%(user.card.cardMoney))
    def saveMoney(self):
        pass
    def transferMoney(self):
        pass
    def changePasswd(self):
        pass
    def lock(self):
        # 输入一个卡号，验证以下存在与否
        cardNum = input("输入要查询的卡号：")
        user = self.allUsers.get(cardNum)
        if not user:
            print("卡号不存在,锁定失败")
            return -1
        if user.card.cardLock:
            print("已经被锁定，请先解锁")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码错误，锁定失败")
            return -1
        tempIdCard = input("请输入您的身份证号：")
        if tempIdCard != user.idCard:
            print("身份证号错误，锁定失败")
            return -1
        # 锁它
        user.card.cardLock = True
        print("锁定成功")
    def unlock(self):
        # 输入一个卡号，验证以下存在与否
        cardNum = input("输入要查询的卡号：")
        user = self.allUsers.get(cardNum)
        if not user:
            print("卡号不存在,解锁失败")
            return -1
        if not user.card.cardLock:
            print("此卡没有被锁定")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码错误，解锁失败")
            return -1
        tempIdCard = input("请输入您的身份证号：")
        if tempIdCard != user.idCard:
            print("身份证号错误，解锁失败")
            return -1
        #解锁
        user.card.cardLock = False
        print("解锁成功")
    def newcard(self):
        pass
    def killUser(self):
        pass
    # 验证密码
    def checkPasswd(self,realPasswd):
        for i in range(3):
            tempPasswd = input("再次输入密码：")
            if tempPasswd ==realPasswd:
                return True
        return False
    #生成卡号
    def randomCardId(self):
        # 随机生成卡号，本次实验只用到数字，所以随机大小写字母被注释掉
        while  True:
            str = ""
            for i in range(6):
                # ty = random.randrange(3)
                # if ty == 0:
                #     # 随机生成大写字母
                #     ch = chr(random.randrange(ord("A"), ord("Z") + 1))
                #     str += ch
                # elif ty == 1:
                #     # 随机生成小写字母
                #     ch = chr(random.randrange(ord("a"), ord("z") + 1))
                #     str += ch
                # else:
                # 随机生成数字
                ch = chr(random.randrange(ord("0"), ord("9") + 1))
                str += ch
                # 判断重复
            if not self.allUsers.get(str):
                return str
class Users(object):
    def __init__(self,name,idCard,phone,card):
        self.name = name
        self.idCard = idCard
        self.phone = phone
        self.card = card

class Card(object):
    def __init__(self,cardID,cardPasswd,cardMoney):
        self.cardID = cardID
        self.cardPasswd = cardPasswd
        self.cardMoney = cardMoney
        self.cardLock = False
def main():
    admin = Admin()
    admin.printAdminview()
    if admin.adminOption():
        return -1

    #card = Card()
    #user = Users()
    filepath = os.path.join(os.getcwd(), "allUsers.txt")
    with  open(filepath, "rb") as fr:
        allUsers = pickle.load(fr)
    print(allUsers)
    atm = ATM(allUsers)



    while True:
        admin.printsysFunctionview()
        option = input("请输入操作：")
        if option == "1":
            print("开户")
            atm.createUser()
        elif option == "2":
            atm.searchUser()
        elif option == "3":
            atm.getMoney()
        elif option == "4":
            print("存款")
        elif option == "5":
            print("转账")
        elif option == "6":
            print("改密")
        elif option == "7":
            atm.lock()
        elif option == "8":
            atm.unlock()
        elif option == "9":
            print("补卡")
        elif option == "0":
            print("销户")
        elif option == "t":
            if not admin.adminOption():
                # 将当前系统用的用户信息保存到文件中
                with open(filepath, "wb") as fw:
                    pickle.dump(atm.allUsers,fw)
                    fw.close()
                    return -1
        # else:
        #     print("输入错误，请重新输入")


if __name__ == "__main__":
    main()