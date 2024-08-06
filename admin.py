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
backcolour2="#9A348E"
Buttoncolor="#F9DBBD"
buttontxt="#0D0628"
win.resizable(False,False)
#=====================App Logo============================
#=====================Dependencies========================
def run_student():
    import runner
    return
def run_instructor():
    import teacher_login
    return
def run_admin():
    import admin_login
#=====================Title===============================
F1= Frame(win,bg=backcolour,relief="solid",border="2")
F1.pack(fill="x",pady=10,padx=2)
a= Label(F1,text="ABC INSTITUTE OF TECHNOLOGY ",font=("timesnewroman",20,"bold"),fg=front,bg=backcolour,justify=CENTER)
a.pack(padx=10,pady=10)
#====================Login background======================
F2= LabelFrame(win,text="Login as",bg=backcolour2,relief="solid",border="2",fg=front,labelanchor="n",font=style,padx=2)
F2.place(x=0,y=80,relwidth=1,height=350)
# ==================Login Buttons==========================
Student=Button(F2,text="Student",padx=20,pady=20,width=10,background=Buttoncolor,command=run_student,fg=buttontxt,relief=SUNKEN)
Student.place(x=60,y=70)
Instructor=Button(F2,text="Instructor",padx=20,pady=20,width=10,background=Buttoncolor,fg=buttontxt,command=run_instructor)
Instructor.place(x=220,y=70)
Admin=Button(F2,text="Administrator",padx=20,pady=20,width=10,background=Buttoncolor,fg=buttontxt)
Admin.place(x=370,y=70)
#===================Copyrights============================
Copy=Label(win,text="COPYRIGHTS ABC INSTITUTE OF TECHNOLOGY",font=("timesnewroman",10,"bold"),border="2")
Copy.pack(fill=X,anchor="s",side="bottom")
#===================Closing Attributes====================
win.bind('<Escape>',quit)
win.mainloop()