
#---------------------------Bus Ticket Booking---------------------------------------------coding----------------######

from tkinter import *
from tkinter import Tk, StringVar,ttk
import random
from tkinter import messagebox
import time;
import datetime
from tkinter import font



root = Tk()
root.geometry("1350x750+0+0")
root.title("Ticket Booking")
root.configure(background='#E9967A')
#-----------------------------------Top frame-------------------------------------------------
Top= Frame(root, width=1350, height=100, bd=20, relief='raise')
Top.pack(side=TOP)

#-----------------------------=END=------------------------------------
f1 =Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 =Frame(root, width=900, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)


frametopRight =Frame(f2, width=440, height=650, bd=12, relief="raise")
frametopRight.pack(side=TOP)
frameBottomRight=Frame(f2, width=440, height=60, bd=16, relief="raise")
frameBottomRight.pack(side=BOTTOM)

f1a =Frame(f1, width=900, height=650, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a =Frame(f1, width=900, height=650, bd=6, relief="raise")
f2a.pack(side=BOTTOM)


topLeft1 =Frame(f1a, width=300, height=200, bd=16, relief="raise")
topLeft1.pack(side=LEFT)
topLeft2=Frame(f1a, width=300, height=200, bd=16, relief="raise")
topLeft2.pack(side=RIGHT)
topLeft3=Frame(f1a, width=300, height=200, bd=16, relief="raise")
topLeft3.pack(side=RIGHT)

#.........................................................................
bottomLeft1 = Frame(f2a, width=450, height=450, bd=14, relief="raise")
bottomLeft1.pack(side=LEFT)

bottomLeft2 = Frame(f2a, width=450, height=450, bd=14, relief="raise")
bottomLeft2.pack(side=RIGHT)
#..............................................top right.............................

Top.configure(background='#E9967A')
f1.configure(background='#E9967A')
f2.configure(background='#E9967A')
#-----------------------------------top heading---------------------------------------------
lb1Title=Label(Top,font=('italic',40,'bold'),text="BUS Ticketing Portal ",fg="#FF4081", bd=10, width=41, justify='center')
lb1Title.grid(row=0,column=0)
#------------------------------------------end--------------------------------------------------
Date1=StringVar()
time1=StringVar()
Ticketclass= StringVar()
TicketPrice = StringVar()
Child_Ticket = StringVar()
Adult_Ticket= StringVar()
From_Destination= StringVar()
To_Destination= StringVar()
Fee_Price= StringVar()
Route= StringVar()
Receipt_Ref= StringVar()

Ticketclass.set("")
TicketPrice.set("")
Child_Ticket.set("")
Adult_Ticket.set("")
From_Destination.set("")
To_Destination.set("")
Fee_Price.set("")
Route.set("")
Receipt_Ref.set("")



#-------------------------------------------------

lb1Receipt=Label(frametopRight,font=('italic',16,'bold'),text="BOOKING DETAILS ",fg="#9FA8DA", bd=10, width=36,height=4, justify='center')
#--------------underline------------------------
f = font.Font(lb1Receipt, lb1Receipt.cget("font"))
f.configure(underline = True)
lb1Receipt.configure(font=f)
#------------------end-----------------------
lb1Receipt.grid(row=0,column=0)

lb1Class1=Label(frameBottomRight,font=('italic',16,'bold'),text="CLASS", width=7, relief ='sunken' ,justify='center')
lb1Class1.grid(row=0,column=0)

lb1Class2=Label(frameBottomRight,font=('italic',16,'bold'),width=7, relief ='sunken',textvariable=Ticketclass, justify='center')
lb1Class2.grid(row=1,column=0)


lb1Ticket1=Label(frameBottomRight,font=('italic',16,'bold'),text="TICKET ", width=7, relief ='sunken' ,justify='center')
lb1Ticket1.grid(row=0,column=1)
lb1Ticket2=Label(frameBottomRight,font=('italic',16,'bold'),width=7, relief ='sunken', textvariable=TicketPrice ,justify='center')
lb1Ticket2.grid(row=1,column=1)


lb1Adult1=Label(frameBottomRight,font=('italic',16,'bold'),text="ADULT ", width=7,relief ='sunken' , justify='center')
lb1Adult1.grid(row=0,column=2)
lb1Adult2=Label(frameBottomRight,font=('italic',16,'bold'),width=7, relief ='sunken',textvariable=Adult_Ticket ,justify='center')
lb1Adult2.grid(row=1,column=2)


lb1Child1=Label(frameBottomRight,font=('italic',16,'bold'),text="CHILD", width=7, relief ='sunken' ,justify='center')
lb1Child1.grid(row=0,column=3)
lb1Child2=Label(frameBottomRight,font=('italic',16,'bold'),width=7, relief ='sunken',textvariable=Child_Ticket ,justify='center')
lb1Child2.grid(row=1,column=3)
#---------------------------------------------------------------

lb1sp=Label(frameBottomRight,font=('italic',14,'bold'), width=34,height=2, relief ='sunken' ,justify='center')

lb1sp.grid(row=2,column=0, columnspan=4)

#------------------------------------------------------------------


lb1From1=Label(frameBottomRight,font=('italic',16,'bold'),text="FROM",fg="#663333", width=7, relief ='sunken' ,justify='center')
lb1From1.grid(row=3,column=1)
lb1From2=Label(frameBottomRight,font=('italic',16,'bold'), width=7, relief ='sunken',textvariable=From_Destination ,justify='center')
lb1From2.grid(row=3,column=2)


lb1To1=Label(frameBottomRight,font=('italic',16,'bold'),text="TO",fg="#663333", width=7, relief ='sunken' ,justify='center')
lb1To1.grid(row=4,column=1)
lb1To2=Label(frameBottomRight,font=('italic',16,'bold'), width=7, relief ='sunken',textvariable=To_Destination ,justify='center')
lb1To2.grid(row=4,column=2)


lb1Price1=Label(frameBottomRight,font=('italic',16,'bold'),text="PRICE",fg="#663333", width=7, relief ='sunken' ,justify='center')
lb1Price1.grid(row=5,column=1)
lb1Price2=Label(frameBottomRight,font=('italic',16,'bold'), width=7, relief ='sunken',textvariable=Fee_Price ,justify='center')
lb1Price2.grid(row=5,column=2)

#---------------------------------------------------------------

lb1sp=Label(frameBottomRight,font=('italic',14,'bold'), width=34,height=2, relief ='sunken' ,justify='center')

lb1sp.grid(row=6,column=0, columnspan=4)

#------------------------------------------------------------------


lb1RefNo1=Label(frameBottomRight,font=('italic',16,'bold'),text="REF NO", width=7, relief ='sunken' ,justify='center')
lb1RefNo1.grid(row=7,column=0)
lb1RefNo2=Label(frameBottomRight,font=('italic',16,'bold'), width=7, relief ='sunken',textvariable=Receipt_Ref,justify='center')
lb1RefNo2.grid(row=8,column=0)


lb1Time1=Label(frameBottomRight,font=('italic',16,'bold'),text="TIME", width=8, relief ='sunken' ,justify='center')
lb1Time1.grid(row=7,column=1)
lb1Time2=Label(frameBottomRight,font=('italic',16,'bold'), width=8, relief ='sunken',textvariable=time1, justify='center')
lb1Time2.grid(row=8,column=1)

lb1Date1=Label(frameBottomRight,font=('italic',16,'bold'),text="DATE", width=8, relief ='sunken' ,justify='center')
lb1Date1.grid(row=7,column=2)
lb1Date2=Label(frameBottomRight,font=('italic',16,'bold'), width=8, relief ='sunken',textvariable=Date1, justify='center')
lb1Date2.grid(row=8,column=2)


lb1Route1=Label(frameBottomRight,font=('italic',16,'bold'),text="ROUTE", width=7, relief ='sunken' ,justify='center')
lb1Route1.grid(row=7,column=3)
lb1Route2=Label(frameBottomRight,font=('italic',16,'bold'), width=7, relief ='sunken',textvariable=Route ,justify='center')
lb1Route2.grid(row=8,column=3)
  


#function variable ------------------------------------------------------------------------------------------------
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

def iExit():
    qExit= messagebox.askyesno("QUIT SYSTEM","DO YOU WANT TO QUIT ?")
    if qExit ==True:
        root.destroy()
        import pymysql
        import pymysql.cursors
        conn= pymysql.connect(host='localhost',user='root')
               
        cur=conn.cursor()
        cur.execute("use slip")
        
        cur.execute("SELECT * FROM detail ") 
        data=cur.fetchall()
        
        data_to_file=open("database_details.Doc","w")

        for i in data:
            
            data_to_file.write(str(i)) 
            data_to_file.write("\n")

        data_to_file.close()
        conn.commit()
        conn.close()
        
        root.destroy()
         
        return
#++++++++++++++++++++++++++++++++++define global variable+++++++++++++++++++++++++++++++++++

Receipt_Ref=" "
cost=" "

#--------------------------------------print slip define------------------------------------------------------

def Print_Slip():
    qExit= messagebox.askyesno("PRINT SYSTEM","PRINT RECEIPT")
    if qExit ==True:
        #from receipt import *
        a=open("slip.doc","w")
        a.write(" \t\t\t\t      TICKET BOOKING RECEIPT      \n")
        a.write(" \t\t\t\t      ......................      \n\n\n\n")
        a.write("Receipt No\t\t\t\tDate\t\t\t\t\t\tTime\n")
        a.write("----------\t\t\t\t----\t\t\t\t\t\t----\n")
        d=time.strftime("\t\t\t%d/%m/%Y")
        t=time.strftime('\t\t\t%H:%M:%S')
        a.write(Receipt_Ref+"\t\t"+d+"\t\t"+t+"\n\n")
        a.write("\n\n1.> Class:" )
        if (var1.get()==1 and var2.get()==0 and var3.get()==0  ):
            a.write("\t\t\t\t\tNON A.C\n")
        elif (var1.get()==0 and var2.get()==1 and var3.get()==0  ):
            a.write("\t\t\t\t\tA.C\n")
        elif (var1.get()==0 and var2.get()==0 and var3.get()==1  ):
            a.write("\t\t\t\t\tVOLVO\n")

        a.write("\n\n2.> ADULT\CHILD:")

        if( var4.get()==1 and var5.get()==0  and var13.get()==0):
            a.write("\t\t\t\tAdult- YES\n\t\t\t\t\t\tChild- NO")
            
        if( var4.get()==0 and var5.get()==1  and var13.get()==0):
            a.write("\t\t\t\tAdult- NO \n\t\t\t\t\t\tChild- YES")
            
        if( var4.get()==0 and var5.get()==0  and var13.get()==1):
            a.write("\t\t\t\tAdult- YES \n\t\t\t\t\t\tChild- YES")

        a.write("\n\n3.> NO. OF BOOKING:\t\t\t")
        a.write(str(var12.get()))

        a.write("\n\n4.> FROM DESTINATION:\t\t\tPATNA")
        a.write("\n\n5.> TO DESTINATION:\t\t\t")

        if (var9.get()=="Delhi" and var9.get()!="Allahabad" and var9.get()!="Kanpur" and var9.get()!="Agra" and var9.get()!="Mathura"):
            a.write("Delhi")


        if (var9.get()!="Delhi" and var9.get()=="Allahabad" and var9.get()!="Kanpur" and var9.get()!="Agra" and var9.get()!="Mathura"):
            a.write("Allahabad")


        if (var9.get()!="Delhi" and var9.get()!="Allahabad" and var9.get()=="Kanpur" and var9.get()!="Agra" and var9.get()!="Mathura"):
            a.write("Kanpur")


        if (var9.get()!="Delhi" and var9.get()!="Allahabad" and var9.get()!="Kanpur" and var9.get()=="Agra" and var9.get()!="Mathura"):
            a.write("Agra")

            
        if (var9.get()!="Delhi" and var9.get()!="Allahabad" and var9.get()!="Kanpur" and var9.get()!="Agra" and var9.get()=="Mathura"):
            a.write("Mathura")
            
          
        a.write("\n\n6.> ROUTE:\t\t\t\t\tDIRECT")
        a.write("\n\n7.> Totalcost:\t\t\t\t")
        a.write(str(cost))
        a.write("\n\n\n\t\t\t\tTHANKU FOR USING OUR BUS SERVICE\n")
        a.write("\t\t\t\tWISHING YOU A HAPPY AND SAFE JOURNEY\n")
        a.write("\t\t\tWE WISH THAT U COME AGAIN AND CHOOSE OUR SERVICE\n ")
        a.write("\t\t\t\tFOR CONTACT:-\tMOBIME NO:9807393030\n")
        a.write("\t\t\t\t.....................................\n\n")
        a.write("-----------*--------*------*--------*------*-------*------*-----*--------")
        return

   
def Travel_Cost():
        
    global Receipt_Ref
    global cost
        
    if (var9.get() == "Delhi" and var1.get() == 1 and var4.get()==1):
                
        Tcost = float(100.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=str('%.2f'%(Tcost * 0.03))
        
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)

        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        
        Ticketclass.set("Non A.C")
        TicketPrice.set(Adult_Fees)
        
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        
        From_Destination.set("Patna")
        To_Destination.set("Delhi")
        
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        
        Route.set("Direct")
                        
        #import pymysql
        #conn=pymysql.connect(host="localhost",user="root")
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()        
        
        """

        x=random.randint(109, 5876)
        randomRef = str(x)
        
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """


#----------------------------------child button------------------------------------  

    elif (var9.get() == "Delhi" and var1.get() == 1 and var5.get() ==1):
        
        Tcost = float(60.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Delhi")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")
        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()     
        
        
#-----------------------------both button---------------------
    elif (var9.get() == "Delhi" and var1.get() == 1 and var13.get() ==1):
        
        Tcost = float(160.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)

        cost= str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))

        SubTotal.set(Adult_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Delhi")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")
        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close() 
        


        #--------------------------------------------------------------------------------
