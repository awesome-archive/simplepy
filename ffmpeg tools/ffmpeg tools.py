import os,shutil
def main():
    print('1、转换\n2、变速\n3、替换视频中的音频（视频路径在前，音频路径在后）\n4、合并相同格式的多个视频或相同格式的多个音频\n5、分离\n6、截取\n')
    i=int(input('输入分类对应的数字：\n'))
    infile=input('输入文件路径（多个路径用|隔开）：\n')
    if i==1:
        print('1、视频转换\n2、音频转换\n')
        i=int(input('输入分类对应的数字：\n'))
        if i==1 or i==2:
            outfile=input('输入名字（包含后缀名，可带路径）：\n')
            cmd='ffmpeg -i "%s" -c:v libx264 -preset ultrafast "%s"'%(infile,outfile)
            os.system(cmd)
        else:
            print('请输入对应数字！')
    elif i==2:
        print('1、视频变速\n2、音频变速\n')
        i=int(input('输入分类对应的数字：\n'))
        if i==1:
            bs=float(input('输入倍数（0.5-100内的数，大于1时加速，小于1时减速）：\n'))
            outfile=input('输入名字（包含后缀名，可带路径）：\n')
            cmd='ffmpeg -i "%s" -filter_complex "[0:v]setpts=%s*PTS[v];[0:a]atempo=%s[a]" -map "[v]" -map "[a]" "%s"'%(infile,1/bs,bs,outfile)
            os.system(cmd)
        elif i==2:
            bs=float(input('输入倍数（0.5-100内的数，大于1时加速，小于1时减速）：\n'))
            outfile=input('输入名字（包含后缀名，可带路径）：\n')
            cmd='ffmpeg -i "%s" -filter_complex atempo=%s "%s"'%(infile,bs,outfile)
            os.system(cmd)
        else:
            print('请输入对应数字！')
    elif i==3:
        outfile=input('输入名字（包含后缀名，可带路径）：\n')
        f1,f2=infile.split('|')
        cmd='ffmpeg -i "%s" -i "%s" -c:v copy -c:a copy -map 0:v:0 -map 1:a:0 "%s"'%(f1,f2,outfile)
        os.system(cmd)
    elif i==4:
        outfile=input('输入名字（包含后缀名，可带路径）：\n')
        n=0
        l=[]
        name=infile.split('|')
        with open('mergelist.txt','a') as file:
            for i in name:
                n+=1
                s='%s%s'%(n,os.path.splitext(i)[1])
                l.append(s)
                shutil.copy(i,s)
                file.write("file '%s'\n"%s)
        cmd='ffmpeg -f concat -i mergelist.txt -c copy "%s"'%outfile
        os.system(cmd)
        os.remove('mergelist.txt')
        for i in l:
            os.remove(i)
    elif i==5:
        print('1、从视频去除音频\n2、从视频分离完整音频\n')
        i=int(input('输入分类对应的数字：\n'))
        if i==1:
            outfile=input('输入名字（包含后缀名，可带路径）：\n')
            cmd='ffmpeg -i "%s" -an "%s"'%(infile,outfile)
            os.system(cmd)
        elif i==2:
            outfile=input('输入名字（包含后缀名，可带路径）：\n')
            cmd='ffmpeg -i "%s" -vn "%s"'%(infile,outfile)
            os.system(cmd)
        else:
            print('请输入对应数字！')
    elif i==6:
        print('1、从视频截取某时刻图片\n2、从视频制作gif\n3、截取某段视频\n4、从视频截取音频\n5、从音频截取音频\n')
        i=int(input('输入分类对应的数字：\n'))
        if i==1:
            st=input('输入开始时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：\n')
            outfile=input('输入名字（包含后缀名，可带路径）：\n')
            cmd='ffmpeg -i "%s" -ss %s -frames 1 "%s"'%(infile,st,outfile)
            os.system(cmd)
        elif i==2 or i==3 or i==4 or i==5:
            st=input('输入开始时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：\n')
            et=input('输入结束时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：\n')
            outfile=input('输入名字（包含后缀名，可带路径）：\n')
            cmd='ffmpeg -ss %s -to %s -i "%s" -c copy "%s"'%(st,et,infile,outfile)
            os.system(cmd)
        else:
            print('请输入对应数字！')
main()
while True:
    i=input('是否继续？q：退出，其它：继续\n')
    if i=='q':
        break
    else:
        main()