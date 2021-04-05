#不生成密码本破解：
#4位数字字母密码：
import time
from unrar import rarfile
def readpassword():
    print('开始破解：')
    for a in range(len(str)):
        for b in range(len(str)):
            for c in range(len(str)):
                for d in range(len(str)):
                    myStr=str[a]+str[b]+str[c]+str[d]#生成4位密码
                    try:
                        file.extractall(path='52pojie',pwd=myStr)#解压到当前py文件所在目录下的52pojie文件夹内，修改path可自定义解压路径
                    except:
                        print('密码错误：',myStr)
                    else:
                        print('密码正确：',myStr)
                        ent=time.time()
                        print('破解成功！用时%f分'%((ent-stm)/60))
                        return
    ent=time.time()
    print('破解失败，用时%f分'%((ent-stm)/60))
stm=time.time()
file=rarfile.RarFile('52pojie.rar','r')#读取rar文件
str='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'#这里可以加上你想要的字符
readpassword()