#--------------------------------allahabad----------------------------------adult------
    if (var9.get() == "Allahabad" and var1.get() == 1 and var4.get()==1):
        
        
        Tcost = float(50.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Allahabad")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")
        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()       
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Allahabad" and var1.get() == 1 and var5.get() ==1):
        
        Tcost = float(20.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost= str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Allahabad")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")
        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()         
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Allahabad" and var1.get() == 1 and var13.get() ==1):
        
        Tcost = float(70.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Allahabad")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")
        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """

        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()        
        
#----------------------end allahabad-------------------------------------------    
#--------------------------------Kanpur----------------------------------adult------
    if (var9.get() == "Kanpur" and var1.get() == 1 and var4.get()==1):
        
        
        Tcost = float(60.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Kanpur")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")
        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()        
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Kanpur" and var1.get() == 1 and var5.get() ==1):
        
        Tcost = float(22.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Kanpur")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")
        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()        
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Kanpur" and var1.get() == 1 and var13.get() ==1):
        
        Tcost = float(82.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Kanpur")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")
        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()    
        
#----------------------------------end kanpur----------------------------------    
#--------------------------------agra----------------------------------adult------
    if (var9.get() == "Agra" and var1.get() == 1 and var4.get()==1):
        
        
        Tcost = float(75.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Agra")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()      
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Agra" and var1.get() == 1 and var5.get() ==1):
        
        Tcost = float(27.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Agra")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()    
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Agra" and var1.get() == 1 and var13.get() ==1):
        
        Tcost = float(102.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Agra")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()      
        
#--------------------------------end agra--------------------------------------    

   
#--------------------------------Mathura----------------------------------adult------
    if (var9.get() == "Mathura" and var1.get() == 1 and var4.get()==1):
        
        
        Tcost = float(82.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Mathura")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()       
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Mathura" and var1.get() == 1 and var5.get() ==1):
        
        Tcost = float(30.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Mathura")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()        
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Mathura" and var1.get() == 1 and var13.get() ==1):
        
        Tcost = float(112.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("Non A.C")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Mathura")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()         
        
#--------------------------------end mathura--------------------------------------    
#**********************************A.C class***********************************************************************************88

#-----------------------------------delhi ----------------class


    elif (var9.get() == "Delhi" and var2.get() == 1 and var4.get()==1):
        
 #--------------------------------standard----------------------- zone--------------------------------------------------------------------       
        Tcost = float(200.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Delhi")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")
        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()       
        
#----------------------------------child button------------------------------------  

    elif (var9.get() == "Delhi" and var2.get() == 1 and var5.get() ==1):
        
        Tcost = float(100.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Delhi")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()        
        
        
#-----------------------------both button---------------------
    elif (var9.get() == "Delhi" and var2.get() == 1 and var13.get() ==1):
        
        Tcost = float(300.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Delhi")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()     
        
#--------------------------------------------------------------------------------
#--------------------------------allahabad----------------------------------adult------
    if (var9.get() == "Allahabad" and var2.get() == 1 and var4.get()==1):
        
        
        Tcost = float(80.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Allahabad")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()    
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Allahabad" and var2.get() == 1 and var5.get() ==1):
        
        Tcost = float(30.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost= str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Allahabad")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Non A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()      
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Allahabad" and var2.get() == 1 and var13.get() ==1):
        
        Tcost = float(110.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Allahabad")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()        
        


#----------------------end allahabad-------------------------------------------    
#--------------------------------Kanpur----------------------------------adult------
    if (var9.get() == "Kanpur" and var2.get() == 1 and var4.get()==1):
        
        
        Tcost = float(100.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Kanpur")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",user="root")
        
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()   
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Kanpur" and var2.get() == 1 and var5.get() ==1):
        
        Tcost = float(45.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Kanpur")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()     
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Kanpur" and var2.get() == 1 and var13.get() ==1):
        
        Tcost = float(145.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Kanpur")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()  
        
#----------------------------------end kanpur----------------------------------    
#--------------------------------agra----------------------------------adult------
    if (var9.get() == "Agra" and var2.get() == 1 and var4.get()==1):
        
        
        Tcost = float(120.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost= str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Agra")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()       
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Agra" and var2.get() == 1 and var5.get() ==1):
        
        Tcost = float(60.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Agra")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()     
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Agra" and var2.get() == 1 and var13.get() ==1):
        
        Tcost = float(180.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Agra")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()        
        
#--------------------------------end agra--------------------------------------    

   
#--------------------------------mathura----------------------------------adult------
    if (var9.get() == "Mathura" and var2.get() == 1 and var4.get()==1):
        
        
        Tcost = float(152.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Mathura")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()      
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Mathura" and var2.get() == 1 and var5.get() ==1):
        
        Tcost = float(90.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Mathura")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()      
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Mathura" and var2.get() == 1 and var13.get() ==1):
        
        Tcost = float(242.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("A.C Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Mathura")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('A.C','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()      
        
#--------------------------------end mathura--------------------------------------    
        

#**********************************First class***********************************************************************************88

#-----------------------------------delhi ----------------class


    elif (var9.get() == "Delhi" and var3.get() == 1 and var4.get()==1):
        
 #--------------------------------standard----------------------- zone--------------------------------------------------------------------       
        Tcost = float(300.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Delhi")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()    
        
#----------------------------------child button------------------------------------  

    elif (var9.get() == "Delhi" and var3.get() == 1 and var5.get() ==1):
        
        Tcost = float(150.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Delhi")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()        
        
        
#-----------------------------both button---------------------
    elif (var9.get() == "Delhi" and var3.get() == 1 and var13.get() ==1):
        
        Tcost = float(400.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Delhi")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()       
        
#--------------------------------------------------------------------------------
#--------------------------------allahabad----------------------------------adult------
    if (var9.get() == "Allahabad" and var3.get() == 1 and var4.get()==1):
        
        
        Tcost = float(120.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Allahabad")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()      
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Allahabad" and var3.get() == 1 and var5.get() ==1):
        
        Tcost = float(50.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Allahabad")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close() 
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Allahabad" and var3.get() == 1 and var13.get() ==1):
        
        Tcost = float(170.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Allahabad")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",user="root")
        
        cur=conn.cursor()
        cur.execute("create database if not exists slip")
        cur.execute("use slip")  #if not exists
                   
        cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
        
        cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")

        conn.commit()
        conn.close()        
        
#----------------------end allahabad-------------------------------------------    
#--------------------------------Kanpur----------------------------------adult------
    if (var9.get() == "Kanpur" and var3.get() == 1 and var4.get()==1):
        
        
        Tcost = float(150.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Kanpur")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()     
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Kanpur" and var3.get() == 1 and var5.get() ==1):
        
        Tcost = float(75.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Kanpur")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()      
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Kanpur" and var3.get() == 1 and var13.get() ==1):
        
        Tcost = float(225.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Kanpur")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """

        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close() 
