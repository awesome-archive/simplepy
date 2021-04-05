import os,re,sys,js2py,requests
import tkinter as tk
from threading import Thread
from tkinter import messagebox
class Tr:
    def Bd(self):
        self.bt2.config(text='正在翻译...')
        strings=(self.text1.get(1.0,'end')).split('\n')
        for string in strings:
            if string=='':
                continue
            else:
                headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','Cookie':'BAIDUID=4650B0B34048BBAA1E0B909B42F5A564:FG=1;BIDUPSID=4650B0B34048BBAA1E0B909B42F5A564;PSTM=1537177909;BDUSS=w0VmEzUFFWTTh0bld5VWVhNVo5MEEyV2ZKdTk3U2stMGZmWVQ1TTRuSnVkOHBiQVFBQUFBJCQAAAAAAAAAAAEAAAD0GzcNaG9uZ3F1YW4xOTkxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG7qoltu6qJbTk;pgv_pvi=6774493184;uc_login_unique=19e6fd48035206a8abe89f98c3fc542a;uc_recom_mark=cmVjb21tYXJrXzYyNDU4NjM%3D;MCITY=-218%3A;cflag=15%3A3;SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02893452711;locale=zh;Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1539333192;from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D;REALTIME_TRANS_SWITCH=1;FANYI_WORD_SWITCH=1;HISTORY_SWITCH=1;SOUND_SPD_SWITCH=1;SOUND_PREFER_SWITCH=1;to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D;Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1539333307'}
                html=requests.get('https://fanyi.baidu.com',headers=headers)
                gtk=re.findall("window.gtk = '(.*?)';",html.text)[0]
                js=js2py.EvalJs()
                js.execute('function a(r,o){for(var t=0;t<o.length-2;t+=3){var a=o.charAt(t+2);a=a>="a"?a.charCodeAt(0)-87:Number(a),a="+"===o.charAt(t+1)?r>>>a:r<<a,r="+"===o.charAt(t)?r+a&4294967295:r^a}return r}var C=null;var hash=function(r,_gtk){var o=r.length;o>30&&(r=""+r.substr(0,10)+r.substr(Math.floor(o/2)-5,10)+r.substr(-10,10));var t=void 0,t=null!==C?C:(C=_gtk||"")||"";for(var e=t.split("."),h=Number(e[0])||0,i=Number(e[1])||0,d=[],f=0,g=0;g<r.length;g++){var m=r.charCodeAt(g);128>m?d[f++]=m:(2048>m?d[f++]=m>>6|192:(55296===(64512&m)&&g+1<r.length&&56320===(64512&r.charCodeAt(g+1))?(m=65536+((1023&m)<<10)+(1023&r.charCodeAt(++g)),d[f++]=m>>18|240,d[f++]=m>>12&63|128):d[f++]=m>>12|224,d[f++]=m>>6&63|128),d[f++]=63&m|128)}for(var S=h,u="+-a^+6",l="+-3^+b+-f",s=0;s<d.length;s++)S+=d[s],S=a(S,u);return S=a(S,l),S^=i,0>S&&(S=(2147483647&S)+2147483648),S%=1e6,S.toString()+"."+(S^h)}')
                sign=js.hash(string,gtk)
                token=re.findall("token: '(.+)',",html.text)[0]
                landata={'query':string}
                lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata)
                lan=lanhtml.json()['lan']
                if lan=='zh':
                    to='en'
                else:
                    to='zh'
                data={'from':lan,'to':to,'query':string,'sign':'%s'%sign,'token':'%s'%token}
                resp=requests.post('https://fanyi.baidu.com/v2transapi',data=data,headers=headers)
                result=resp.json()['trans_result']['data'][0]['dst']+'\n'
                self.text2.insert('end',result)
        self.text2.delete(self.text2.index('end-1c'),'end')
        self.bt2.config(text='翻译完成')
    def Gg(self):
        self.bt3.config(text='正在翻译...')
        strings=(self.text1.get(1.0,'end')).split('\n')
        for string in strings:
            if string=='':
                continue
            else:
                js=js2py.EvalJs()
                js.execute('function TL(a){var k="";var b=406644;var b1=3293161072;var jd=".";var $b="+-a^+6";var Zb="+-3^+b+-f";for(var e=[],f=0,g=0;g<a.length;g++){var m=a.charCodeAt(g);128>m?e[f++]=m:(2048>m?e[f++]=m>>6|192:(55296==(m&64512)&&g+1<a.length&&56320==(a.charCodeAt(g+1)&64512)?(m=65536+((m&1023)<<10)+(a.charCodeAt(++g)&1023),e[f++]=m>>18|240,e[f++]=m>>12&63|128):e[f++]=m>>12|224,e[f++]=m>>6&63|128),e[f++]=m&63|128)}a=b;for(f=0;f<e.length;f++)a+=e[f],a=RL(a,$b);a=RL(a,Zb);a^=b1||0;0>a&&(a=(a&2147483647)+2147483648);a%=1E6;return a.toString()+jd+(a^b)};function RL(a,b){var t="a";var Yb="+";for(var c=0;c<b.length-2;c+=3){var d=b.charAt(c+2),d=d>=t?d.charCodeAt(0)-87:Number(d),d=b.charAt(c+1)==Yb?a>>>d:a<<d;a=b.charAt(c)==Yb?a+d&4294967295:a^d}return a}')
                tk=js.TL(string)
                landata={'query':string}
                lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata)
                lan=lanhtml.json()['lan']
                if lan=='zh':
                    to='en'
                else:
                    to='zh-CN'
                html=requests.get('https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=%s&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&pc=1&otf=1&ssel=0&tsel=0&kc=1&tk=%s&q=%s'%(to,tk,string))
                result=html.json()[0][0][0]+'\n'
                self.text3.insert('end',result)
        self.text3.delete(self.text3.index('end-1c'),'end')
        self.bt3.config(text='翻译完成')
    def Yd(self):
        self.bt4.config(text='正在翻译...')
        strings=(self.text1.get(1.0,'end')).split('\n')
        for string in strings:
            if string=='':
                continue
            else:
                url="http://fanyi.youdao.com/translate"
                data={'doctype':'json','i':string}
                resp=requests.post(url,params=data)
                result=resp.json()['translateResult'][0][0]['tgt']+'\n'
                self.text4.insert('end',result)
        self.text4.delete(self.text4.index('end-1c'),'end')
        self.bt4.config(text='翻译完成')
    def Bdfy(self):
        Thread(target=self.Bd,daemon=True).start()
    def Ggfy(self):
        Thread(target=self.Gg,daemon=True).start()
    def Ydfy(self):
        Thread(target=self.Yd,daemon=True).start()
    def Fy(self):
        self.bt1.config(text='正在翻译...')
        self.Bdfy()
        self.Ggfy()
        self.Ydfy()
        self.done()
    def done(self):
        loop=self.root.after(100,self.done)
        if self.bt2['text']=='翻译完成' and self.bt3['text']=='翻译完成' and self.bt3['text']=='翻译完成':
            self.bt1.config(text='翻译完成')
            self.root.after_cancel(loop)
    def Clear(self):
        self.text1.delete(1.0,'end')
        self.text2.delete(1.0,'end')
        self.text3.delete(1.0,'end')
        self.text4.delete(1.0,'end')
        self.bt1.config(text='聚合翻译')
        self.bt2.config(text='百度翻译')
        self.bt3.config(text='谷歌翻译')
        self.bt4.config(text='有道翻译')
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
        self.root.title('聚合翻译')
        self.root.call('package','require','Winico')
        self.icon=self.root.call('winico','createfrom',iicon)
        self.root.call('winico','taskbar','add',self.icon,'-callback',(self.root.register(self.menuf),'%m','%x','%y'),'-pos',0,'-text',u'聚合翻译')
        self.menu=tk.Menu(self.root,tearoff=0)
        self.menu.add_command(label=u'显示主页面',command=self.root.deiconify)
        self.menu.add_command(label=u'关于',command=self.about)
        self.menu.add_command(label=u'隐藏主页面',command=self.root.withdraw)
        self.menu.add_command(label=u'退出',command=self.allquit)
        panel1=tk.Frame(self.root)
        xgd1=tk.Scrollbar(panel1,orient='horizontal')
        ygd1=tk.Scrollbar(panel1)
        xgd1.pack(side='bottom',fill='x')
        ygd1.pack(side='right',fill='y')
        self.text1=tk.Text(panel1,wrap='none',xscrollcommand=xgd1.set,yscrollcommand=ygd1.set)
        self.text1.pack(fill='both')
        panel1.pack(fill='both',expand=1)
        xgd1.config(command=self.text1.xview)
        ygd1.config(command=self.text1.yview)
        panel2=tk.Frame(self.root)
        self.bt1=tk.Button(panel2,text='聚合翻译',font=('',16),command=self.Fy)
        self.bt1.pack(side='left')
        self.bt2=tk.Button(panel2,text='百度翻译',font=('',16),command=self.Bdfy)
        self.bt2.pack(side='left')
        self.bt3=tk.Button(panel2,text='谷歌翻译',font=('',16),command=self.Ggfy)
        self.bt3.pack(side='left')
        self.bt4=tk.Button(panel2,text='有道翻译',font=('',16),command=self.Ydfy)
        self.bt4.pack(side='left')
        tk.Button(panel2,text='清屏',font=('',16),command=self.Clear).pack(side='left')
        panel2.pack(expand=1)
        panel3=tk.Frame(self.root)
        panel4=tk.Frame(panel3)
        xgd2=tk.Scrollbar(panel4,orient='horizontal')
        ygd2=tk.Scrollbar(panel4)
        xgd2.pack(side='bottom',fill='x')
        ygd2.pack(side='right',fill='y')
        tk.Label(panel4,text='百度翻译',font=('',15)).pack()
        self.text2=tk.Text(panel4,width=66,wrap='none',xscrollcommand=xgd2.set,yscrollcommand=ygd2.set)
        self.text2.pack()
        panel4.pack(side='left')
        xgd2.config(command=self.text2.xview)
        ygd2.config(command=self.text2.yview)
        panel5=tk.Frame(panel3)
        xgd3=tk.Scrollbar(panel5,orient='horizontal')
        ygd3=tk.Scrollbar(panel5)
        xgd3.pack(side='bottom',fill='x')
        ygd3.pack(side='right',fill='y')
        tk.Label(panel5,text='谷歌翻译',font=('',15)).pack()
        self.text3=tk.Text(panel5,width=66,wrap='none',xscrollcommand=xgd3.set,yscrollcommand=ygd3.set)
        self.text3.pack()
        panel5.pack(side='left')
        xgd3.config(command=self.text3.xview)
        ygd3.config(command=self.text3.yview)
        panel6=tk.Frame(panel3)
        xgd4=tk.Scrollbar(panel6,orient='horizontal')
        ygd4=tk.Scrollbar(panel6)
        xgd4.pack(side='bottom',fill='x')
        ygd4.pack(side='right',fill='y')
        tk.Label(panel6,text='有道翻译',font=('',15)).pack()
        self.text4=tk.Text(panel6,width=66,wrap='none',xscrollcommand=xgd4.set,yscrollcommand=ygd4.set)
        self.text4.pack()
        panel6.pack(side='left')
        xgd4.config(command=self.text4.xview)
        ygd4.config(command=self.text4.yview)
        panel3.pack(expand=1)
        self.root.mainloop()
if getattr(sys,'frozen',False):
        odir=sys._MEIPASS
else:
    odir=os.path.dirname(os.path.abspath(__file__))
iicon=os.path.join(odir,'聚合翻译.ico')
Tr().Root()