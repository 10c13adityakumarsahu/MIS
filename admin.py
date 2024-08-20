from tkinter import *
import random
import mysql.connector
#=====================Initialization======================
win=Tk()
win.title("Login")
win.geometry("560x360")
backcolour="#DA627D"
style=("timesnewroman",20,"bold")
front="#F9DBBD"
backcolour2="#408EC6"
Buttoncolor="#F9DBBD"
buttontxt="#0D0628"
win.resizable(False,False)
#=====================App Logo============================
#=====================Dependencies========================
def back_command():
    win.destroy()
def run_student():
    win.destroy()
    import student_login
    
def run_instructor():
    win.destroy()
    import teacher_login
    
def run_admin():
    win.destroy()
    import admin_login
    
#=====================Title===============================
F1= Frame(win,bg=backcolour,relief="solid",border="2")
F1.pack(fill="x",pady=10,padx=2)
a= Label(F1,text="ABC INSTITUTE OF TECHNOLOGY ",font=("timesnewroman",20,"bold"),fg=front,bg=backcolour,justify=CENTER)
a.pack(padx=10,pady=10)
#Back=Button(win,text="X",font=style,command=back_command,background="black",fg="white")
#Back.place(x=0,y=0,height=50,width=50)
#====================Login background======================
F2= LabelFrame(win,text="Login as",bg=backcolour2,relief="solid",border="2",fg=front,labelanchor="n",font=style,padx=2)
F2.place(x=0,y=80,relwidth=1,height=350)
# ==================Login Buttons==========================
Student=Button(F2,text="Student",padx=20,pady=20,width=10,background=Buttoncolor,command=run_student,fg=buttontxt,relief=SUNKEN)
Student.place(x=60,y=70)
Instructor=Button(F2,text="Instructor",padx=20,pady=20,width=10,background=Buttoncolor,fg=buttontxt,command=run_instructor)
Instructor.place(x=220,y=70)
Admin=Button(F2,text="Administrator",padx=20,pady=20,width=10,background=Buttoncolor,fg=buttontxt,command=run_admin)
Admin.place(x=370,y=70)
#===================Copyrights============================
Copy=Label(win,text="COPYRIGHTS ABC INSTITUTE OF TECHNOLOGY",font=("timesnewroman",10,"bold"),border="2")
Copy.pack(fill=X,anchor="s",side="bottom")
#===================Closing Attributes====================
win.bind('<Escape>',quit)
win.mainloop()