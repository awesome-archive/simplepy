import os,re,requests
def main():
    i=int(input('输入数字：\n1、查询本机ip\n2、查询公网ip\n'))
    if i==1:
        os.system('ipconfig /all >ip.txt&find "IPv4 地址" ip.txt')
        os.remove('ip.txt')
    elif i==2:
        resp=requests.get('https://2021.ip138.com',headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)''AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/83.0.4103.97 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;''q=0.9,image/webp,image/apng,*/*;''q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'})
        ip=re.findall(r'>(.+)</a>](.+)',resp.text)
        print(' '.join(ip[0]))
    else:
        print('请输入对应数字！')
main()
while True:
    i=input('是否继续？q：退出，其它：继续\n')
    if i=='q':
        break
    else:
        main()