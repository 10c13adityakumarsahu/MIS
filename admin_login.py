from tkinter import *
import random
import mysql.connector
from tkinter import messagebox as tmsg
#=====================Initialization======================
Win=Tk()
Win.title("Administrator Login")
Win.geometry("500x500")
Win.resizable(False,False)
backcolour="#408EC6"
style=("timesnewroman",20,"bold")
front="#F9DBBD"
backcolour2="#9A348E"
Buttoncolor="#F9DBBD"
buttontxt="#0D0628"
#=====================Databased estrablishment===========
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aditya@1234",
  database="Admin_Info")

mycursor = mydb.cursor()
#======================Captcha===========================
captcha=random.randint(10000,99999)
def admin_console():
    Win.destroy()
    import admin_console
    
def generate_new_captcha():
    global captcha
    captcha1=random.randint(10000,99999)
    F10.config(text=captcha1)
    F11.delete(0,END)
    captcha=captcha1
#=====================Variables==========================
passwordvar=StringVar
registrationvar=IntVar
captchavar=IntVar
#===================Mysql integration=====================
def checkpassword(event=None):
    try:
        a=int(F11.get())
        b=F8.get()
    except:
        tmsg.showerror("Invalid Credintials","Enter your details")
    c=registration_id.get()
    mycursor.execute(f"Select * from admin_info where admin_id={c}")
    passkey=mycursor.fetchall()
    if captcha!=a:
        tmsg.showerror("Error","Error Captcha")
        generate_new_captcha()
        return
    for x in passkey:
        #print(x)
        if len(x)==0:
            tmsg.showerror("Warning","Incorrect Credentials")
        elif x[2]==b:
            tmsg.showinfo("Login",f"Login Successful {x[1]}")
            syslog(x[0])
            admin_console()
        else:
            tmsg.showerror("Warning","Incorrect Credentials")
    
    
#====================reload===========================
def reload_window():
    registration_id.delete(0,END)
    F8.delete(0,END)
    F11.delete(0,END)
    registration_id.focus()
    generate_new_captcha()
'''def dataset_verification():
    if len(F11.get())!=:
        tmsg.showerror("Error","Error Captcha")
        reload_window()'''
#=====================================================
def back_command():
    Win.destroy()
    import admin

#====================Environment=======================
F3=Label(Win,text="Administrator Login",font=style,background="black",foreground="white",border="2",padx=1,relief=GROOVE)
F3.place(x=0,y=0,relwidth=1,height=50)
Back=Button(Win,text="<",font=style,command=back_command,background="black",fg="white")
Back.place(x=0,y=0,height=50,width=50)
F4=Frame(Win,background=backcolour,padx=17)
F4.place(x=0,y=55,relwidth=1,relheight=0.9)
F5=Label(F4,text="Administrator ID:",font=style,background=backcolour,foreground=front,anchor="nw",width=13,border="2")
F5.grid(row=0,column=0,pady=2)
F6=Label(F4,text="Password:",font=style,background=backcolour,foreground=front,anchor="nw",width=13,border="2")
F6.grid(row=1,column=0,pady=2)
registration_id=Entry(F4,width=15,font=style,textvariable=registrationvar,border="3")
registration_id.grid(row=0,column=1,pady=2)
F8=Entry(F4,width=15,font=style,textvariable=passwordvar,border="3",show='*')
F8.grid(row=1,column=1,pady=2)
F9=Label(F4,text="Enter Captcha:",font=style,background=backcolour,foreground=front,anchor="nw",width=13,border="2")
F9.grid(row=2,column=0,pady=2)
F10=Label(F4,text=captcha,font=style,background="white",foreground="black",anchor="nw",width=5,border="2")
F10.grid(row=3,column=0)
Copy=Label(Win,text="COPYRIGHTS ABC INSTITUTE OF TECHNOLOGY",font=("timesnewroman",10,"bold"),border="2")
F11=Entry(F4,width=15,font=style,textvariable=captchavar,border="2")
F11.grid(row=3,column=1)
Reset=Button(F4,text="Reset",font=("timesnewroman",10,"bold"),width=27,height=2,command=reload_window)
Reset.grid(row=5,column=0,pady=10)
Submit=Button(F4,text="Login",font=("timesnewroman",10,"bold"),width=27,command=checkpassword,height=2)
Submit.grid(row=5,column=1,pady=10)
Copy.pack(fill=X,anchor="s",side="bottom")
#============take forward===========================
def syslog(a):
    user=a
    print(user)
Win.bind('<Escape>',quit)
Win.bind('<Return>',checkpassword)
Win.mainloop()