#----------------------------------end kanpur----------------------------------    
#--------------------------------agra----------------------------------adult------
    if (var9.get() == "Agra" and var3.get() == 1 and var4.get()==1):
        
        
        Tcost = float(180.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Agra")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """

        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()      
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Agra" and var3.get() == 1 and var5.get() ==1):
        
        Tcost = float(100.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Agra")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """

        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()   
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Agra" and var3.get() == 1 and var13.get() ==1):
        
        Tcost = float(280.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Agra")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()         
        
#--------------------------------end agra--------------------------------------    

   
#--------------------------------mathura----------------------------------adult------
    if (var9.get() == "Mathura" and var3.get() == 1 and var4.get()==1):
        
        
        Tcost = float(210.0)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        A_Tax=Adult_Tax
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Mathura")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()         
        
        
#-------------------------------child--------------------------------------
    elif (var9.get() == "Mathura" and var3.get() == 1 and var5.get() ==1):
        
        Tcost = float(110.8)
        Single = float(var12.get())
        Child_Tax = "Rs", str('%.2f'%(Tcost * 0))
        Child_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        Tax.set(Child_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0)))
        SubTotal.set(Child_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Patna")
        To_Destination.set("Mathura")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()     
        
        
#-----------------------------both----------------------------------------
    elif (var9.get() == "Mathura" and var3.get() == 1 and var13.get() ==1):
        
        Tcost = float(320.8)
        Single = float(var12.get())
        Adult_Tax = "Rs", str('%.2f'%(Tcost * 0.03))
        Adult_Fees = "Rs", str('%.2f'%(Tcost * Single))
        Totalcost = "Rs", str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        Tax.set(Adult_Tax)
        cost=str('%.2f'%(  (Tcost * Single)+ (Tcost * 0.03)))
        SubTotal.set(Adult_Fees)
        Ticketclass.set("VOLVO")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("Yes")
        From_Destination.set("Patna")
        To_Destination.set("Mathura")                              
        Fee_Price.set(Totalcost)
        Total.set(Totalcost)
        Route.set("Direct")

        """
        x=random.randint(109, 5876)
        Receipt_Ref=randomRef
        Receipt_Ref.set("TFL"+ Receipt_Ref)
        """
        try:
            import pymysql
            import pymysql.cursors
            conn= pymysql.connect(host='localhost',user='root')
            cur=conn.cursor()
            cur.execute("create database if not exists slip")
            cur.execute("use slip")  #if not exists
            cur.execute("create table if not exists detail(class varchar(8),seat varchar(3),source varchar(5),destination varchar(10),cost varchar(10))")
            cur.execute("insert into detail values('Volvo','"+str(var12.get())+"','Patna','"+str(var9.get())+"','"+str(cost)+"')")
            conn.commit()
            messagebox.showinfo('message','ticket process successfully.....')
        except:
                  print('message','ticket  process successfully.....')
                  conn.rollback() 
        conn.close()        
        
#--------------------------------end mathura--------------------------------------    


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
Tc=IntVar()
Tax=StringVar()



MessageBox=StringVar()

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")



def chkbutton_value():
    #print "ok"
    if (var10.get()==1):
        #print "okk"
        var12.set("0")
        entSingle.configure(state= NORMAL)
    elif var10.get()==0:
        #print "okk2"
        entSingle.configure(state=NORMAL)
        var12.set("0")
       
                             
                              
def Reset():
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    SubTotal.set("0")
    Total.set("0")
    Ticketclass.set("")
    TicketPrice.set("")
    Child_Ticket.set("")
    Adult_Ticket.set("")
    From_Destination.set("")
    To_Destination.set("")
    Fee_Price.set("")
    Tax.set("0")

    

#variable ------------------------------------------------------------------------------------------------


SubTotal=StringVar()
Total=StringVar()
text_Input=StringVar()
operator=""

#-------------------------------------------------------Date and Time-------------------------------------------------------------

Date1.set(time.strftime("%d/%m/%Y"))
time1.set(time.strftime('%H:%M:%S'))

 # wadges topleft1---------------------------------------------------------------------------------------------------------------------
lblClass=Label(topLeft1, font=('italic',22,'bold'),text="CLASS",fg="#9FA8DA",bd=10)
#--------------------underline--------------------
f = font.Font(lblClass, lblClass.cget("font"))
f.configure(underline = True)
lblClass.configure(font=f)
#-------------------------end---------------------------
lblClass.grid(row=0,column=0, sticky=W)

chkStandard = Checkbutton(topLeft1, font=('italic',20,'bold'),text="Non A.C", variable=var1, onvalue=1, offvalue=0)
chkStandard.grid(row=1,column=0, sticky=W)

chkEconomy = Checkbutton(topLeft1, font=('italic',20,'bold'),text="A.C Class", variable=var2, onvalue=1, offvalue=0)
chkEconomy.grid(row=2,column=0, sticky=W)

chkFirstClass = Checkbutton(topLeft1, font=('italic',20,'bold'),text="VOLVO", variable=var3, onvalue=1, offvalue=0)
chkFirstClass.grid(row=3,column=0, sticky=W)


#wadges 2------------------------------------------------------------------------------------------

lblSelect = Label(topLeft3, font=('italic',20,'bold'),text="Select Destination", fg="#9FA8DA",bd=8)
#--------------underline------------------------
f = font.Font(lblSelect, lblSelect.cget("font"))
f.configure(underline = True)
lblSelect.configure(font=f)
#------------------------end-----------------------
lblSelect.grid(row=0,column=0, sticky=W, columnspan=2)
lblDestination = Label(topLeft3, font=('italic',20,'bold'),text="Destination", bd=4)
lblDestination.grid(row=1,column=0, sticky=W)

cboDestination=ttk.Combobox(topLeft3, textvariable = var9, state='readonly', font=('italic',20,'bold'),width=8)
cboDestination['value']=('Select', 'Delhi','Allahabad', 'Kanpur', 'Agra', 'Mathura')
cboDestination.current(0)
cboDestination.grid(row=1,column=1)

chkAdult = Checkbutton(topLeft3, font=('italic',20,'bold'),text="Adult", variable=var4, onvalue=1, offvalue=0)
chkAdult.grid(row=2,column=0, sticky=W)
chkChild = Checkbutton(topLeft3, font=('italic',20,'bold'),text="Child", variable=var5, onvalue=1, offvalue=0)
chkChild.grid(row=3,column=0, sticky=W)
chkBoth = Checkbutton(topLeft3, font=('italic',20,'bold'), text="Both", variable=var13, onvalue=1, offvalue=0)
chkBoth.grid(row=3,column=1, sticky=W)

#ticket----------------------------------------------------------------------------------------------------------------------

lblClass = Label(topLeft2, font=('italic',22,'bold'),text='TICKET',fg="#9FA8DA", bd=8,justify='center')
#--------------underline------------------------
f = font.Font(lblClass, lblClass.cget("font"))
f.configure(underline = True)
lblClass.configure(font=f)
#------------------------end-----------------------

lblClass.grid(row=0,column=0)

chkSingle = Checkbutton(topLeft2, font=('italic',20,'bold'),text='ENTER', height=2, variable=var10, onvalue=1, offvalue=0
                        ,command=chkbutton_value)
                        
chkSingle.grid(row=1,column=0, sticky=W)
entSingle = Entry(topLeft2, font=('italic',20,'bold'),  textvariable = var12, bd=2,
                  width=8,state= DISABLED)
                  
entSingle.grid(row=1,column=1, sticky=W)


lblComment= Label(topLeft2, font=('italic',22,'bold'),text='Comment', bd=8)
lblComment.grid(row=3,column=0, sticky=W)
entComment = Entry(topLeft2, font=('italic',20,'bold'),  textvariable = var7, bd=2, width=8)
entComment.grid(row=3,column=1, sticky=W)

#--------------------------------------------------------calculator---------------------------------------------------------------------

text_Input = StringVar()
txtDisplay = Entry(bottomLeft2, font=('italic', 10, 'bold'), textvariable= text_Input, bd=8,
                    justify='right',width=36)
txtDisplay.grid(columnspan=4)
#--------------------------------addition-------------------------------------------------
btn7= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='7',width=4,
                    command=lambda:btnClick(7)).grid(row=2, column=0)


btn8= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='8',width=4,
                    command=lambda:btnClick(8)).grid(row=2, column=1)

