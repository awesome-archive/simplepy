import os,webbrowser
def main():
    keystr=input('输入关键字：\n')
    print('0、所有分类\n1、搜索\n2、百科\n3、社交\n4、购物\n5、视频\n6、图片\n7、翻译\n8、代码')
    num=int(input('选择分类：\n'))
    if num==0:
        l=lss+lbk+lsj+lgw+lsp+ltp+lfy+ldm
        for i in l:
            url=i%keystr
            webbrowser.open(url,new=0)
    elif num==1:
        for i in lss:
            url=i%keystr
            webbrowser.open(url,new=0)
    elif num==2:
        for i in lbk:
            url=i%keystr
            webbrowser.open(url,new=0)
    elif num==3:
        for i in lsj:
            url=i%keystr
            webbrowser.open(url,new=0)
    elif num==4:
        for i in lgw:
            url=i%keystr
            webbrowser.open(url,new=0)
    elif num==5:
        for i in lsp:
            url=i%keystr
            webbrowser.open(url,new=0)
    elif num==6:
        for i in ltp:
            url=i%keystr
            webbrowser.open(url,new=0)
    elif num==7:
        for i in lfy:
            url=i%keystr
            webbrowser.open(url,new=0)
    elif num==8:
        for i in ldm:
            url=i%keystr
            webbrowser.open(url,new=0)
    else:
        print('请输入对应数字！')
#搜索类，可以添加或者删除，注意关键词位置用%s代替
lss=[
    'https://www.baidu.com/s?wd=%s',
    'https://www.sogou.com/web?query=%s',
    'http://www.bing.com/search?q=%s',
    'https://www.yandex.com/search/?text=%s'
     ]
#百科类，可以添加或者删除，注意关键词位置用%s代替
lbk=[
    'https://baike.baidu.com/search?word=%s',
    'https://www.sogou.com/sogou?query=%s&insite=baike.sogou.com',
    'https://zh.moegirl.org/index.php?search=%s',
    'https://zh.wikihow.com/wikiHowTo?search=%s'
    ]
#社交类，可以添加或者删除，注意关键词位置用%s代替
lsj=[
    'https://m.weibo.cn/p/100103type=1&q=%s',
    'https://www.zhihu.com/search?type=content&q=%s'
    ]
#购物类，可以添加或者删除，注意关键词位置用%s代替
lgw=[
    'https://search.jd.com/Search?enc=utf-8&keyword=%s',
    'https://s.taobao.com/search?tab=mall&q=%s',
    'https://s.taobao.com/search?q=%s',
    'https://search.suning.com/%s/',
    'https://search.gome.com.cn/search?question=%s',
    'https://www.amazon.cn/s/%s',
    'http://search.dangdang.com/?key=%s'
    ]
#视频类，可以添加或者删除，注意关键词位置用%s代替
lsp=[
    'https://search.bilibili.com/all?keyword=%s',
    'http://so.youku.com/search_video/q_%s',
    'https://v.qq.com/x/search/?q=%s',
    'http://so.iqiyi.com/so/q_%s'
    ]
#图片类，可以添加或者删除，注意关键词位置用%s代替
ltp=[
    'http://image.baidu.com/search/index?tn=baiduimage&word=%s',
    'https://pic.sogou.com/pics?query=%s',
    'https://cn.bing.com/images/search?q=%s',
    'https://yandex.com/images/search?text=%s'
    ]
#翻译类，可以添加或者删除，注意关键词位置用%s代替
lfy=[
    'https://translate.google.cn/#auto/zh-CN/%s',
    'https://translate.google.cn/#auto/en/%s',
    'https://cn.bing.com/translator/?from=&to=zh-cn&text=%s',
    'https://cn.bing.com/translator/?from=&to=en&text=%s'
    ]
#代码类，可以添加或者删除，注意关键词位置用%s代替
ldm=[
    'https://github.com/search?q=%s',
    'https://search.gitee.com/?skin=rec&type=repository&q=%s',
    'https://caniuse.com/#search=%s'
    ]
main()
while True:
    i=input('是否继续？q：退出，其它：继续\n')
    if i=='q':
        break
    else:
        os.system('cls')
        main()