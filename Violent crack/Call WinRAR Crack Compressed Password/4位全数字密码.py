#不生成密码本破解：
#4位全数字密码：
import os,time
def Jy():
    print('开始破解：')
    for i in range(10000):
        myStr=str(i).zfill(4)#生成压缩包密码
        #这里修改WinRAR.exe所在路径、压缩包路径和解压目录（C:\Program Files (x86)\WinRAR\WinRAR.exe、52pojie.rar、52pojie）
        jy=r'"C:\Program Files (x86)\WinRAR\WinRAR.exe" -ibck -y x -p%s 52pojie.zip 52pojie'%myStr
        if os.system(jy)==0:
            print('密码正确!',myStr)
            ent=time.time()
            print('破解成功！用时%f分'%((ent-stm)/60))
            return
        else:
            print('密码错误：',myStr)
    ent=time.time()
    print('破解失败，用时%f分'%((ent-stm)/60))
stm=time.time()
if os.path.exists('52pojie')==False:#判断当前py文件所在目录下是否存在52pojie文件夹，如果没有则建立
    os.mkdir('52pojie')
Jy()