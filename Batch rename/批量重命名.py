import os,glob,shutil
def main():
    path=input('输入要重命名的目录或者文件所在的目录路径：\n')
    os.chdir(path)
    print('1、重命名目录下具有相同关键词的目录\n2、重命名目录下具有相同关键词的文件\n3、重命名目录下的所有目录\n4、重命名目录下的所有文件\n5、重命名目录下的所有目录和文件\n6、替换目录名\n7、替换文件名\n8、替换目录和文件名\n')
    i=int(input('输入对应数字：\n'))
    n=0
    if i==1:
        keystr=input('输入关键词（只会重命名具有这些关键词的目录）：\n')
        tofile=input('输入你要的目录名：\n')
        fromstr='*%s*'%keystr
        for fromfile in glob.glob(fromstr):
            if os.path.isdir(fromfile):
                n+=1
                shutil.move(fromfile,tofile+str(n))
    elif i==2:
        keystr=input('输入关键词（只会重命名具有这些关键词的文件，可以是相同的后缀名）：\n')
        tofile=input('输入你要的文件名（无后缀名）：\n')
        tp=input('输入你要的后缀名（回车无后缀名）：\n')
        fromstr='*%s*'%keystr
        for fromfile in glob.glob(fromstr):
            if os.path.isfile(fromfile):
                n+=1
                shutil.move(fromfile,tofile+str(n)+'.'+tp)
    elif i==3:
        tofile=input('输入你要的目录名：\n')
        for fromfile in glob.glob('*'):
            if os.path.isdir(fromfile):
                n+=1
                shutil.move(fromfile,tofile+str(n))
    elif i==4:
        tofile=input('输入你要的文件名：\n')
        tp=input('输入你要的后缀名（回车无后缀名）：\n')
        for fromfile in glob.glob('*'):
            if os.path.isfile(fromfile):
                n+=1
                shutil.move(fromfile,tofile+str(n)+'.'+tp)
    elif i==5:
        tofile=input('输入你要的名字：\n')
        for fromfile in glob.glob('*'):
            n+=1
            shutil.move(fromfile,tofile+str(n))
    elif i==6:
        oldstr=input('输入目录中你要替换的字符：\n')
        newstr=input('输入替换后的字符：\n')
        for fromfile in glob.glob('*'):
            if os.path.isdir(fromfile):
                tofile=fromfile.replace(oldstr,newstr)
                shutil.move(fromfile,tofile)
    elif i==7:
        oldstr=input('输入文件中你要替换的字符：\n')
        newstr=input('输入替换后的字符：\n')
        for fromfile in glob.glob('*'):
            if os.path.isfile(fromfile):
                tofile=fromfile.replace(oldstr,newstr)
                shutil.move(fromfile,tofile)
    elif i==8:
        oldstr=input('输入你要替换的字符：\n')
        newstr=input('输入替换后的字符：\n')
        for fromfile in glob.glob('*'):
            tofile=fromfile.replace(oldstr,newstr)
            shutil.move(fromfile,tofile)
    else:
        print('请输入对应数字！\n')
main()
while True:
    i=input('是否继续？y：继续，其它：退出\n')
    if i=='y':
        main()
    else:
        break