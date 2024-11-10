from tkinter import *
from tkinter import Tk, StringVar
import random
from tkinter import messagebox
import time;
import datetime
from tkinter import font



root = Tk()
root.geometry("1350x750+0+0")
root.title("Bus Ticket")
root.configure(background='#FFA07A')



Top= Frame(root, width=1350, height=100, bd=20, relief='raise')
Top.pack(side=TOP)

f2=Frame(root, width=520, height=100, bd=2, relief="raise",pady=10)
f2.pack(side=TOP)


f4=Frame(root, width=600, height=400, bd=10, relief="raise")
f4.pack(side=LEFT)


f5=Frame(root, width=500, height=200, bd=10, relief="raise")
f5.pack(side=RIGHT)

f6=Frame(f4, width=500, height=200, bd=10, relief="raise")
f6.pack(side=BOTTOM)


#-----------------------------------------------------------------------------fun def--------------------
def iExit():
    #qExit= messagebox.showinfo("QUIT SYSTEM","DO YOU WANT TO QUIT ?")
    #if qExit ==True:
        root.destroy()
        return
"""
def submit():
    qSubmit= tkMessageBox.askyesno("SUBMIT","DO YOU WANT TO SUBMIT ?")
    if USER_ID=="rohit" and PASSWORD =="12345":
        from onlineticket import *
    else:
        qSubmit= tkMessageBox.askyesno("ERROR","ENTER ID OR PASSWORD IS WRONG ")
    
        return
"""

#---------------------------------------------frame,title -------------------------------------------

Top.configure(background='#FFA07A')
f2.configure(background='#FFA07A')
f2.configure(background='pink')
lb1Title=Label(Top,font=('italic',40,'bold'),text="Bus Ticketing system ",bd=5,fg="#FF4081", width=41, justify='center')
lb1Title.grid(row=0,column=0)

#------------------------------------------------------button---
"""
#lb1left=Label(f1,font=('italic',16,'bold'),text="Bus Ticketing system ", bd=10, width=32,height=2)
lb1left.grid(row=0,column=1)
"""
#----------------------------------------------space-----------------------------
"""
lb1sp=Label(f3,font=('italic',14,'bold'), width=32,height=2,
            relief ='sunken' ,justify='center')
lb1sp.grid(row=1,column=0, columnspan=4)
"""
#--------------------------------------------------------------------------------------------
lb1Receipt=Label(f2,font=('italic',25,),text="LOGIN FORM ", bd=10,fg='#9966FF', width=32,height=2)
f = font.Font(lb1Receipt, lb1Receipt.cget("font"))
f.configure(underline = True)
lb1Receipt.configure(font=f)

lb1Receipt.grid(row=2,column=0)
#------------------------------------------------------
lb1sp=Label(f5,font=('italic',14,'bold'), width=32,height=1,
            relief ='sunken' ,justify='center')
lb1sp.grid(row=1,column=0, columnspan=4)


lb1sp=Label(f6,font=('italic',14,'bold'), width=32,height=2,
            relief ='sunken' ,justify='center')
lb1sp.grid(row=1,column=0, columnspan=4)

#----------------------------------------------------------

id1=Label(f5, text="USER I.D",width=40,fg='#9966FF',justify='left').grid(row=2)
id1=Label(f5, text="NAME",width=40,fg='#9966FF',justify='left').grid(row=3)
id1=Label(f5, text="MAIL I.D",width=40,fg='#9966FF',justify='left').grid(row=6)
id1=Label(f5, text="MOBILE NO",width=40,fg='#9966FF',justify='left').grid(row=5)
#---------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
psL=Label(f5, text="PASSWORD",width=40,fg='#9966FF',justify='left').grid(row=4)

e1 = Entry(f5)
e2 = Entry(f5)
name = Entry(f5)
mail = Entry(f5)
mobile = Entry(f5)

e1.grid(row=2, column=1)
e2.grid(row=4, column=1)
name.grid(row=3, column=1)
mail.grid(row=6, column=1)
mobile.grid(row=5, column=1)

def signup():
    try:
        import pymysql
        import pymysql.cursors
        conn=pymysql.connect(host='localhost',user='root')
        cur=conn.cursor()
        cur.execute("create database if not exists bus_ticket")
        cur.execute("use bus_ticket")
        cur.execute("create table if not exists login(user_id varchar(20),name varchar(10),passwd varchar(5),Mobile_no varchar(10),Mail_id varchar(20))")
        x=str(e1.get())
        y=str(e2.get())
        nm=str(name.get())
        mal=str(mail.get())
        mob=str(mobile.get())
    
        cur.execute("insert into login values(%s,%s,%s,%s,%s)",(x,nm,y,mob,mal))
    
        """cur.execute("SELECT * FROM login")
        row=cur.fetchall()
        i in row:
        #pass
        print (i)"""

        conn.commit()
        messagebox.showinfo("registration successfully....")
    except:
        conn.rollback()
        messagebox.showinfo("not successfully.........")
    conn.close()
    #print "ok"
    
    
b1=Button(f5, text='QUIT', command=iExit,fg='red').grid(row=15, column=2, sticky=W, pady=4)
b2=Button(f5, text='SUBMITT',fg='red',command=signup).grid(row=15, column=1, sticky=W, pady=4)

#--------------------------------------------------------------------------------------------

id11=Label(f6, text="USER I.D",width=40,fg='#9966FF',justify='left').grid(row=2)
#---------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
psL1=Label(f6, text="PASSWORD",width=40,fg='#9966FF',justify='left').grid(row=4)

e3 = Entry(f6)
e4 = Entry(f6)

e3.grid(row=2, column=1)
e4.grid(row=4, column=1)


def signin():
    import pymysql
    import pymysql.cursors
    conn=pymysql.connect(host='localhost',user='root')

    
    cur=conn.cursor()
    cur.execute("use bus_ticket")
    x1=str(e3.get())
    y1=str(e4.get())
    
    #print "entered usr=",x1
    #print "entered pass=",y1

    
    cur.execute("SELECT * FROM login WHERE user_id='"+x1+"' and passwd='"+y1+"'") 
    data=cur.fetchone()

    #usr=data[0]
    #pas=data[1]
    #print "from SQl usr=",usr
    #print "from SQl pass=",pas
        
    #conn.commit()
    #conn.close()

    count=cur.rowcount
   
    if(count>0):
        import os
        os.system("onlineticket.py")
        
    else:
        global root
        root.destroy()
    
    
b1=Button(f6, text='QUIT', command=iExit,fg='red').grid(row=15, column=2, sticky=W, pady=4)
b2=Button(f6, text='SUBMIT',fg='red',command=signin).grid(row=15, column=1, sticky=W, pady=4)


#--------------------------------------------------------------------------------------
lb1sp=Label(f5,font=('italic',14,'bold'), width=32,height=2,
            relief ='sunken' ,justify='center')
lb1sp.grid(row=16,column=0, columnspan=4)

lb1sp=Label(f6,font=('italic',14,'bold'), width=32,height=2,
            relief ='sunken' ,justify='center')
lb1sp.grid(row=16,column=0, columnspan=4)




#-------------------------------------------------------------------------------------
lb1Class1=Label(f5,font=('italic',16,'bold'),text="SIGN UP", fg='#9966FF',width=7, relief ='sunken' ,justify='center')
lb1Class1.grid(row=0,column=0)

lb1Class2=Label(f6,font=('italic',16,'bold'),text="SIGN IN", fg='#9966FF',width=7, relief ='sunken' ,justify='center')
lb1Class2.grid(row=0,column=0)

#------------------------------------------------------------------------------


root.mainloop()
