from tkinter import *
import random
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as tmsg
#from admin_login import syslog 
from PIL import ImageTk, Image
from tkinter import filedialog
from tkcalendar import Calendar,DateEntry
from tkPDFViewer import tkPDFViewer as pdf
#=========================Initialization=======================
Win=Tk()
Win.title("Adminisatrator Access")
Win.geometry("720x720")
backcolour3="#7A2048"
style=("timesnewroman",20,"bold")
style1=("Calibri", 20, "italic")
style2=("Calibri", 15, "italic")
style3=("Calibri", 25, "italic")
front="white"
B="#d0d9d9"
backcolour2="black"
Buttoncolor="#7A2048"
buttontxt="white"
backcolour="#408EC6"
backcolour4="#4a9ad4"

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
            tmsg.showinfo("Success","Task executed")
            reset()
        except:
            tmsg.showerror("Duplicate Entry","User Already Exists or Data Invalid")
            reset()
    if b=="revoke":
        try:
            if tab=="students":
                val = Val1_input.get()
                sql = f"update {tab} set access=0 where registration={val}"
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute(f"Select * from {tab}")
                passkey=mycursor.fetchall()
                #for x in passkey:
                    #print(x)
                reset()
                tmsg.showinfo("Success","Acess Denied")
            elif tab=="instructor":
                vall=(Val1_input.get())
                sql = f"update {tab} set access=0 where Emp_id={vall}"
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute(f"Select * from {tab}")
                passkey=mycursor.fetchall()
                #for x in passkey:
                    #print(x)
                tmsg.showinfo("Success","User Data Updated")
                reset()
            else:
                vall=(Val1_input.get())
                sql = f"update {tab} set access=0 where admin_id={vall}"
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute(f"Select * from {tab}")
                passkey=mycursor.fetchall()
                #for x in passkey:
                    #print(x)
                tmsg.showinfo("Success","User Data Updated")
                reset()
        except:
            tmsg.showerror("Error","Unable To Update Access")
            reset()
    if b=="access":
        try:
            if tab=="students":
                vall=(Val1_input.get())
                sql = f"update {tab} set access=1 where Registration={vall}"
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute(f"Select * from {tab}")
                passkey=mycursor.fetchall()
                #for x in passkey:
                    #print(x)
                tmsg.showinfo("Success","User Data Updated")
                reset()
            elif tab=="instructor":
                vall=(Val1_input.get())
                sql = f"update {tab} set access=1 where Emp_id={vall}"
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute(f"Select * from {tab}")
                passkey=mycursor.fetchall()
                #for x in passkey:
                    #print(x)
                tmsg.showinfo("Success","User Data Updated")
                reset()
            else:
                vall=(Val1_input.get())
                sql = f"update {tab} set access=1 where admin_id={vall}"
                mycursor.execute(sql)
                mydb.commit()
                mycursor.execute(f"Select * from {tab}")
                passkey=mycursor.fetchall()
                #for x in passkey:
                    #print(x)
                tmsg.showinfo("Success","User Data Updated")
                reset()

        except:
            tmsg.showerror("Error","Unable To Update Access")
            reset()
    if b=="delete":
        try:
            val = Val1_input.get()
            sql = f"delete from {tab} where Registration={val}"
            mycursor.execute(sql)
            mydb.commit()
            mycursor.execute(f"Select * from {tab}")
            passkey=mycursor.fetchall()
            #for i in passkey:
                #print(i)
            tmsg.showinfo("Success","User Deleted")
            reset()
        except:
            reset()
    if b=="update":
        try:
            if tab=="students":
                vall=(Val2_input.get(),Val3_input.get(),Val1_input.get())
                sql = f"update {tab} set name=%s,password=%s where Registration=%s"
                mycursor.execute(sql,vall)
                mydb.commit()
                mycursor.execute(f"Select * from {tab}")
                passkey=mycursor.fetchall()
                #for x in passkey:
                    #print(x)
                reset()
                tmsg.showinfo("Success","User Data Updated")
                reset()
            elif tab=="instructor":
                vall=(Val2_input.get(),Val3_input.get(),Val1_input.get())
                sql = f"update {tab} set name=%s,password=%s where Emp_id=%s"
                mycursor.execute(sql,vall)
                mydb.commit()
                mycursor.execute(f"Select * from {tab}")
                passkey=mycursor.fetchall()
                #for x in passkey:
                    #print(x)
                reset()
                tmsg.showinfo("Success","User Data Updated")
                reset()
            else:
                vall=(Val2_input.get(),Val3_input.get(),Val1_input.get())
                sql = f"update {tab} set name=%s,password=%s where Emp_id=%s"
                mycursor.execute(sql,vall)
                mydb.commit()
                mycursor.execute(f"Select * from {tab}")
                passkey=mycursor.fetchall()
                #for x in passkey:
                    #print(x)
                reset()
                tmsg.showinfo("Success","User Data Updated")
                reset()

        except:
            reset()
    if b=="data":
        try:
            reset_1()
            mycursor.execute(f"Select * from {tab}")
            passkey=mycursor.fetchall()
            t1.config(state="normal")
            t1.delete(1.0,END)
            for x in passkey:
                #print(x)
                for j in x:
                    t1.insert(END,f"[{j}]\t")
                t1.insert(END,f"\n")
            t1.config(state="disabled")
        except:
            tmsg.showerror("Error","unable to fetch Data")