btn9= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='9',width=4,
                    command=lambda:btnClick(7)).grid(row=2, column=2)

Addition= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='+',width=4,
                    bg="powder blue",command=lambda:btnClick("+")).grid(row=2, column=3)

#--------------------------------------------------------subtraction---------------------------------------------------

btn4= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='4',width=4,
                    command=lambda:btnClick(4)).grid(row=3, column=0)


btn5= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='5',width=4,
                    command=lambda:btnClick(5)).grid(row=3, column=1)

btn6= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='6',width=4,
                    command=lambda:btnClick(6)).grid(row=3, column=2)

Subtraction= Button(bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='-',width=4,
                   bg="powder blue", command=lambda:btnClick("-")).grid(row=3, column=3)
#----------------------------------------------------------------multiply------------------------------------------------------

btn1= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='1',width=4,
                    command=lambda:btnClick(1)).grid(row=4, column=0)


btn2= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='2',width=4,
                    command=lambda:btnClick(2)).grid(row=4, column=1)

btn3= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='3',width=4,
                    command=lambda:btnClick(3)).grid(row=4, column=2)

Multiply= Button(bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='*',width=4,
                    bg="powder blue",command=lambda:btnClick("*")).grid(row=4, column=3)

#--------------------------------------------------------------------bott-----------------------------------------------------
btn0= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='0',width=4,
                    command=lambda:btnClick(0)).grid(row=5, column=0)


