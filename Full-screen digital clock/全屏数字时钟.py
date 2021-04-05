import os,sys,time,winsound
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
from borax.calendars.lunardate import LunarDate
class Go:
    def settime(self):
        a,b,c,d=time.strftime('%Y'),time.strftime('%m'),time.strftime('%d'),int(time.strftime('%w'))
        e={1:'星期一',2:'星期二',3:'星期三',4:'星期四',5:'星期五',6:'星期六',0:'星期日'}
        f=e[d]
        nl=LunarDate.from_solar_date(int(a),int(b),int(c))
        g,h,i,j=nl.gz_year,nl.animal,nl.cn_month,nl.cn_day
        today1=a+'年'+b+'月'+c+'日'+f
        todaynl='%s(%s)年%s%s%s'%(g,h,i,j,f)
        time1=time.strftime('%H:%M:%S')
        self.var1.set(todaynl)
        self.var2.set(today1)
        self.var3.set(time1)
        self.root.after(1000,self.settime)
    def swt(self):
        StopWatch().stopwatch()
    def ert(self):
        Endtime().edg()
    def attr(self,v):
        self.root.attributes('-alpha',v)
    def Attr(self):
        atw=tk.Toplevel()
        atw.iconbitmap(iicon)
        atw.title('透明度设置')
        sc=tk.Scale(atw,from_=0,to=1,resolution=0.01,orient='horizontal',command=self.attr,length=230,label='当前透明度（0完全透明，1完全不透明）：')
        sc.set(1)
        sc.pack(expand=1)
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
    def go(self):
        self.root=tk.Tk()
        self.root.attributes('-alpha',1)
        self.root.attributes('-fullscreen',True)
        self.root.iconbitmap(iicon)
        self.root.title('全屏数字时钟')
        self.root.call('package','require','Winico')
        self.icon=self.root.call('winico','createfrom',iicon)
        self.root.call('winico','taskbar','add',self.icon,'-callback',(self.root.register(self.menuf),'%m','%x','%y'),'-pos',0,'-text',u'全屏数字时钟')
        self.menu=tk.Menu(self.root,tearoff=0)
        self.menu.add_command(label=u'显示主页面',command=self.root.deiconify)
        self.menu.add_command(label=u'多闹钟',command=self.ert)
        self.menu.add_command(label=u'关于',command=self.about)
        self.menu.add_command(label=u'隐藏主页面',command=self.root.withdraw)
        self.menu.add_command(label=u'退出',command=self.allquit)
        width=self.root.winfo_width()
        height=self.root.winfo_height()
        if os.path.exists('wallpaper.jpg'):
            photo=Image.open('wallpaper.jpg').resize((width,height))
        elif os.path.exists('wallpaper.png'):
            photo=Image.open('wallpaper.png').resize((width,height))
        img=ImageTk.PhotoImage(photo)
        img1=ImageTk.PhotoImage(photo.crop((160/425*width,0,265/425*width,33/181*height)))
        img2=ImageTk.PhotoImage(photo.crop((160/425*width,33/181*height,264/425*width,72/181*height)))
        img3=ImageTk.PhotoImage(photo.crop((176/425*width,72/181*height,249/425*width,145/181*height)))
        img4=ImageTk.PhotoImage(photo.crop((0,146/181*height,74/425*width,height)))
        img5=ImageTk.PhotoImage(photo.crop((74/425*width,146/181*height,149/425*width,height)))
        img6=ImageTk.PhotoImage(photo.crop((149/425*width,146/181*height,204/425*width,height)))
        img7=ImageTk.PhotoImage(photo.crop((204/425*width,146/181*height,366/425*width,height)))
        img8=ImageTk.PhotoImage(photo.crop((366/425*width,146/181*height,width,height)))
        tk.Label(self.root,image=img).place(x=0,y=0,relwidth=1,relheight=1)
        self.var1=tk.StringVar(self.root)
        self.var2=tk.StringVar(self.root)
        self.var3=tk.StringVar(self.root)
        tk.Label(self.root,image=img1,borderwidth=0,highlightthickness=0,padx=0,pady=0,compound='center',textvariable=self.var1,font=('',21)).pack(expand=1)
        tk.Label(self.root,image=img2,borderwidth=0,highlightthickness=0,padx=0,pady=0,compound='center',textvariable=self.var2,font=('',25)).pack(expand=1)
        tk.Label(self.root,image=img3,borderwidth=0,highlightthickness=0,padx=0,pady=0,compound='center',textvariable=self.var3,font=('Arial',45)).pack(expand=1)
        self.settime()
        panel1=tk.Frame(self.root)
        tk.Button(panel1,image=img4,borderwidth=0,highlightthickness=0,padx=0,pady=0,compound='center',text='透明度',font=('',15),command=self.Attr).pack(side='left')
        tk.Button(panel1,image=img5,borderwidth=0,highlightthickness=0,padx=0,pady=0,compound='center',text='多秒表',font=('',15),command=self.swt).pack(side='left')
        tk.Button(panel1,image=img6,borderwidth=0,highlightthickness=0,padx=0,pady=0,compound='center',text='计次',font=('',15),command=StopWatch().stopwatch).pack(side='left')
        tk.Button(panel1,image=img7,borderwidth=0,highlightthickness=0,padx=0,pady=0,compound='center',text='多倒计时/多闹钟',font=('',15),command=self.ert).pack(side='left')
        tk.Button(panel1,image=img8,borderwidth=0,highlightthickness=0,padx=0,pady=0,compound='center',text='退出',font=('',15),command=self.allquit).pack(side='left')
        panel1.pack(expand=1)
        self.root.mainloop()