var=StringVar()
var1=IntVar()
varx=StringVar()
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
def allow_access():
    a=var.get()
    validatior()
    selected(a,b="access")
def delete_user():
    a=var.get()
    validatior()
    selected(a,b="delete")

def change_data():
    a=var.get()
    validatior()
    selected(a,b="update")

def get_data():
    a=var.get()
    selected(a,b="data")

def reset_1():
    global t1
    t1.config(state="normal")
    t1.delete(1.0,END)

def generate_cert():
    import generate_certificate

def generate_Admission_no(b,c,d,e,f,g,h,i,j,k,l):
    global scs
    b1=b
    c=c
    d=d
    e=e
    f=f
    g=g
    h=h
    i=i
    j=j
    k=k
    l=l
    scs=random.randint(100000,1000000)
    complete_Admission(a=int(scs),b=b1,c=c,d=d,e=e,f=f,g=g,h=h,i=i,j=j,k=k,l=l)
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        xwin=Toplevel(Win)
        img = Image.open(file_path)
        img = img.resize((300, 300), Image.LANCZOS) # Resize image if needed
        img = ImageTk.PhotoImage(img)
        label = Label(xwin, image=img)
        label.image = img # Keep reference to avoid garbage collection
        label.pack()
def upload_file():
    file_path = filedialog.askopenfilename(defaultextension="C:/Users/Adity/Downloads/",filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        # Process the file (e.g., save it to a new location)
        save_file(file_path)
def save_file(file_path):
    save_path = filedialog.asksaveasfilename(defaultextension="C:/Users/Adity/Desktop/mis/Certificates_uploaded",filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if save_path:
        with open(file_path, "rb") as f:
            data = f.read()
        with open(save_path, "wb") as f:
            f.write(data)
def complete_Admission(a,b,c,d,e,f,g,h,i,j,k,l):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aditya@1234",
    database="New_Entry")
    mycursor = mydb.cursor()
    mycursor.execute(f"Insert into student_entry (Registration,Gender,Admission_Branch,Category,Mother,father,DOB,MTounge,Resadd,peradd,CRL) values ({a},{b},{c},{d},{e},{f},{g},{h},{i},{j},{k},{l})")
    tmsg.showinfo("Admission",f"Admission Done! \n Registration number is : {a}")
def make_admission():
    Admission=Toplevel(Win)
    Admission.geometry("800x800")
    Admission.state("zoomed")
    Admission.maxsize(800,800)
    Admission.minsize(800,800)
    Admission.title("New Admission")
    #generate_Admission_no()
    #print(scs)
    ad1=Label(Admission,text="New Admission",background="black",fg="white",font=style)
    ad1.place(relx=0,rely=0,relwidth=1,relheight=0.09)
    ad2=Frame(Admission,bg=backcolour)
    ad2.place(rely=0.1,relx=0,relwidth=1,relheight=0.9)
    ad3=Label(ad2,text="Name",width=20,anchor="w",bg=backcolour4,font=style3)
    ad3.grid(row=0,column=0,pady=2,padx=2)
    ad4=Label(ad2,text="Gender",width=20,anchor="w",bg=backcolour4,font=style3)
    ad4.grid(row=1,column=0,pady=2,padx=2)
    ad5=Label(ad2,text="Admission Branch",width=20,anchor="w",bg=backcolour4,font=style3)
    ad5.grid(row=2,column=0,pady=2,padx=2)
    ad6=Label(ad2,text="Category",width=20,anchor="w",bg=backcolour4,font=style3)
    ad6.grid(row=3,column=0,pady=2,padx=2)
    ad7=Label(ad2,text="Mother's Name",width=20,anchor="w",bg=backcolour4,font=style3)
    ad7.grid(row=4,column=0,pady=2,padx=2)
    ad8=Label(ad2,text="Father's Name",width=20,anchor="w",bg=backcolour4,font=style3)
    ad8.grid(row=5,column=0,pady=2,padx=2)
    ad9=Label(ad2,text="Date Of Birth",width=20,anchor="w",bg=backcolour4,font=style3)
    ad9.grid(row=6,column=0,pady=2,padx=2)
    ad10=Label(ad2,text="Mother Tounge",width=20,anchor="w",bg=backcolour4,font=style3)
    ad10.grid(row=7,column=0,pady=2,padx=2)
    ad11=Label(ad2,text="Residencial Address",width=20,anchor="w",bg=backcolour4,font=style3)
    ad11.grid(row=8,column=0,pady=2,padx=2)
    ad11=Label(ad2,text="Permenant Address",width=20,anchor="w",bg=backcolour4,font=style3)
    ad11.grid(row=9,column=0,pady=2,padx=2)
    ad12=Label(ad2,text="Common Rank",width=20,anchor="w",bg=backcolour4,font=style3)
    ad12.grid(row=10,column=0,pady=2,padx=2)
    ad3a=Entry(ad2,textvariable=StringVar,width=13,bg="white",font=style3)
    ad3a.grid(row=0,column=1,padx=10)
    ad4v=StringVar()
    ad4a=OptionMenu(ad2,ad4v,"Male","Female")
    ad4v.set("Select")
    ad4a.grid(row=1,column=1)
    ad5v=StringVar()
    ad5a=OptionMenu(ad2,ad5v,"Computer Science","Information Technology","Civil Engineering","Mechanical Engineering","Chemical Engineering","Artificial Intelligence","Electronics and Communication","Mining Engineering")
    ad5a.grid(row=2,column=1)
    ad5v.set("Select")
    ad6v=StringVar()
    ad6a=OptionMenu(ad2,ad6v,"Select","General","OBC(NCL)","SC","ST","PWD")
    ad6a.grid(row=3,column=1)
    ad6v.set("Select")
    ad7a=Entry(ad2,textvariable=StringVar,width=13,bg="white",font=style3)
    ad7a.grid(row=4,column=1,padx=10)
    ad8a=Entry(ad2,textvariable=StringVar,width=13,bg="white",font=style3)
    ad8a.grid(row=5,column=1,padx=10)
    sel=StringVar() # declaring string variable 
    cal=DateEntry(ad2,selectmode='day',textvariable=sel)
    cal.grid(row=6,column=1,padx=20)
    ad10a=Entry(ad2,textvariable=StringVar,width=13,bg="white",font=style3)
    ad10a.grid(row=7,column=1,padx=10)
    ad11a=Entry(ad2,textvariable=StringVar,width=13,bg="white",font=style3)
    ad11a.grid(row=8,column=1,padx=10)
    ad12a=Entry(ad2,textvariable=StringVar,width=13,bg="white",font=style3)
    ad12a.grid(row=9,column=1,padx=10)
    ad13a=Entry(ad2,textvariable=StringVar,width=13,bg="white",font=style3)
    ad13a.grid(row=10,column=1,padx=10)
    ad15=Label(ad2,text="Upload Document",width=20,anchor="w",bg=backcolour4,font=style3)
    ad15.grid(row=11,column=0,pady=4)
    ad16b=Button(ad2,text="Upload Aadhar",command=upload_file,anchor="w",width=15,font=style2)
    ad16b.grid(row=11,column=1,pady=3)
    ad16b=Button(ad2,text="Upload Migration",command=upload_file,anchor="w",width=15,font=style2)
    ad16b.grid(row=11,column=2,pady=3)
    ad16c=Button(ad2,text="Upload Rank Card",command=upload_file,anchor="w",width=15,font=style2)
    ad16c.grid(row=12,column=1,pady=3)
    ad16d=Button(ad2,text="Upload TC",command=upload_file,anchor="w",width=15,font=style2)
    ad16d.grid(row=12,column=2,pady=3)
    vary=StringVar()
    #TC,Aadhar,Migration,Rankcard
    #ad16a=Checkbutton(ad2,text="Aadhar",background=backcolour,fg="black",font=style2,activebackground=backcolour3,variable=vary,onvalue="NA",offvalue="Aadhar",command=filedialog.askopenfile(mode="r"))
    #ad16a.grid(row=12,column=0)
    d1=ad3a.get()
    d2=ad4v.get()
    d3=ad5v.get()
    d4=ad6v.get()
    d5=ad7a.get()
    d6=ad8a.get()
    d7=str(sel.get())
    d8=ad10a.get()
    d9=ad11a.get()
    d10=ad12a.get()
    d11=ad13a.get()
    ad14=Button(ad2,text="Submit and Generate Registration Number",bg="red",fg="white",command=generate_Admission_no(b=d1,c=d2,d=d3,e=d4,f=d5,g=d6,h=d7,i=d8,j=d9,k=d10,l=d11))
    Admission.bind('<Escape>',quit)
#===============================================================
Admin_Label=Label(Win,text="Administrator Panel",background=backcolour2,fg=front,font=style,relief=GROOVE)
Admin_Label.place(x=0,y=0,relwidth=1,height=50)
Back=Button(Win,text="<",font=style,command=back_command,background="black",fg="white")
Back.place(x=0,y=0,height=50,width=50)
F1=LabelFrame(Win,text="Client MIS Portal",bg=backcolour,font=style,labelanchor="n")
F1.place(x=2,y=55,relwidth=1,height=400)
Type=Radiobutton(F1,text="Student",font=style,background=backcolour,activebackground=backcolour,value="Student",variable=var,command=selected(var.get()),state="active")
Type.grid(row=0,column=0)
Type1=Radiobutton(F1,text="Instructor",font=style,background=backcolour,activebackground=backcolour,variable=var,value="Instructor",command=selected(var.get()))
Type1.grid(row=0,column=1)
Type2=Radiobutton(F1,text="Administrator",font=style,background=backcolour,activebackground=backcolour,variable=var,value="Administrator",command=selected(var.get()))
Type2.grid(row=0,column=2)
Val1=Label(F1,text="Registration no:",bg=backcolour,font=style)
Val1.grid(row=1,column=0)
Val1_input=Entry(F1,textvariable=IntVar,disabledbackground="white",background="white",font=style2)
Val1_input.grid(row=1,column=1,ipadx=4)
Val2=Label(F1,text="Name:",bg=backcolour,font=style)
Val2.grid(row=1,column=2)
Val2_input=Entry(F1,textvariable=StringVar,disabledbackground="white",background="white",font=style2)
Val2_input.grid(row=1,column=3,ipadx=0)
Val3=Label(F1,text="     Password:",bg=backcolour,font=style)
Val3.grid(row=1,column=4,padx=3)
Val3_input=Entry(F1,textvariable=StringVar,disabledbackground="white",background="white",font=style2)
Val3_input.grid(row=1,column=5,ipadx=4)
Val4=Checkbutton(F1,text="Do you want to make\n the changes applicable",background=backcolour,fg="black",font=style2,activebackground=backcolour3,variable=var1,onvalue=1,offvalue=0)
Val4.grid(row=3,column=0,pady=10)
Val5=Button(F1,text="Add User",background=Buttoncolor,font=style,fg="white",activebackground=backcolour,width=15,command=add_user)
Val5.grid(row=5,column=0,padx=15)
Val6=Button(F1,text="Change User Data",background=Buttoncolor,fg="white",font=style,activebackground=backcolour,width=15,command=change_data)
Val6.grid(row=5,column=1,padx=15)
Val7=Button(F1,text="Revoke User",background=Buttoncolor,fg="white",font=style,activebackground=backcolour,width=15,command=revoke_user)
Val7.grid(row=5,column=2,padx=15)
Val8=Label(F1,text=captcha,font=style3,bg="#dbcad0",width=15)
Val8.grid(row=4,column=0,pady=10)
Val8_input=Entry(F1,textvariable=StringVar,background="white",font=style3,width=15)
Val8_input.grid(row=4,column=1,padx=10,pady=10)
Val9=Button(F1,text="Allow User",background=Buttoncolor,fg="white",font=style,activebackground=backcolour,width=15,command=allow_access)
Val9.grid(row=6,column=0,pady=10)
Val10=Button(F1,text="Reset",background=Buttoncolor,fg="white",font=style,activebackground=backcolour,width=15,command=reset)
Val10.grid(row=6,column=1,pady=10)
Val11=Button(F1,text="Delete",background=Buttoncolor,fg="white",font=style,activebackground=backcolour,width=15,command=delete_user)
Val11.grid(row=6,column=2,pady=10)
F2=LabelFrame(Win,text="Details",font=style,labelanchor="n")
F2.place(x=5,y=460,relwidth=0.5,relheight=0.43)
t1=Text(F2,state="normal",padx=1,pady=1,font=style3)
t1.place(x=0,y=0,relwidth=1,relheight=0.75)
scrollbar = Scrollbar(t1)
scrollbar.pack( side = RIGHT, fill=Y )
scrollbar.config(command=t1.yview,jump=1,orient=VERTICAL)
t1.config(yscrollcommand=scrollbar.set)
ValF2_1=Button(F2,text="Fetch all data",background=Buttoncolor,fg="white",font=style,activebackground=backcolour,width=15,command=get_data)
ValF2_1.place(x=50,y=260)
ValF2_2=Button(F2,text="Reset",background=Buttoncolor,fg="white",font=style,activebackground=backcolour,width=15,command=reset_1)
ValF2_2.place(x=400,y=260)
F3=LabelFrame(Win,text="Action Pane",labelanchor="n",font=style)
F3.place(x=800,y=460,relheight=0.43,relwidth=0.47)
Actp=Button(F3,text="Get Complete Student Details",height=3,width=30)
Actp.grid(row=0,column=0,padx=4,pady=4)
Actp1=Button(F3,text="Get Student Fees Details",height=3,width=30)
Actp1.grid(row=1,column=0,padx=4,pady=4)
Actp2=Button(F3,text="See Complete Student Document",height=3,width=30,command=open_image)
Actp2.grid(row=2,column=0,padx=4,pady=4)
Actp3=Button(F3,text="Make new Admission",height=3,width=30,command=make_admission)
Actp3.grid(row=3,column=0,padx=4,pady=4)
Actp4=Button(F3,text="Transfer Student",height=3,width=30)
Actp4.grid(row=4,column=0,padx=4,pady=4)
#============================================================#
EActp=Button(F3,text="Get Complete Employee Details",height=3,width=30)
EActp.grid(row=0,column=1,padx=4,pady=4)
EActp1=Button(F3,text="Get Employee Salary Details",height=3,width=30)
EActp1.grid(row=1,column=1,padx=4,pady=4)
EActp2=Button(F3,text="See Employee Document",height=3,width=30)
EActp2.grid(row=2,column=1,padx=4,pady=4)
EActp3=Button(F3,text="Take Onboard",height=3,width=30)
EActp3.grid(row=3,column=1,padx=4,pady=4)
EActp4=Button(F3,text="Relief Instructor",height=3,width=30)
EActp4.grid(row=4,column=1,padx=4,pady=4)
#================================================================
EActp=Button(F3,text="Send Promotional Emails",height=3,width=30)
EActp.grid(row=0,column=2,padx=4,pady=4)
EActp1=Button(F3,text="Generate Certificates",height=3,width=30,command=generate_cert)
EActp1.grid(row=1,column=2,padx=4,pady=4)
EActp2=Button(F3,text="Generate Grade Cards",height=3,width=30)
EActp2.grid(row=2,column=2,padx=4,pady=4)
EActp3=Button(F3,text="Check Student Attendence",height=3,width=30)
EActp3.grid(row=3,column=2,padx=4,pady=4)
EActp4=Button(F3,text="Instructor Attendence",height=3,width=30)
EActp4.grid(row=4,column=2,padx=4,pady=4)
Copy=Label(Win,text="COPYRIGHTS ABC INSTITUTE OF TECHNOLOGY",font=("timesnewroman",10,"bold"),border=2,relief="raise")
Copy.pack(fill=X,anchor="s",side="bottom")
#===================Closing Attributes==========================
Win.attributes("-fullscreen",True)
Win.bind('<Escape>',quit)
Win.mainloop()
