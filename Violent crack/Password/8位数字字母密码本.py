#8位数字字母密码本：
import time
stm=time.time()
dic = open('password.txt', 'a')#在当前py文件所在目录生成password.txt文件
str='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'#这里加上你想要的字符
for a in range(len(str)):
    for b in range(len(str)):
        for c in range(len(str)):
            for d in range(len(str)):
                for e in range(len(str)):
                    for f in range(len(str)):
                        for g in range(len(str)):
                            for h in range(len(str)):
                                pwd=str[a]+str[b]+str[c]+str[d]+str[e]+str[f]+str[g]+str[h]#生成8位数字字母密码，通过增加/删除for语句并且在这句后面加上/删除相应的str来自定义密码位数
                                dic.write(pwd)
                                dic.write('\n')
                                print('密码正在写入文件：',pwd)
dic.close()
ent = time.time()
print('成功生成密码本！用时%f分'%((ent - stm)/60))