class StopWatch:
    def __init__(self,se=0):
        self.se=se
        self.run=True
    def update(self):
        self.se=time.time()-self.start
        self.setTime(self.se)
        self.timer=self.win.after(50,self.update)
    def setTime(self,tm):
        minutes=int(tm/60)
        seconds=int(tm-minutes*60.0)
        hsec=int((tm-minutes*60.0-seconds)*100)
        self.var.set('%.2d:%.2d:%.2d'%(minutes,seconds,hsec))
    def Start(self):
        if self.run:
            self.start=time.time()-self.se
            self.update()
            self.run=False
    def Stop(self):
        if not self.run:
            self.win.after_cancel(self.timer)
            self.se=time.time()-self.start
            self.setTime(self.se)
            self.run=True
    def Reset(self):
        if self.run:
            self.se=0
            self.setTime(self.se)
    def stopwatch(self):
        self.win=tk.Toplevel()
        self.win.geometry('250x100')
        self.win.iconbitmap(iicon)
        self.win.title('多秒表/计次')
        self.var=tk.StringVar()
        tk.Label(self.win,textvariable=self.var,font=('',35)).pack(expand=1)
        self.setTime(self.se)
        panel2=tk.Frame(self.win)
        panel2.pack(expand=1)
        tk.Button(panel2,text='开始计时',font=('',13),command=self.Start).pack(side='left')
        tk.Button(panel2,text='停止计时',font=('',13),command=self.Stop).pack(side='left')
        tk.Button(panel2,text='复位',font=('',13),command=self.Reset).pack(side='left')
