import os,re,requests,sys,webbrowser
import tkinter as tk
from tkinter import messagebox
class rs:
    def openurl(self,event):
        link=self.lb.curselection()[0]
        url=self.tmp[link]
        webbrowser.open(url,new=0)
    def Bzw(self):
        self.tmp=[]
        bzw=tk.Toplevel()
        bzw.iconbitmap(iicon)
        bzw.title('b站全站日热榜')
        bzw.geometry('550x280')
        gd=tk.Scrollbar(bzw)
        gd.pack(side='right',fill='y')
        self.lb=tk.Listbox(bzw,width=230,font=('Arial',16),yscrollcommand=gd.set)
        self.lb.bind('<Double-Button-1>',self.openurl)
        resp=requests.get('https://www.bilibili.com/v/popular/rank/all')
        bzr=re.findall(r'"info"><a\shref="//(.+)"\starget="_blank"\sclass="title">(.*?)</a>',resp.text)
        for bz in bzr:
            self.lb.insert('end',bz[1])
            self.tmp.append(bz[0])
        self.lb.pack(side='left',fill='both')
        gd.config(command=self.lb.yview)
    def Wbw(self):
        self.tmp=[]
        wbw=tk.Toplevel()
        wbw.iconbitmap(iicon)
        wbw.title('微博热搜榜')
        wbw.geometry('550x280')
        gd=tk.Scrollbar(wbw)
        gd.pack(side='right',fill='y')
        self.lb=tk.Listbox(wbw,width=230,font=('Arial',16),yscrollcommand=gd.set)
        self.lb.bind('<Double-Button-1>',self.openurl)
        resp=requests.get('https://s.weibo.com/top/summary')
        wbr=re.findall(r'"td-02">\s+<a\shref="(.+)"\starget="_blank">(.+)</a>',resp.text)
        for wb in wbr:
            self.lb.insert('end',wb[1])
            self.tmp.append('https://s.weibo.com'+wb[0])
        self.lb.pack(side='left',fill='both')
        gd.config(command=self.lb.yview)
    def Waw(self):
        self.tmp=[]
        waw=tk.Toplevel()
        waw.iconbitmap(iicon)
        waw.title('吾爱破解日热度排行')
        waw.geometry('550x280')
        gd=tk.Scrollbar(waw)
        gd.pack(side='right',fill='y')
        self.lb=tk.Listbox(waw,width=230,font=('Arial',16),yscrollcommand=gd.set)
        self.lb.bind('<Double-Button-1>',self.openurl)
        resp=requests.get('https://www.52pojie.cn/misc.php?mod=ranklist&type=thread&view=heats&orderby=today')
        war=re.findall(r'href="(.+html)"\starget="_blank">(.+)</a>',resp.text)
        for wa in war:
            self.lb.insert('end',wa[1])
            self.tmp.append('https://www.52pojie.cn/'+wa[0])
        self.lb.pack(side='left',fill='both')
        gd.config(command=self.lb.yview)
    def Zhw(self):
        self.tmp=[]
        zhw=tk.Toplevel()
        zhw.iconbitmap(iicon)
        zhw.title('知乎热榜')
        zhw.geometry('550x280')
        gd=tk.Scrollbar(zhw)
        gd.pack(side='right',fill='y')
        self.lb=tk.Listbox(zhw,width=230,font=('Arial',16),yscrollcommand=gd.set)
        self.lb.bind('<Double-Button-1>',self.openurl)
        resp=requests.get('https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total',headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)''AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/83.0.4103.97 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;''q=0.9,image/webp,image/apng,*/*;''q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'})
        zhr=resp.json()['data']
        for zh in zhr:
            self.lb.insert('end',zh['target']['title'])
            self.tmp.append('https://www.zhihu.com/question/'+str(zh['target']['id'])+'?utm_division=hot_list_page')
        self.lb.pack(side='left',fill='both')
        gd.config(command=self.lb.yview)
    def menuf(self,event,x,y):
        if event=='WM_RBUTTONDOWN':
            self.menu.tk_popup(x,y)
        if event=='WM_LBUTTONDOWN':
            self.root.deiconify()
        if event=='WM_MBUTTONDOWN':
            self.root.withdraw()
    def about(self):
        messagebox.showinfo('关于','作者：cnzb\nGithub：https://github.com/cnzbpy/simplepy\nGitee：https://gitee.com/cnzbpy/simplepy')
    def allquit(self):
        self.root.call('winico','taskbar','delete',self.icon)
        self.root.quit()
    def Root(self):
        self.root=tk.Tk()
        self.root.iconbitmap(iicon)
        self.root.title('热榜')
        self.root.call('package','require','Winico')
        self.icon=self.root.call('winico','createfrom',iicon)
        self.root.call('winico','taskbar','add',self.icon,'-callback',(self.root.register(self.menuf),'%m','%x','%y'),'-pos',0,'-text',u'热榜')
        self.menu=tk.Menu(self.root,tearoff=0)
        self.menu.add_command(label=u'显示主页面',command=self.root.deiconify)
        self.menu.add_command(label=u'关于',command=self.about)
        self.menu.add_command(label=u'隐藏主页面',command=self.root.withdraw)
        self.menu.add_command(label=u'退出',command=self.allquit)
        panel=tk.Frame(self.root)
        tk.Button(panel,text='b站',font=('',16),command=self.Bzw).pack(side='left')
        tk.Button(panel,text='微博',font=('',16),command=self.Wbw).pack(side='left')
        tk.Button(panel,text='吾爱破解',font=('',16),command=self.Waw).pack(side='left')
        tk.Button(panel,text='知乎',font=('',16),command=self.Zhw).pack(side='left')
        panel.pack(expand=1)
        self.root.mainloop()
if getattr(sys,'frozen',False):
        odir=sys._MEIPASS
else:
    odir=os.path.dirname(os.path.abspath(__file__))
iicon=os.path.join(odir,'热榜.ico')
rs().Root()