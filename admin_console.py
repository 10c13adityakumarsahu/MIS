from tkinter import *
import random
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as tmsg
#from admin_login import syslog 
from PIL import ImageTk, Image
#=========================Initialization=======================
Win=Tk()
Win.title("Adminisatrator Access")
Win.geometry("720x720")
backcolour3="#e882a6"
style=("timesnewroman",20,"bold")
style1=("Calibri", 20, "italic")
style2=("Calibri", 15, "italic")
style3=("Calibri", 25, "italic")
front="white"
backcolour2="black"
Buttoncolor="#82E8C4"
buttontxt="#0D0628"
backcolour="#d65a86"
l1=[]
#===========Admin User id===================================
def selected(a,b="sec"):
    global user
    global l1
    user=a
    l1.append(user)
    c=b
    sql_commands(user,c)

def sql_commands(a,b="select"):
    if a=="Student":
        tab="students"
        dab="Student_Info"
    elif a=="Instructor":
        tab="instructor"
        dab="Teacher_Info"
    else:
        dab="Admin_Info"
        tab="admin_info"
    mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aditya@1234",
  database=f"{dab}")
    mycursor = mydb.cursor()

    if b=="add":
        try:
            sql = f"INSERT INTO {tab} VALUES (%s, %s,%s,%s)"
            val = (Val1_input.get(), Val2_input.get(),Val3_input.get(),1)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.execute(f"Select * from {tab}")
            passkey=mycursor.fetchall()
            for x in passkey:
                print(x)
            tmsg.showinfo("Success","Task executed")
        except:
            tmsg.showerror("Duplicate Entry","User Already Exists")
    if b=="revoke":
        val = Val1_input.get()
        sql = f"update {tab} set access=0 where Registration={val}"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.execute(f"Select * from {tab}")
        passkey=mycursor.fetchall()
        for x in passkey:
            print(x)
    if b=="access":
        val = Val1_input.get()
        sql = f"update {tab} set access=1 where Registration={val}"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.execute(f"Select * from {tab}")
        passkey=mycursor.fetchall()
        for x in passkey:
            print(x)



    


var=StringVar()
var1=IntVar()
#============Captcha=========================================
def back_command():
    if tmsg.askyesno("Back","Do you want to go back \n unsaved changes will not reflect")==True:
        Win.destroy()
        import admin
    else:
        pass
captcha=random.randint(10000,99999)
def generate_new_captcha():
    global captcha
    captcha1=random.randint(10000,99999)
    Val8.config(text=captcha1)
    Val8_input.delete(0,END)
    captcha=captcha1
def reset():
    Val1_input.delete(0,END)
    Val2_input.delete(0,END)
    Val3_input.delete(0,END)
    Val4.deselect()
    Val8_input.delete(0,END)
    generate_new_captcha()
def validatior():
    if var1.get()==0:
            tmsg.showerror("Error","Accept to continue")
    if str(captcha)!=Val8_input.get():
            tmsg.showerror("Error Captcha","Wrong Captcha! Retry")
            reset()
def add_user():
    a=var.get()
    validatior()
    selected(a,b="add")
def revoke_user():
    a=var.get()
    validatior()
    selected(a,b="revoke")
    tmsg.showinfo("Success","acess denied")
def allow_access():
    a=var.get()
    validatior()
    selected(a,b="access")
    tmsg.showinfo("Success","access granted")

#===============================================================
Admin_Label=Label(Win,text="Administrator Panel",background=backcolour2,fg=front,font=style,relief=GROOVE)
Admin_Label.place(x=0,y=0,relwidth=1,height=50)
Back=Button(Win,text="<",font=style,command=back_command,background="black",fg="white")
Back.place(x=0,y=0,height=50,width=50)
F1=LabelFrame(Win,text="Add User to Client",bg=backcolour,font=style,labelanchor="n")
F1.place(x=2,y=55,relwidth=1,height=400)
Type=Radiobutton(F1,text="Student",font=style,background=backcolour,activebackground=backcolour3,value="Student",variable=var,command=selected(var.get()))
Type.grid(row=0,column=0)
Type1=Radiobutton(F1,text="Instructor",font=style,background=backcolour,activebackground=backcolour3,variable=var,value="Instructor",command=selected(var.get()))
Type1.grid(row=0,column=1)
Type2=Radiobutton(F1,text="Administrator",font=style,background=backcolour,activebackground=backcolour3,variable=var,value="Administrator",command=selected(var.get()))
Type2.grid(row=0,column=2)
Val1=Label(F1,text="Registration no:",bg=backcolour,font=style)
Val1.grid(row=1,column=0)
Val1_input=Entry(F1,textvariable=IntVar,disabledbackground="white",background="#dbcad0",font=style2)
Val1_input.grid(row=1,column=1,ipadx=4)
Val2=Label(F1,text="Name:",bg=backcolour,font=style)
Val2.grid(row=1,column=2)
Val2_input=Entry(F1,textvariable=StringVar,disabledbackground="white",background="#dbcad0",font=style2)
Val2_input.grid(row=1,column=3,ipadx=0)
Val3=Label(F1,text="     Password:",bg=backcolour,font=style)
Val3.grid(row=1,column=4,padx=3)
Val3_input=Entry(F1,textvariable=StringVar,disabledbackground="white",background="#dbcad0",font=style2)
Val3_input.grid(row=1,column=5,ipadx=4)
Val4=Checkbutton(F1,text="Do you want to make\n the changes applicable",background=backcolour,fg="black",font=style2,activebackground=backcolour3,variable=var1,onvalue=1,offvalue=0)
Val4.grid(row=3,column=0,pady=10)
Val5=Button(F1,text="Add User",background=Buttoncolor,font=style,activebackground=backcolour,width=15,command=add_user)
Val5.grid(row=5,column=0,padx=15)
Val6=Button(F1,text="Change User Data",background=Buttoncolor,font=style,activebackground=backcolour,width=15)
Val6.grid(row=5,column=1,padx=15)
Val7=Button(F1,text="Revoke User",background=Buttoncolor,font=style,activebackground=backcolour,width=15,command=revoke_user)
Val7.grid(row=5,column=2,padx=15)
Val8=Label(F1,text=captcha,font=style3,bg="white",width=15)
Val8.grid(row=4,column=0,pady=10)
Val8_input=Entry(F1,textvariable=StringVar,background="#dbcad0",font=style3,width=15)
Val8_input.grid(row=4,column=1,padx=10,pady=10)
Val9=Button(F1,text="Allow User",background=Buttoncolor,font=style,activebackground=backcolour,width=15,command=allow_access)
Val9.grid(row=6,column=0,pady=10)
Val10=Button(F1,text="Reset",background=Buttoncolor,font=style,activebackground=backcolour,width=15,command=reset)
Val10.grid(row=6,column=1,pady=10)
Val11=Button(F1,text="Delete",background=Buttoncolor,font=style,activebackground=backcolour,width=15)
Val11.grid(row=6,column=2,pady=10)
#===================Closing Attributes==========================
Win.attributes("-fullscreen",True)
Win.bind('<Escape>',quit)
Win.mainloop()
