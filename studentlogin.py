from tkinter import *
import random
import mysql.connector
backcolour="#DA627D"
style=("timesnewroman",20,"bold")
front="#F9DBBD"
backcolour2="#9A348E"
Buttoncolor="#F9DBBD"
buttontxt="#0D0628"
#=====================Variables==========================
passwordvar=StringVar
registrationvar=IntVar
captchavar=IntVar
#======================Captcha===========================
captcha=random.randint(0,99999)

def studentwin():
    #win.destroy()
    Toplevel=Tk()
    lay=Toplevel
    lay.focus_get()
    Toplevel.title("Student Login")
    Toplevel.geometry("500x500")
    lay.resizable(False,False)
    F3=Label(lay,text="Login",font=style,background=backcolour2,foreground=front,border="2",padx=1)
    F3.place(x=0,y=0,relwidth=1,height=30)
    F4=Frame(lay,background=backcolour)
    F4.place(x=0,y=37,relwidth=1,relheight=0.9)
    F5=Label(F4,text="Registration No:",font=style,background=backcolour,foreground=front,anchor="nw",width=13,border="2")
    F5.grid(row=0,column=0,pady=2)
    F6=Label(F4,text="Password",font=style,background=backcolour,foreground=front,anchor="nw",width=13,border="2")
    F6.grid(row=1,column=0,pady=2)
    F7=Entry(F4,width=15,font=style,textvariable=registrationvar)
    F7.grid(row=0,column=1,pady=2)
    F8=Entry(F4,width=15,font=style,textvariable=passwordvar)
    F8.grid(row=1,column=1,pady=2)
    F9=Label(F4,text="Enter Captcha",font=style,background=backcolour,foreground=front,anchor="nw",width=13,border="2")
    F9.grid(row=2,column=0,pady=2)
    F10=Label(F4,text=captcha,font=style,background=backcolour,foreground=front,anchor="nw",width=13,border="2")
    F10.grid(row=3,column=0)
    Copy=Label(lay,text="COPYRIGHTS ABC INSTITUTE OF TECHNOLOGY",font=("timesnewroman",10,"bold"),border="2")
    F11=Entry(F4,width=15,font=style,textvariable=captchavar)
    F11.grid(row=3,column=1)
    Verify=Button(F4,text="Reset",font=("timesnewroman",10,"bold"),width=27)
    Verify.grid(row=5,column=0,pady=10)
    Submit=Button(F4,text="Login",font=("timesnewroman",10,"bold"),width=27,command=checkpassword(F7,F8))
    Submit.grid(row=5,column=1,pady=10)
    Copy.pack(fill=X,anchor="s",side="bottom")
    lay.bind('<Escape>',quit)
    lay.mainloop
#===================Mysql integration=====================
def checkpassword(a,b):
    print(a.get(),b.get())
    #mycursor.execute(f"Select password from students where registration=%s"%a)
    #passkey=mycursor.fetchall()
    #for x in passkey:
    #    print(x)