btnClear= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='C',width=4, 
                   bg="powder blue",command=btnClearDisplay).grid(row=5, column=1)

btnEquals= Button (bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='=',width=4,
                   bg="powder blue", command=btnEqualsInput).grid(row=5, column=2)

Division= Button(bottomLeft2, padx=8,pady=8,bd=8, fg='black', font=('italic', 10, 'bold'), text='/',width=4,
                   bg="powder blue", command=lambda:btnClick("/")).grid(row=5, column=3)

#---------------------------------------------------------------------Tax, SubTotal and Total--------------------------------------

lblStateTax = Label(bottomLeft1, font=('italic',  16, 'bold'), text ='STATE TAX', bd=16, anchor='w')
lblStateTax.grid(row=3,column=2)

txtStateTax = Entry(bottomLeft1, font=('italic', 16, 'bold'), textvariable=Tax, bd=10,width=28,bg="#ffffff" ,justify='right')
txtStateTax.grid(row=3, column=3)                    


lblSubTotal = Label(bottomLeft1, font=('italic',  16, 'bold'), text ='SUB TOTAL', bd=16, anchor='w')
lblSubTotal .grid(row=4,column=2)
txtSubTotal = Entry(bottomLeft1, font=('italic', 16, 'bold'), textvariable=SubTotal, bd=10,width=28,
                    bg="#ffffff" ,justify='right')
