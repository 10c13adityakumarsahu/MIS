from tkinter import *
import random
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as tmsg
from PIL import ImageTk, Image
import time
from time import strftime
from datetime import date


Win=Tk()
Win.title("Generate Certificates")
Win.geometry("1080x720")
backcolour3="#7A2048"
style=("timesnewroman",20,"bold")
style1=("Calibri", 20, "italic")
style2=("Calibri", 22, "italic")
style3=("Calibri", 25, "italic")
front="white"
B="#d0d9d9"
backcolour2="black"
Buttoncolor="#7A2048"
buttontxt="white"
backcolour="#408EC6"
z=""
def certification_no():
    global z
    x=random.randint(0,100000000)
    y=str(date.today())
    z=(y)+"/"+str(x)
def disabled():
    Cert1.config(state="disabled")
    Cert2.config(state="disabled")
    Cert3.config(state="disabled")
    Cert4.config(state="disabled")
    Cert5.config(state="disabled")
    Cert6.config(state="disabled")
    Cert7.config(state="disabled")
    Cert8.config(state="disabled")
    Cert9.config(state="disabled")
    Cert10.config(state="disabled")

def enabled():
    Cert1.config(state="normal")
    Cert2.config(state="normal")
    Cert3.config(state="normal")
    Cert4.config(state="normal")
    Cert5.config(state="normal")
    Cert6.config(state="normal")
    Cert7.config(state="normal")
    Cert8.config(state="normal")
    Cert9.config(state="normal")
    Cert10.config(state="normal")

def bonafied():
    certification_no()
    global z
    text1.insert(END,f'Certificate Number:{z}\n')
    file_path = r"C:\Users\Adity\Desktop\mis\Bonafide.txt"  # Replace with your file path
    with open(file_path) as file:
        content = file.read()
        text1.insert(END, content)
        disabled()
    
def Noc():
    certification_no()
    global z
    text1.insert(END,f'Certificate Number:{z}\n')
    file_path = r"C:\Users\Adity\Desktop\mis\Noc.txt"  # Replace with your file path
    with open(file_path) as file:
        content = file.read()
        text1.insert(END, content)
        disabled()

def Char():
    certification_no()
    global z
    text1.insert(END,f'Certificate Number:{z}\n')
    file_path = r"C:\Users\Adity\Desktop\mis\Char.txt"  # Replace with your file path
    with open(file_path) as file:
        content = file.read()
        text1.insert(END, content)
        disabled()

def Migr():
    certification_no()
    global z
    text1.insert(END,f'Certificate Number:{z}\n')
    file_path = r"C:\Users\Adity\Desktop\mis\Migr.txt"  # Replace with your file path
    with open(file_path) as file:
        content = file.read()
        text1.insert(END, content)
        disabled()

def ND():
    certification_no()
    global z
    text1.insert(END,f'Certificate Number:{z}\n')
    file_path = r"C:\Users\Adity\Desktop\mis\NoDue.txt"  # Replace with your file path
    with open(file_path) as file:
        content = file.read()
        text1.insert(END, content)
        disabled()

def TrC():
    certification_no()
    global z
    text1.insert(END,f'Certificate Number:{z}\n')
    file_path = r"C:\Users\Adity\Desktop\mis\TC.txt"  # Replace with your file path
    with open(file_path) as file:
        content = file.read()
        text1.insert(END, content)
        disabled()
    
def Appo():
    certification_no()
    global z
    text1.insert(END,f'Certificate Number:{z}\n')
    file_path = r"C:\Users\Adity\Desktop\mis\Acc.txt"  # Replace with your file path
    with open(file_path) as file:
        content = file.read()
        text1.insert(END, content)
        disabled()

def relif():
    certification_no()
    global z
    text1.insert(END,f'Certificate Number:{z}\n')
    file_path = r"C:\Users\Adity\Desktop\mis\rlv.txt"  # Replace with your file path
    with open(file_path) as file:
        content = file.read()
        text1.insert(END, content)
        disabled()    

