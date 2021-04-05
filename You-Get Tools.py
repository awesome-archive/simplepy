import os,re,requests
def main():
    c=int(input('输入数字：\n1、单个网址\n2、多个网址\n3、Bilibili Up Download\n'))
    if c==1:
        url=input('输入网址：\n')
        n=int(input('输入数字：\n1、查看格式\n2、调用播放器在线播放\n3、下载（默认最高画质）\n4、选择画质下载\n5、获取真实地址（Real URLs:后面的地址）\n'))
        if n==1:
            cmd=r'you-get -i "%s"'%url
            os.system(cmd)
        elif n==2:
            cmd=r'you-get -p "%s" "%s"'%(playerpath,url)
            os.system(cmd)
        elif n==3:
            cmd=r'you-get -o "%s" "%s"'%(savepath,url)
            os.system(cmd)
        elif n==4:
            cmd=r'you-get -i "%s"'%url
            os.system(cmd)
            format=input('输入画质，画质是- format:后面的字符串（例如：mp4hd2v2，直接回车默认下载最高画质）：\n')
            cmd=r'you-get --format=%s -o "%s" "%s"'%(format,savepath,url)
            os.system(cmd)
        elif n==5:
            cmd=r'you-get -u "%s"'%url
            os.system(cmd)
        else:
            print('请输入对应数字！')
    elif c==2:
        files=input('输入保存网址的文本文件路径（一个网址占一行）：\n')
        with open(r'%s'%files) as file:
            for durl in file:
                durl=durl.replace('\n','')
                cmd=r'you-get -o "%s" "%s"'%(savepath,durl)
                os.system(cmd)
    elif c==3:
        upurl=input('输入Up主个人空间地址，类似于https://space.bilibili.com/8047632或者https://space.bilibili.com/8047632?from=search&seid=3287339846988974210或者https://space.bilibili.com/8047632?spm_id_from=333.788.b_765f7570696e666f.2\n')
        mid=re.findall(r'https://space.bilibili.com/(\d*)',upurl)[0]
        home=requests.get('https://space.bilibili.com/%s'%mid)
        upname=re.findall(r'<title>(.*)的个人空间',home.text)[0]
        u=int(input('输入数字：\n1、所有视频\n2、某个频道下的所有视频\n'))
        if u==1:
            pagehtml=requests.get('https://api.bilibili.com/x/space/arc/search?mid=%s'%mid)
            count=re.findall(r'{.*?,"ps":(\d*?),"count":(\d*?)}',pagehtml.text)
            pn=int(count[0][1])//int(count[0][0])+1
            print('正在下载%s的所有视频（共%s个视频）：'%(upname,count[0][1]))
            for page in range(1,pn+1):
                r=requests.get('https://api.bilibili.com/x/space/arc/search?mid=%s&pn=%s'%(mid,page))
                bvids=re.findall(r'"bvid":"(.+?)"',r.text)
                for bvid in bvids:
                    videohtml='https://www.bilibili.com/video/%s'%bvid
                    cmd=r'you-get -o "%s" "%s"'%(savepath,videohtml)
                    os.system(cmd)
        elif u==2:
            r=requests.get('https://api.bilibili.com/x/space/channel/index?mid=%s&guest=false&jsonp=jsonp&callback=__jp3'%mid,headers={'referer': 'https://space.bilibili.com/%s'%mid})
            columns=re.findall(r'"cid":(\d*?),"mid":\d*?,"name":"(.*?)"',r.text)
            if columns==[]:
                print('%s没有频道'%upname)
            else:
                print('%s的所有频道如下：'%upname)
                ltmp=[]
                for num,name in enumerate(columns):
                    print(num+1,name[1])
                    ltmp.append('https://space.bilibili.com/%s/channel/detail?cid=%s'%(mid,name[0]))
                i=int(input('输入频道对应的数字：\n'))
                cmd=r'you-get -o "%s" "%s"'%(savepath,ltmp[i-1])
                os.system(cmd)
        else:
            print('请输入对应数字！')
    else:
        print('请输入对应数字！')
savepath=r'D:\You-Get'#这里更改下载路径
playerpath="'C:\Program Files (x86)\Windows Media Player\wmplayer.exe'"#这里更改播放器路径，这里调用的是Windows Media Player
if os.path.exists(r'D:\You-Get')==False:
    os.mkdir(r'D:\You-Get')
    main()
else:
    main()
while True:
    i=input('是否继续？q：退出，其它：继续\n')
    if i=='q':
        break
    else:
        os.system('cls')
        main()