txtSubTotal .grid(row=4, column=3)                    


lblTotalCost = Label(bottomLeft1, font=('italic',  16, 'bold'), text ='TOTAL COST', bd=16, anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost = Entry(bottomLeft1, font=('italic', 16, 'bold'), textvariable=Total , bd=10,width=28,
                    bg="#ffffff" ,justify='right')
txtTotalCost.grid(row=5, column=3)

#------------------------------------------spacing---------
lb1sp=Label(frameBottomRight,font=('italic',14,'bold'), width=34,height=2,
            relief ='sunken' ,justify='center')
lb1sp.grid(row=6,column=0, columnspan=4)


#-----------------------------------------------
#----------------------------------------------------------SPACEE----------------------------------------------------------------------------

lblSpace = Label(bottomLeft1, font=('italic',  24, 'bold'), text ="      \n        ", bd=16, anchor='w')
lblSpace .grid(row=6,column=2)

#-------------------------------------------------------------------------------------------------------------------------------
lblSpace = Label(bottomLeft1, font=('italic',  24, 'bold'), text ="     \n        ", bd=16, anchor='w')
lblSpace .grid(row=6,columnspan=4)

#-----------------------------------space------------------------------------------------------------------------------------------------------

lb1sp=Label(frameBottomRight,font=('italic',14,'bold'), width=34,height=1, relief ='sunken' ,justify='center')
lb1sp.grid(row=9,column=0, columnspan=4)


#------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------button-----------------------------------------------------------
btnTotal= Button (frameBottomRight, text='TOTAL', padx=2,pady=2,bd=2,fg="#FF6F00", font=('italic', 12, 'bold'),width=8,
                  height=1,command=Travel_Cost).grid(row=10, column=0)
               

btnPrint= Button (frameBottomRight, text='PRINT',padx=2,pady=2,bd=2, fg='#00B8D4', font=('italic', 12, 'bold'), width=8,
                  height=1, command= Print_Slip).grid(row=10, column=1)

btnReset= Button (frameBottomRight, text='RESET',padx=2,pady=2,bd=2, fg='#9966FF', font=('italic', 12, 'bold'), width=8,
                  height=1, command= Reset).grid(row=10, column=2)


btnExit= Button (frameBottomRight,text='EXIT', padx=2,pady=2,bd=2, fg='#FF0000', font=('italic', 12, 'bold'), width=8,
                 height=1,command=iExit).grid(row=10, column=3)


#------------------------------------------------------spaceee -----------

lb1sp=Label(frameBottomRight,font=('italic',14,'bold'), width=34,height=0, relief ='sunken' ,justify='center')
lb1sp.grid(row=12,column=0, columnspan=4)

root.mainloop()