def exp():
    certification_no()
    global z
    text1.insert(END,f'Certificate Number:{z}\n')
    file_path = r"C:\Users\Adity\Desktop\mis\Expltr.txt"  # Replace with your file path
    with open(file_path) as file:
        content = file.read()
        text1.insert(END, content)
        disabled()
    
def rec():
    certification_no()
    global z
    text1.insert(END,f'Certificate Number:{z}\n')
    file_path = r"C:\Users\Adity\Desktop\mis\reco.txt"  # Replace with your file path
    with open(file_path) as file:
        content = file.read()
        text1.insert(END, content)
        disabled()


def savecert():
    op=tmsg.askyesno('Save Certificate','Do you want to save this Certificate')
    if op>0:
        bill_details=text1.get(1.0,END)
        f1=open("C:/Users/Adity/Desktop/cert/"+str(z)+".txt",'a')
        f1.write(bill_details)
        f1.close()
        tmsg.showinfo('Saved',"Certificate is issued and saved")
def res():
    text1.delete(1.0,END)
    enabled()

Certify=Frame(Win,bg="white")
Certify.place(x=0,y=3,relheight=1,relwidth=0.795)
Name=Label(Certify,text="Certificate",font=style)
Name.place(relx=0.01,rely=0.005,relheight=0.04,relwidth=0.97)
text1=Text(Certify,bg="#d9ddde",font=style2)
text1.place(relx=0.01,rely=0.05,relheight=0.95,relwidth=0.97)
Commands=LabelFrame(Win,text="Command",font="style",bg=backcolour,labelanchor="n")
Commands.place(relx=0.8,rely=0.001,relheight=1,relwidth=0.2)
Cert1=Button(Commands,text="Bonafide Certificate",command=bonafied)
Cert1.place(relx=0.05,y=8,relwidth=0.9,relheight=0.07)
Cert2=Button(Commands,text="No objection Certificate",command=Noc)
Cert2.place(relx=0.05,y=68,relwidth=0.9,relheight=0.07)
Cert3=Button(Commands,text="Character Certificate",command=Char)
Cert3.place(relx=0.05,y=128,relwidth=0.9,relheight=0.07)
Cert4=Button(Commands,text="Migration Certificate",command=Migr)
Cert4.place(relx=0.05,y=188,relwidth=0.9,relheight=0.07)
Cert5=Button(Commands,text="No Due Certificate",command=ND)
Cert5.place(relx=0.05,y=248,relwidth=0.9,relheight=0.07)
Cert6=Button(Commands,text="Transfer Certificate",command=TrC)
Cert6.place(relx=0.05,y=308,relwidth=0.9,relheight=0.07)
Cert7=Button(Commands,text="Appointment Letter",command=Appo)
Cert7.place(relx=0.05,y=368,relwidth=0.9,relheight=0.07)
Cert8=Button(Commands,text="Reliving Letter",command=relif)
Cert8.place(relx=0.05,y=428,relwidth=0.9,relheight=0.07)
Cert9=Button(Commands,text="Experience Letter",command=exp)
Cert9.place(relx=0.05,y=488,relwidth=0.9,relheight=0.07)
Cert10=Button(Commands,text="Letter of Recommendation",command=rec)
Cert10.place(relx=0.05,y=548,relwidth=0.9,relheight=0.07)
Cert11=Button(Commands,text="Save Certificate",command=savecert)
Cert11.place(relx=0.05,y=608,relwidth=0.9,relheight=0.07)
Cert12=Button(Commands,text="Mail Certificate")
Cert12.place(relx=0.05,y=668,relwidth=0.9,relheight=0.07)
Cert13=Button(Commands,text="Reset",bg="red",fg="white",command=res)
Cert13.place(relx=0.05,y=728,relwidth=0.9,relheight=0.05)

Win.bind('<Escape>',quit)
Win.mainloop()