class Endtime:
    def __init__(self):
        self.tag=True
    def upgrade(self):
        if not self.tag:
            self.var4.set('倒计时正在运行')
            if self.sec!=0:
                self.sec-=1
            elif self.min!=0 and self.sec==0:
                self.min-=1
                self.sec=59
            elif self.hour!=0 and self.min==0 and self.sec==0:
                self.hour-=1
                self.min=59
                self.sec=59
            else:
                self.var4.set('计时结束')
                self.tag=True
                self.b1.config(text='开始计时',command=self.dl)
            self.var5.set('%.2d'%self.hour)
            self.var6.set('%.2d'%self.min)
            self.var7.set('%.2d'%self.sec)
            self.up=self.ewi.after(1000,self.upgrade)
    def et(self):
        if self.tag:
            self.b1.config(text='停止计时',command=self.stop)
            self.tag=False
            self.upgrade()
    def stop(self):
        if not self.tag:
            self.ewi.after_cancel(self.up)
            self.var4.set('')
            self.b1.config(text='开始计时',command=self.dl)
            self.tag=True
    def reset(self):
        if self.tag:
            self.var4.set('')
            self.var5.set('%.2d'%0)
            self.var6.set('%.2d'%0)
            self.var7.set('%.2d'%0)
    def dl(self):
        try:
            self.hour,self.min,self.sec=int(self.e1.get()),int(self.e2.get()),int(self.e3.get())
        except:
            self.var4.set('格式错误')
        else:
            if self.hour>=0 and 0<=self.min<=59 and 0<=self.sec<=59:
                self.et()
            else:
                self.var4.set('超出范围,请重新输入！')
                self.var5.set('%.2d'%0)
                self.var6.set('%.2d'%0)
                self.var7.set('%.2d'%0)
    def rinw(self):
        self.var4.set('正在响铃，请及时关闭闹钟！')
        self.var5.set('%.2d'%self.hour)
        self.var6.set('%.2d'%self.min)
        self.var7.set('%.2d'%self.sec)
        self.b2.config(text='关闭闹钟',command=self.rinws)
        winsound.Beep(4850,500)
        if self.n<120:
            self.n+=1
            self.rin2=self.ewi.after(50,self.rinw)
        else:
            self.n=1
            self.rin2=self.ewi.after(300000,self.rinw)
    def rinws(self):
        self.ewi.after_cancel(self.rin2)
        self.var4.set('')
        self.tag=True
        self.b2.config(text='设定闹钟',command=self.rinb)
    def rup(self):
        if self.hour==int(time.strftime('%H')) and self.min==int(time.strftime('%M')) and self.sec==int(time.strftime('%S')):
            self.n=1
            self.rinw()
        else:
            self.var5.set('%.2d'%self.hour)
            self.var6.set('%.2d'%self.min)
            self.var7.set('%.2d'%self.sec)
            self.b2.config(text='取消设定',command=self.rins)
            self.rin1=self.ewi.after(50,self.rup)
    def ring(self):
        if self.tag:
            self.var4.set('闹钟已设定')
            self.rup()
            self.tag=False
    def rins(self):
        self.ewi.after_cancel(self.rin1)
        self.var4.set('')
        self.tag=True
        self.b2.config(text='设定闹钟',command=self.rinb)
    def rinb(self):
        try:
            self.hour,self.min,self.sec=int(self.e1.get()),int(self.e2.get()),int(self.e3.get())
        except:
            self.var4.set('格式错误')
        else:
            if 0<=self.hour<=24 and 0<=self.min<=59 and 0<=self.sec<=59:
                self.ring()
            else:
                self.var4.set('超出范围,请重新输入！')
                self.var5.set('%.2d'%0)
                self.var6.set('%.2d'%0)
                self.var7.set('%.2d'%0)
    def edg(self):
        self.ewi=tk.Toplevel()
        self.ewi.geometry('258x90')
        self.ewi.iconbitmap(iicon)
        self.ewi.title('多倒计时/多闹钟')
        self.var4=tk.StringVar()
        self.var5=tk.StringVar()
        self.var6=tk.StringVar()
        self.var7=tk.StringVar()
        panel3=tk.Frame(self.ewi)
        panel4=tk.Frame(self.ewi)
        self.e1=tk.Entry(panel3,justify='center',textvariable=self.var5,width=10)
        self.e1.pack(side='left')
        tk.Label(panel3,text=':').pack(side='left')
        self.e2=tk.Entry(panel3,justify='center',textvariable=self.var6,width=10)
        self.e2.pack(side='left')
        tk.Label(panel3,text=':').pack(side='left')
        self.e3=tk.Entry(panel3,justify='center',textvariable=self.var7,width=10)
        self.e3.pack(side='left')
        panel3.pack(expand=1)
        self.var5.set('%.2d'%0)
        self.var6.set('%.2d'%0)
        self.var7.set('%.2d'%0)
        tk.Label(self.ewi,textvariable=self.var4,font=('',13)).pack(expand=1)
        self.b1=tk.Button(panel4,text='开始计时',font=('',13),command=self.dl)
        self.b1.pack(side='left')
        self.b2=tk.Button(panel4,text='设定闹钟',font=('',13),command=self.rinb)
        self.b2.pack(side='left')
        tk.Button(panel4,text='复位',font=('',13),command=self.reset).pack(side='left')
        panel4.pack(expand=1)
if getattr(sys,'frozen',False):
        odir=sys._MEIPASS
else:
    odir=os.path.dirname(os.path.abspath(__file__))
iicon=os.path.join(odir,'全屏数字时钟.ico')
Go().go()