#不生成密码本破解：
#4位全数字密码：
import time
from unrar import rarfile
def readpassword():
    for i in range(10000):
        myStr=str(i).zfill(4)#生成4位全数字密码
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
readpassword()