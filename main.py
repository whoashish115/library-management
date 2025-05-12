from tkcalendar import *
from customtkinter import *
from tkinter import *
from customtkinter import CTkToplevel
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import messagebox
from pymysql import *
import time

con = connect(host='localhost', user='root', password="root")
mycursor = con.cursor()
try:
    query = 'create database library;'
    mycursor.execute(query)
except:
    pass
query = 'use library;'
mycursor.execute(query)
try:
    query = 'create table storebook(bookid int primary key, title varchar(100), author varchar(50), edition varchar(50),issue_status varchar(1000), issued_to varchar(1000), price int);'
    mycursor.execute(query)
except:
    pass
try:
    query = 'create table  bookissued_data(roll_no int,from_date date,to_date date,bookid int primary key);'
    mycursor.execute(query)
except:
    pass
try:
    query = 'create table student_data(roll_no bigint primary key, student_name varchar(100), student_course varchar(50), phone numeric(10), college_name varchar(25));'
    mycursor.execute(query)
except:
    pass

dashwin = CTk(fg_color='#092042')
dashwin.geometry("1200x550+300+100")
dashwin.resizable(False, False)
dashwin.iconbitmap('assets/icon.ico')
dashwin.title("Library Management System")
try:
    from ctypes import windll, byref, sizeof, c_int
    HWND = windll.user32.GetParent(dashwin.winfo_id())
    title_bar_color = 0x0000000
    title_text_color = 0xFFFFFF00
    windll.dwmapi.DwmSetWindowAttribute( HWND,
    35,
    byref(c_int(title_bar_color)), sizeof(c_int))
    windll.dwmapi.DwmSetWindowAttribute(
    HWND,
    36,
    byref(c_int(title_text_color)), sizeof(c_int))
except:
    pass
bg = PhotoImage(file = "assets/bg.png")
back = PhotoImage(file='assets/back.png')

# =================================================================================================================================================
# ============================================================== Add Book Frame ===================================================================
addbookframe = Frame(dashwin, bg="#092042",relief = 'flat' ,bd= 0)
addbookframe.place(x=0,y=0,relwidth = 1, relheight=1)
Label(addbookframe, image=bg).place(x=0, y=0,relwidth = 1 ,relheight = 1)
Button(addbookframe, bd=0, image=back, command=lambda: dashboardframe.tkraise(),bg = '#092042', activebackground='#1857b5').place(x=10, y=10)
miniaddbookframe = Frame(addbookframe, bg='#d1dbeb',height =380,width =550 ,relief = 'flat' ,bd = 4)
miniaddbookframe.place(x=160, y=20)
addbookframe_title = Label(miniaddbookframe, text="ADD BOOK", bg="#092042", font=("Arial", 15, "bold"),relief = 'flat' ,fg='white',width = 41)
addbookframe_title.place(x=20, y=10)
idval = StringVar()
idLabel = Label(miniaddbookframe, text="Book ID :", font=("Arial", 15, "bold"), bg='#D1DEE4')
idLabel.place(x=80, y=72)
idEntry = Entry(miniaddbookframe, textvariable=idval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT, width=15)
idEntry.place(x=190, y=70)
titleLabel = Label(miniaddbookframe, text="TITLE :", font=("Arial", 15, "bold"), bg='#D1DEE4')
titleLabel.place(x=80, y=122)
titleval = StringVar()
titleEntry = Entry(miniaddbookframe, textvariable=titleval , bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,
                   width=30)
titleEntry.place(x=190, y=120)
authorLabel = Label(miniaddbookframe, text="Author", font=("Arial", 15, "bold"), bg='#D1DEE4')
authorLabel.place(x=80, y=172)
authorval = StringVar()
authorEntry = Entry(miniaddbookframe, textvariable=authorval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,
                    width=30)
authorEntry.place(x=190, y=170)
editionLabel = Label(miniaddbookframe, text="Edition", font=("Arial", 15, "bold"), bg='#D1DEE4')
editionLabel.place(x=80, y=222)
editionval = StringVar()
editionEntry = Entry(miniaddbookframe, textvariable=editionval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,width=30)
editionEntry.place(x=190, y=220)
priceLabel = Label(miniaddbookframe, text="Price", font=("Arial", 15, "bold"), bg='#D1DEE4')
priceLabel.place(x=80, y=272)
priceval = StringVar()
priceEntry = Entry(miniaddbookframe, textvariable=priceval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,
                   width=15)
priceEntry.place(x=190, y=270)
def addbooksubmitbtnfunc():
    if (
            idval.get() == "" or titleval.get() == "" or authorval.get() == "" or editionval.get() == "" or priceval.get() == ""):
        messagebox.showinfo("Info", "All Fields are requi#095070...", parent=dashwin)
    else:
        query = "Select bookid,title,author,edition,price from storebook where bookid=%s"
        r = mycursor.execute(query, (idval.get()))
        if (r == True):
            messagebox.showinfo("Info", "Book ID already exists!!!", parent=dashwin)
        else:
            query = "insert into storebook(bookid,title,author,edition,price) values(%s,%s,%s,%s,%s);"
            r = mycursor.execute(query,
                                 (idval.get(), titleval.get(), authorval.get(), editionval.get(), priceval.get()))
            if (r == True):
                messagebox.showinfo("Notification", "Book Added Successfully...", parent=dashwin)
            con.commit()
            idval.set("")
            titleval.set("")
            authorval.set("")
            editionval.set("")
            priceval.set("")
def addbookResetbtnfunc():
    idval.set("")
    titleval.set("")
    authorval.set("")
    editionval.set("")
    priceval.set("")
addbooksubmitbtn = Button(miniaddbookframe, text="Submit", bg='#092042', fg='white',  activebackground='#095070', bd =0,
                         height=12,
                          activeforeground='white' ,relief=FLAT
                          , width=12, font=("Arial", 18, "bold"), command=addbooksubmitbtnfunc)
addbooksubmitbtn.place(x=310, y=320)
addbookResetbtn = Button(miniaddbookframe, text="Reset", bg='#092042', fg='white',  activebackground='#095070', bd=0,
                         height=12,
                          activeforeground='white',relief=FLAT
                          , width=12, font=("Arial", 18, "bold"), command=addbookResetbtnfunc)
addbookResetbtn.place(x=430, y=320)



















# ==============================================================================================================================================
# =================================================================== Issue Book ===============================================================
issuebookframe = Frame(dashwin, bg="black", relief='flat', bd=0)
issuebookframe.place(x=0, y=0, relwidth=1, relheight=1)
Label(issuebookframe, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
def issuebookbackbtnFun():
    studentidEntry['state'] = 'normal'
    studentidEntry.delete(0, 'end')
    stdnameLabelVal.configure(text='')
    stdcourseLabelVal.configure(text='')
    stdcontactLabelVal.configure(text='')
    stdcollegeLabelVal.configure(text='')
    for child in issuebookminiframe3.winfo_children():
        child.configure(state='disable')
    BookidLabelEntry.delete(0,'end')
    for child in issuebookminiframe2.winfo_children():
        child.configure(state='disable')
    issuebookminiframe3_title1.configure(state='normal')
    issuebookminiframe2_title1.configure(state='normal')
    dashboardframe.tkraise()
Button(issuebookframe, bd=0, image=back,
                        command=issuebookbackbtnFun ,bg= '#092042', activebackground='#1857b5').place(x=10, y=10)
miniissuebookframe1 = Frame(issuebookframe, bg='#D1DEE4',relief = 'flat' ,bd = 4)
miniissuebookframe1.place(x=120, y=20, width=400, height=300)
issuebookminiframe3 = Frame(issuebookframe, bg='#d1dee4', relief='flat', bd=0)
issuebookminiframe3.place(x=540, y=20, width=400, height=300)
issuebookminiframe2 = Frame(issuebookframe, bg='#d1dee4', relief='flat', bd=0)
issuebookminiframe2.place(x=975, y=20, width=500, height=300)
issuebookframe_title1 = Label(miniissuebookframe1, text="Student Info", bg="#092042",relief='flat',bd =0,
                              font=("Arial", 15, "bold"),
                              foreground='white', width=30, height=2)
issuebookframe_title1.place(x=13, y=15)
studentidLabel = Label(miniissuebookframe1, text="Student Id :" , bg='#d1dee4', font=("Arial", 15, "bold"))
studentidLabel.place(x=20, y=92)
studentidval = StringVar()
studentidEntry = Entry(miniissuebookframe1, textvariable=studentidval, bg='#dbe9ff', font=("Arial", 14), bd=0,
                       relief=FLAT, width=20 ,state = 'normal')
studentidEntry.place(x=140, y=90)
def issuebooksubmitbtnfunc1():
    if studentidval == "":
        messagebox.showinfo("Information" ,"Student Id cannot Be Empty  !!!",parent = dashwin)
    else:
        query = 'SELECT * FROM student_data WHERE roll_no=%s;'
        result = mycursor.execute(query,(studentidval.get()))
        if result == True:
            for child in issuebookminiframe3.winfo_children():
                child.configure(state='normal')
            query = "SELECT * FROM student_data WHERE roll_no=%s;"
            r = mycursor.execute(query, (studentidval.get()))
            data = mycursor.fetchall()
            for i in data:
                stdnameLabelVal.configure(text = i[1])
                stdcourseLabelVal.configure(text = i[2])
                stdcontactLabelVal.configure(text =i[3])
                stdcollegeLabelVal.configure(text =i[4])
            for child in issuebookminiframe2.winfo_children():
                child.configure(state='normal')
            studentidEntry['state'] = 'disable'
        else:
            messagebox.showwarning("Warning", "Student Id Doesn't Exist !!!", parent=dashwin)
issuebooksubmitbtn1 = Button(miniissuebookframe1, text="Submit", bg='#092042', fg='white',  activebackground='#095070',bd=0,
                             activeforeground='white',relief = 'raised'
                             , width=8, font=("Arial", 14, "bold"), command=issuebooksubmitbtnfunc1)
issuebooksubmitbtn1.place(x=155, y=145)
issuebookminiframe3_title1 = Label(issuebookminiframe3, text="Student Information", bg="#092042", relief='flat',
                                   bd=0,
                                   font=("Arial", 15, "bold"),
                                   foreground='white', width=30, height=2)
issuebookminiframe3_title1.place(x=13, y=15)
stdnameLabel = Label(issuebookminiframe3, text="Name     : ", font=("Arial", 15, "bold"), bg='#d1dee4')
stdnameLabel.place(x=20, y=80)
stdnameLabelVal = Label(issuebookminiframe3, text=" ", bg='#d1dee4',fg = '#092042', font=("Arial", 12 ,''),)
stdnameLabelVal.place(x=130, y=80)
stdcourseLabel = Label(issuebookminiframe3, text="Branch  : ", font=("Arial", 15, "bold"), bg='#d1dee4')
stdcourseLabel.place(x=20, y=110)
stdcourseLabelVal = Label(issuebookminiframe3, text=" ", bg='#d1dee4',fg = '#092042', font=("Arial", 12,''), )
stdcourseLabelVal.place(x=130, y=110)
stdcontactLabel = Label(issuebookminiframe3, text="Contact : ", font=("Arial", 15, "bold"), bg='#d1dee4')
stdcontactLabel.place(x=20, y=140)
stdcontactLabelVal = Label(issuebookminiframe3, text=" ", bg='#d1dee4',fg = '#092042', font=("Arial", 12 ,''), )
stdcontactLabelVal.place(x=130, y=140)
stdcollegeLabel = Label(issuebookminiframe3, text="College : ", font=("Arial", 15, "bold"), bg='#d1dee4')
stdcollegeLabel.place(x=20, y=170)
stdcollegeLabelVal = Label(issuebookminiframe3, text=" ", bg='#d1dee4',fg = '#092042', font=("Arial", 12 ,''), )
stdcollegeLabelVal.place(x=130, y=170)
for child in issuebookminiframe3.winfo_children():
    child.configure(state='disable')
issuedbooktitle1 = StringVar()
issuedbookauthor1 = StringVar()
issuedbookedition1 = StringVar()
issuedbooktitle2 = StringVar()
issuedbookauthor2 = StringVar()
issuedbookedition2 = StringVar()
issuedbooktitle3 = StringVar()
issuedbookauthor3 = StringVar()
issuedbookedition3 = StringVar()
to_dateval = StringVar()
issuebookminiframe2_title1 = Label(issuebookminiframe2, text="Book to Issue",foreground='#ffffff', background="#092042", relief='flat',
                                   bd=0,
                                   font=("Arial", 15, "bold"),
                                   width=38, height=2)
issuebookminiframe2_title1.place(x=13, y=15)
BookidLabelLabel = Label(issuebookminiframe2, text="Book Id : ", bg='#d1dee4', font=("Arial", 15, "bold"))
BookidLabelLabel.place(x=70, y=85)
Bookidval = StringVar()
BookidLabelEntry = Entry(issuebookminiframe2, textvariable=Bookidval, bg='#dbe9ff', font=("Arial", 14), bd=0,
                         relief=FLAT, width=20)
BookidLabelEntry.place(x=180, y=85)
def issuebooksubmitbtnfunc2():
    if (Bookidval.get() == ""):
        messagebox.showerror("Error", "Book Id is requi#095070!!!", parent=dashwin)
    else:
        query = "select issue_status from storebook where bookid=%s;"
        r = mycursor.execute(query, (Bookidval.get()))
        if r == True:
            data = mycursor.fetchall()
            for i in data:
                if i[0] == "Issued":
                    messagebox.showinfo("Info", "This book already issued\nTry another one...!!!", parent=dashwin)
                else:
                    query = "select title,author,edition from storebook where issued_to=%s"
                    mycursor.execute(query,studentidval.get())
                    data = mycursor.fetchall()
                    case = True
                    for i in data:
                        if (issuedbooktitle1.get() == ""):
                            issuedbooktitle1.set(i[0])
                            issuedbookauthor1.set(i[1])
                            issuedbookedition1.set(i[2])
                        elif (issuedbooktitle2.get() == ""):
                            issuedbooktitle2.set(i[0])
                            issuedbookauthor2.set(i[1])
                            issuedbookedition2.set(i[2])
                        elif (issuedbooktitle3.get() == ""):
                            issuedbooktitle3.set(i[0])
                            issuedbookauthor3.set(i[1])
                            issuedbookedition3.set(i[2])
                        else:
                            messagebox.showinfo("Info", "Maximum 3 books can be taken!!!", parent=dashwin)
                            studentidval.set("")
                            stdnameLabelVal.configure(text = '')
                            stdcourseLabelVal.configure(text = '')
                            stdcontactLabelVal.configure(text = '')
                            stdcollegeLabelVal.configure(text = '')
                            Bookidval.set("")
                            issuedbooktitle1.set("")
                            issuedbookauthor1.set("")
                            issuedbookedition1.set("")
                            issuedbooktitle2.set("")
                            issuedbookauthor2.set("")
                            issuedbookedition2.set("")
                            issuedbooktitle3.set("")
                            issuedbookauthor3.set("")
                            issuedbookedition3.set("")
                            to_dateval.set("")
                            case = False
                    query = "select title,author,edition from storebook where bookid=%s"
                    mycursor.execute(query, (Bookidval.get()))
                    data = mycursor.fetchall()
                    for i in data:
                        if (issuedbooktitle1.get() == ""):
                            issuedbooktitle1.set(i[0])
                            issuedbookauthor1.set(i[1])
                            issuedbookedition1.set(i[2])
                        elif (issuedbooktitle2.get() == ""):
                            issuedbooktitle2.set(i[0])
                            issuedbookauthor2.set(i[1])
                            issuedbookedition2.set(i[2])
                        elif (issuedbooktitle3.get() == ""):
                            issuedbooktitle3.set(i[0])
                            issuedbookauthor3.set(i[1])
                            issuedbookedition3.set(i[2])
                        else:
                            messagebox.showinfo("Info", "Maximum 3 books can be taken!!!", parent=dashwin)
                            studentidval.set("")
                            stdnameLabelVal.configure(text='')
                            stdcourseLabelVal.configure(text='')
                            stdcontactLabelVal.configure(text='')
                            stdcollegeLabelVal.configure(text='')
                            Bookidval.set("")
                            issuedbooktitle1.set("")
                            issuedbookauthor1.set("")
                            issuedbookedition1.set("")
                            issuedbooktitle2.set("")
                            issuedbookauthor2.set("")
                            issuedbookedition2.set("")
                            issuedbooktitle3.set("")
                            issuedbookauthor3.set("")
                            issuedbookedition3.set("")
                            to_dateval.set("")
                            case = False
                    if case == True :
                        issuebooksroot = CTkToplevel(dashwin)
                        frame = CTkFrame(issuebooksroot, fg_color="#092042") 
                        frame.pack(fill="both", expand=True)
                        issuebooksroot.geometry("600x500+500+100")
                        issuebooksroot.iconbitmap("assets/icon.ico")
                        issuebooksroot.resizable(False, False)
                        issuebooksroot.title("Issue Books")
                        issuebooksroot.grab_set()
                        def on_close():
                            issuedbooktitle1.set("")
                            issuedbookauthor1.set("")
                            issuedbookedition1.set("")
                            issuedbooktitle2.set("")
                            issuedbookauthor2.set("")
                            issuedbookedition2.set("")
                            issuedbooktitle3.set("")
                            issuedbookauthor3.set("")
                            issuedbookedition3.set("")
                            issuebooksroot.destroy()
                        issuebooksroot.protocol('WM_DELETE_WINDOW',on_close)
                        Label(issuebooksroot, text="Title : ", bg="#092042", fg='white',
                                             font=("Arial", 14, "bold")).place(x=20, y=20)
                        Label(issuebooksroot, textvariable=issuedbooktitle1, bg="#092042", fg='white',
                                                font=("Arial", 14, '')).place(x=100, y=20)
                        Label(issuebooksroot, text="Author : ", bg="#092042", fg='white',
                                              font=("Arial", 14, "bold")).place(x=20, y=40)
                        Label(issuebooksroot, textvariable=issuedbookauthor1, bg="#092042", fg='white',
                                                 font=("Arial", 14, '')).place(x=100, y=40)
                        Label(issuebooksroot, text="Edition : ", bg="#092042", fg='white',
                                               font=("Arial", 14, "bold")).place(x=20, y=60)
                        Label(issuebooksroot, textvariable=issuedbookedition1, bg="#092042", fg='white',
                                                  font=("Arial", 14, '')).place(x=100, y=60)
                        dashLabel1 = Label(issuebooksroot,
                                           text=".....................................................................................", fg='white',
                                           bg="#092042")
                        dashLabel1.place(x=20, y=90)
                        Label(issuebooksroot, text="Title : ", bg="#092042", fg='white',
                                             font=("Arial", 14, "bold")).place(x=20, y=120)
                        Label(issuebooksroot, textvariable=issuedbooktitle2, bg="#092042", fg='white',
                                                font=("Arial", 14, '')).place(x=100, y=120)
                        Label(issuebooksroot, text="Author : ", bg="#092042", fg='white',
                                              font=("Arial", 14, "bold")).place(x=20, y=140)
                        Label(issuebooksroot, textvariable=issuedbookauthor2, bg="#092042", fg='white',
                                                 font=("Arial", 14, '')).place(x=100, y=140)
                        Label(issuebooksroot, text="Edition : ", bg="#092042", fg='white',
                                               font=("Arial", 14, "bold")).place(x=20, y=160)
                        Label(issuebooksroot, textvariable=issuedbookedition2, bg="#092042", fg='white',
                                                  font=("Arial", 14, '')).place(x=100, y=160)
                        dashLabel2 = Label(issuebooksroot,
                                           text=".....................................................................................", fg='white',
                                           bg="#092042")
                        dashLabel2.place(x=20, y=190)
                        Label(issuebooksroot, text="Title : ", bg="#092042", fg='white',
                                             font=("Arial", 14, "bold")).place(x=20, y=220)
                        Label(issuebooksroot, textvariable=issuedbooktitle3, bg="#092042", fg='white',
                                                font=("Arial", 14)).place(x=100, y=220)
                        Label(issuebooksroot, text="Author : ", bg="#092042", fg='white',
                                              font=("Arial", 14, "bold")).place(x=20, y=240)
                        Label(issuebooksroot, textvariable=issuedbookauthor3, bg="#092042", fg='white',
                                                 font=("Arial", 14)).place(x=100, y=240)
                        Label(issuebooksroot, text="Edition : ", bg="#092042", fg='white',
                                               font=("Arial", 14, "bold")).place(x=20, y=260)
                        Label(issuebooksroot, textvariable=issuedbookedition3, bg="#092042", fg='white',
                                                  font=("Arial", 14)).place(x=100, y=260)
                        dashLabel3 = Label(issuebooksroot, fg='white',
                                           text=".....................................................................................",
                                           bg="#092042")
                        dashLabel3.place(x=20, y=290)
                        cal = Calendar(issuebooksroot, selectmode='day', year=2025,  font=("Arial", 15), month=1, day=22)
                        cal.place(x=330, y=20)
                        dateLabel = Label(issuebooksroot,
                                          text="Date : ",fg='white',
                                          bg="#092042", font=("Arial", 15 , 'bold'))
                        dateLabel.place(x=20, y=340)
                        dateLabelval = Label(issuebooksroot,
                                          text="",
                                          bg="#092042", fg='white', font=("Arial", 14))
                        dateLabelval.place(x=200, y=340)
                        def issuedbtnfunc():
                            if (to_dateval.get() == ""):
                                messagebox.showinfo("Info", "Confirm last date!!!", parent=dashwin)
                            else:
                                from_date = time.strftime("%y-%m-%d")
                                query = "insert into bookissued_data(roll_no,from_date,to_date,bookid) values(%s,%s,%s,%s);"
                                r = mycursor.execute(query, (
                                    studentidval.get(), from_date, to_dateval.get(), Bookidval.get()))
                                query = "update storebook set issue_status=%s,issued_to=%s where bookid=%s;"
                                mycursor.execute(query, ("Issued", studentidval.get(), Bookidval.get()))
                                messagebox.showinfo("Notification","Book Issued Successfully...",
                                                    parent=issuebooksroot)
                                issuedbooktitle1.set("")
                                issuedbookauthor1.set("")
                                issuedbookedition1.set("")
                                issuedbooktitle2.set("")
                                issuedbookauthor2.set("")
                                issuedbookedition2.set("")
                                issuedbooktitle3.set("")
                                issuedbookauthor3.set("")
                                issuedbookedition3.set("")
                                to_dateval.set('')
                                issuebooksroot.destroy()
                        def grab_date():
                            date = cal.get_date()
                            date = date.split('/')
                            date[0], date[1], date[2] = date[2], date[0], date[1]
                            s = '-'
                            date = s.join(date)
                            to_dateval.set(date)
                            date = date.split('-')
                            date[0], date[1], date[2] = date[2], date[1], date[0]
                            ldate = '/'.join(date)
                            dateLabelval['text'] = ldate
                        confirmdatebtn = Button(issuebooksroot, text="Confirm Date", font=("Arial", 14 ,'bold'),
                                                command=grab_date, bg="#095070", fg='white', bd=0)
                        confirmdatebtn.place(x=20, y=400)
                        issuedbtn = Button(issuebooksroot, text="Issue", font=("Arial", 14,'bold'),
                                           command=issuedbtnfunc,
                                           bg="#095070", fg='white', bd=0,width=12)
                        issuedbtn.place(x=20, y=470)
        else:
            messagebox.showinfo("INFORMATION", "No Book Available with Such ID", parent=dashwin)
            Bookidval.set('')
def issuebookAddMorebtn():
    studentidEntry['state'] = 'normal'
    studentidEntry.delete(0, 'end')
    stdnameLabelVal.configure(text='')
    stdcourseLabelVal.configure(text='')
    stdcontactLabelVal.configure(text='')
    stdcollegeLabelVal.configure(text='')
    for child in issuebookminiframe3.winfo_children():
        child.configure(state='disable')
    BookidLabelEntry.delete(0, 'end')
    for child in issuebookminiframe2.winfo_children():
        child.configure(state='disable')
    issuebookminiframe3_title1.configure(state='normal')
    issuebookminiframe2_title1.configure(state='normal')
issuebooksubmitbtn2 = Button(issuebookminiframe2, text="Issue", bg='#092042', foreground='#ffffff',  activebackground='#095070',
                             bd=0,
                             activeforeground='#fff', relief='flat'
                             , width=12, font=("Arial", 14, "bold"), command=issuebooksubmitbtnfunc2)
issuebooksubmitbtn2.place(x = 70, y=160)
issuebookAddMorebtn1 = Button(issuebookminiframe2, text="Add More Book", bg='#092042', fg='white',  activebackground='#095070',
                             bd=0,
                             activeforeground='white', relief='flat'
                             , width=15, font=("Arial", 14, 'bold'), command=issuebookAddMorebtn)
issuebookAddMorebtn1.place(x=240, y=160)
for child in issuebookminiframe2.winfo_children():
    child.configure(state='disable')
issuebookminiframe3_title1.configure(state='normal')
issuebookminiframe2_title1.configure(state='normal')

   















# =================================================================================================================================================
# ============================================================== Edit Book Frame ===================================================================
editBookframe = Frame(dashwin, bg="#d1dbeb", relief='flat', bd=0)
editBookframe.place(x=0,y=0,relwidth = 1, relheight=1)
Label(editBookframe, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
Button(editBookframe, bd=0, image=back,command=lambda: dashboardframe.tkraise(),bg='#092042', activebackground='#1857b5').place(x=10, y=10)

miniEditbookframe = Frame(editBookframe, bg='#d1dbeb', height =300, width=600, relief='flat', bd=0)
miniEditbookframe.place(x=100, y=20)
editBookframe_title = Label(miniEditbookframe, text="EDIT BOOK", bg="#092042", font=("Arial", 15, "bold"),
                           relief='flat', fg='white', width=41, height=2)
editBookframe_title.place(x=20, y=10)
editBookidLabel = Label(miniEditbookframe, text="Book ID :", font=("Arial", 15, "bold"), bg='#d1dbeb')
editBookidLabel.place(x=160, y=97)
editBookidval = StringVar()
editBookidEntry = Entry(miniEditbookframe, textvariable=editBookidval , font=("Arial", 14), bd=0, relief=FLAT,
                width=15)
editBookidEntry.place(x=270, y=95)
def editBooksubmitbtnfun():
    if editBookidval.get() == '':
        messagebox.showinfo("INFORMATION","Book ID cannot be Empty !!!" ,parent = dashwin )
    else:
        query = "select title ,author, edition, price from storebook where bookid  = %s;"
        r = mycursor.execute(query,(editBookidval.get()))
        if r == True:
            data = mycursor.fetchall()
            for i in data:
                editBooktitleval.set(i[0])
                editBookauthorval.set(i[1])
                editBookeditionval.set(i[2])
                editBookpriceval.set(i[3])
            miniEditbookframe.place_forget()
            miniEditbookframe2.place(x=100, y=10)
            editBookidEntry2.configure(state = 'disable')
        else:
            messagebox.showinfo("INFORMATION", "No Book There With Such ID !!!", parent=dashwin)
editBookbooksubmitbtn = Button(miniEditbookframe, text="Submit", bg='#092042', fg='white',  activebackground='#095070', bd=0,
                          activeforeground='white'
                          , width=12, font=("Arial", 15, "bold"), command=editBooksubmitbtnfun)
editBookbooksubmitbtn.place(x=160, y=160)

miniEditbookframe2 = Frame(editBookframe, bg='#d1dbeb', height=500, width=600, relief='flat', bd=0)
miniEditbookframe2.place_forget()
editBookframe_title2 = Label(miniEditbookframe2, text="EDIT BOOK", bg="#092042", font=("Arial", 15, "bold"),
                            relief='flat', fg='white', width=41, height=2)
editBookframe_title2.place(x=20, y=10)
editBookidLabel2 = Label(miniEditbookframe2, text="Book ID :", font=("Arial", 15, "bold"), bg='#d1dbeb')
editBookidLabel2.place(x=80, y=90)
editBookidEntry2 = Entry(miniEditbookframe2, textvariable=editBookidval, bg='#dbe9ff', font=("Arial", 14), bd=0,
                        relief=FLAT,
                        width=15)
editBookidEntry2.place(x=190, y=90)
editBooktitleLabel = Label(miniEditbookframe2, text="TITLE :", font=("Arial", 15, "bold"), bg='#d1dbeb')
editBooktitleLabel.place(x=80, y=142)
editBooktitleval = StringVar()
editBooktitleEntry = Entry(miniEditbookframe2, textvariable=editBooktitleval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,
                   width=30)
editBooktitleEntry.place(x=190, y=140)
editBookauthorLabel = Label(miniEditbookframe2, text="Author", font=("Arial", 15, "bold"), bg='#d1dbeb')
editBookauthorLabel.place(x=80, y=192)
editBookauthorval = StringVar()
editBookauthorEntry = Entry(miniEditbookframe2, textvariable=editBookauthorval, bg='#dbe9ff', font=("Arial", 14), bd=0,
                    relief=FLAT,
                    width=30)
editBookauthorEntry.place(x=190, y=190)
editBookeditionLabel = Label(miniEditbookframe2, text="Edition", font=("Arial", 15, "bold"), bg='#d1dbeb')
editBookeditionLabel.place(x=80, y=242)
editBookeditionval = StringVar()
editBookeditionEntry = Entry(miniEditbookframe2, textvariable=editBookeditionval, bg='#dbe9ff', font=("Arial", 14), bd=0,
                     relief=FLAT, width=30)
editBookeditionEntry.place(x=190, y=240)
editBookpriceLabel = Label(miniEditbookframe2, text="Price", font=("Arial", 15, "bold"), bg='#d1dbeb')
editBookpriceLabel.place(x=80, y=292)
editBookpriceval = StringVar()
editBookpriceEntry = Entry(miniEditbookframe2, textvariable=editBookpriceval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,
                   width=15)
editBookpriceEntry.place(x=190, y=290)
def editBooksavebtnfun():
    if editBooktitleval.get() == '' or editBookauthorval.get() == '' or editBookeditionval.get() == '' or editBookpriceval.get() == '':
        messagebox.showinfo("INFORMATION", "Any Field Cannot be Empty !!!", parent=dashwin)
    else:
        query = 'UPDATE storebook SET title = %s , author = %s ,edition = %s , price = %s WHERE bookid = %s'
        res = mycursor.execute(query , (editBooktitleval.get() ,editBookauthorval.get() ,editBookeditionval.get() ,editBookpriceval.get(),editBookidval.get()))
        if res == True:
            messagebox.showinfo("INFORMATION", "Book Successfully Updated !!!", parent=dashwin)
            editBooktitleval.set('')
            editBookauthorval.set('')
            editBookeditionval.set('')
            editBookpriceval.set('')
            editBookidval.set('')
            miniEditbookframe2.place_forget()
            miniEditbookframe.place(x=100, y=20)
        else:
            messagebox.showerror("ERROR", "Book Failed To Updated !!!", parent=dashwin)
            editBooktitleval.set('')
            editBookauthorval.set('')
            editBookeditionval.set('')
            editBookpriceval.set('')
            editBookidval.set('')
            miniEditbookframe2.place_forget()
            miniEditbookframe.place(x=100, y=20)
editBookbooksavebtn = Button(miniEditbookframe2, text="SAVE", bg='#092042', fg='white',  activebackground='#095070',
                               bd=0,
                               activeforeground='white'
                               , width=8, font=("Arial", 15, "bold"), command=editBooksavebtnfun)
editBookbooksavebtn.place(x=310, y=340)









# ==============================================================================================================================================
# =================================================================== Return Book ===============================================================
ReturnBookframe = Frame(dashwin, bg="#D1DEE4", relief='flat', bd=0)
ReturnBookframe.place(x=0, y=0, relwidth=1,relheight=1)
Label(ReturnBookframe, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
Button(ReturnBookframe, bd=0, font=("Arial", 15, "bold"), image=back,
                         command=lambda: dashboardframe.tkraise(),bg ='#092042', activebackground='#1857b5').place(x=10, y=10)



miniReturnbookframe = Frame(ReturnBookframe, bg='#D1DEE4', height=200, width=600, relief='flat', bd=0)
miniReturnbookframe.place(x=100, y=20)
ReturnBookframe_title = Label(miniReturnbookframe, text="RETURN BOOK", bg="#092042", font=("Arial", 15, "bold"),
                              relief='flat', fg='white', width=47, height=2)
ReturnBookframe_title.place(x=20, y=10)
ReturnBookidLabel = Label(miniReturnbookframe, text="Book ID :", font=("Arial", 15, "bold"), bg='#D1DEE4')
ReturnBookidLabel.place(x=150, y=92)
ReturnBookidEntryval = StringVar()
ReturnBookidEntry = Entry(miniReturnbookframe, textvariable = ReturnBookidEntryval, font=("Arial", 14),
                          bd=0,
                          relief=FLAT,
                          width=20)
ReturnBookidEntry.place(x=270, y=90)
def ReturnBooksubmitbtnfun():
    if ReturnBookidEntryval.get() == '':
        messagebox.showinfo("INFORMATION","Book ID cannot be Empty !!!" ,parent = dashwin )
    else:
        query = "select * from storebook where bookid  = %s;"
        r = mycursor.execute(query,(ReturnBookidEntryval.get()))
        if r == True:
            query = 'select to_date from bookissued_data where bookid =%s'
            chk = mycursor.execute(query, (ReturnBookidEntryval.get()))
            if chk == True:
                data = mycursor.fetchall()
                for i in data:
                    to_date = i[0]
                today_date = time.strftime("%y-%m-%d")
                query = "select datediff(%s,%s);"
                mycursor.execute(query, (str(today_date), str(to_date)))
                dif = mycursor.fetchall()
                for j in dif:
                    difren = j[0]
                if (difren <= 0):
                    query = "update storebook set issue_status=NULL,issued_to=NULL where bookid=%s"
                    r = mycursor.execute(query, (ReturnBookidEntryval.get()))
                    if r == True:
                        query = "delete from bookissued_data where bookid=%s"
                        r = mycursor.execute(query, (ReturnBookidEntryval.get()))
                        con.commit()
                        if r == True:
                            messagebox.showinfo("INFORMATION", 'Book Status SuccessFull Updated...', parent=dashwin)
                            ReturnBookidEntryval.set('')
                else:
                    fineroot = CTkToplevel()
                    fineroot.title('Late Fine')
                    fineroot.geometry('300x260')
                    fineroot.resizable(False, False)
                    fineframe = Frame(fineroot, bd=0, relief='flat', bg='#d1dbeb')
                    fineframe.place(x=0, y=0, relwidth=1, relheight=1)
                    Duedatelabel = Label(fineframe, font=("Arial", 15, "bold"), bg='#d1dbeb',
                                         text='Due Date : ')
                    Duedatelabel.place(x=20, y=20)
                    d = str(to_date).split('-')
                    d[0], d[1], d[2] = d[2], d[1], d[0]
                    d = '-'.join(d)
                    Duedatelabelval = Label(fineframe, font=("Arial", 15, "bold"), bg='#d1dbeb', text=d,
                                            fg='#095070')
                    Duedatelabelval.place(x=140, y=20)
                    Todaydatelabel = Label(fineframe, font=("Arial", 15, "bold"), bg='#d1dbeb',
                                           text='Today Date : ')
                    Todaydatelabel.place(x=20, y=70)
                    Todaydatelabelval = Label(fineframe, font=("Arial", 15, "bold"), bg='#d1dbeb',
                                              text=time.strftime("%d-%m-%y"), fg='#095070')
                    Todaydatelabelval.place(x=140, y=70)
                    finedatelabel = Label(fineframe, font=("Arial", 15, "bold"), bg='#d1dbeb',
                                          text='Late Fine : ')
                    finedatelabel.place(x=20, y=120)
                    fin = difren * 2
                    finedatelabelval = Label(fineframe, font=("Arial", 15, "bold"), bg='#d1dbeb', text=fin,
                                             fg='#095070')
                    finedatelabelval.place(x=140, y=120)
                    def FinePaidfun():
                        query = "update storebook set issue_status=NULL,issued_to=NULL where bookid=%s;"
                        r = mycursor.execute(query, (ReturnBookidEntryval.get()))
                        if r == True:
                            query = "delete from bookissued_data where bookid=%s;"
                            r = mycursor.execute(query, (ReturnBookidEntryval.get()))
                            if r == True:
                                con.commit()
                                fineroot.destroy()
                                messagebox.showinfo("INFORMATION", 'Book Status SuccessFull Updated...',
                                                    parent=dashwin)
                                ReturnBookidEntryval.set('')
                    finebutton = Button(fineframe, text='Paid', font=("Arial", 15, "bold"), bd=0, bg='#092042',
                                        fg='white',
                                        command=FinePaidfun)
                    finebutton.place(x=150, y=190)
            else:
                messagebox.showinfo("INFORMATION", "These Book is Not Issued Yet... !!!", parent=dashwin)
                ReturnBookidEntry.delete(0,'end')
        else:
            messagebox.showinfo("INFORMATION", "No Book There With Such ID !!!", parent=dashwin)
            ReturnBookidEntry.delete(0, 'end')
ReturnBookbooksubmitbtn = Button(miniReturnbookframe, text="Submit", bg='#092042', fg='white',  activebackground='#095070', bd=0,
                          activeforeground='white'
                          , width=8, font=("Arial", 15, "bold"), command=ReturnBooksubmitbtnfun)
ReturnBookbooksubmitbtn.place(x=310, y=140)
















# ==============================================================================================================================================
# =================================================================== Delete Book ===============================================================
deleteBookframe = Frame(dashwin, bg="#D1DEE4", relief='flat', bd=0)
deleteBookframe.place(x=0, y=0, relwidth=1,relheight=1)
Label(deleteBookframe, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
Button(deleteBookframe, bd=0, font=("Arial", 15, "bold"), image=back,
                         command=lambda: dashboardframe.tkraise(),bg='#092042', activebackground='#092042').place(x=10, y=10)
miniDeletebookframe = Frame(deleteBookframe, bg='#D1DEE4', height=200, width=600, relief='flat', bd=0)
miniDeletebookframe.place(x=100, y=20)

deleteBookframe_title = Label(miniDeletebookframe, text="DELETE BOOK", bg="#092042", font=("Arial", 15, "bold"),
                            relief='flat', fg='white', width=47, height=2)
deleteBookframe_title.place(x=10, y=10)
deleteBookidLabel = Label(miniDeletebookframe, text="Book ID :", font=("Arial", 15, "bold"), bg='#D1DEE4')
deleteBookidLabel.place(x=150, y=92)
deleteBookidEntryval = StringVar()
deleteBookidEntry = Entry(miniDeletebookframe, textvariable=deleteBookidEntryval, font=("Arial", 14), bd=0,
                        relief=FLAT,
                        width=15)
deleteBookidEntry.place(x=270, y=90)
def deleteBooksubmitbtnfun():
    if deleteBookidEntryval.get() == '':
        messagebox.showinfo("INFORMATION","Book ID cannot be Empty !!!" ,parent = dashwin )
    else:
        query = "select title ,author, edition, price from storebook where bookid  = %s;"
        r = mycursor.execute(query,(deleteBookidEntryval.get()))
        if r == True:
            data = mycursor.fetchall()
            for i in data:
                pass
                deleteBooktitleval.set(i[0])
                deleteBookauthorval.set(i[1])
                deleteBookeditionval.set(i[2])
                deleteBookpriceval.set(i[3])
            miniDeletebookframe.place_forget()
            miniDeletebookframe2.place(x=100, y=20)
            deleteBookidEntry2.configure(state = 'disable')
            deleteBooktitleEntry.configure(state = 'disable')
            deleteBookauthorEntry.configure(state = 'disable')
            deleteBookeditionEntry.configure(state = 'disable')
            deleteBookpriceEntry.configure(state = 'disable')
        else:
            messagebox.showinfo("INFORMATION", "No Book There With Such ID !!!", parent=dashwin)
deleteBookbooksubmitbtn = Button(miniDeletebookframe, text="Submit", bg='#092042', fg='white',  activebackground='#095070', bd=0,
                          activeforeground='white'
                          , width=8, font=("Arial", 15, "bold"), command=deleteBooksubmitbtnfun)
deleteBookbooksubmitbtn.place(x=310, y=140)
miniDeletebookframe2 = Frame(deleteBookframe, bg='#D1DEE4', height=450, width=600, relief='flat', bd=0)
miniDeletebookframe2.place_forget()
deleteBookframe_title2 = Label(miniDeletebookframe2, text="DELETE BOOK", bg="#092042", font=("Arial", 15, "bold"),
                               relief='flat', fg='white', width=47, height=2)
deleteBookframe_title2.place(x=10, y=10)
deleteBookidLabel2 = Label(miniDeletebookframe2, text="Book ID :", font=("Arial", 15, "bold"), bg='#D1DEE4')
deleteBookidLabel2.place(x=80, y=82)
deleteBookidEntry2 = Entry(miniDeletebookframe2, textvariable=deleteBookidEntryval, bg='#dbe9ff', font=("Arial", 14), bd=0,
                         relief=FLAT,
                         width=15)
deleteBookidEntry2.place(x=190, y=80)
deleteBooktitleLabel = Label(miniDeletebookframe2, text="TITLE :", font=("Arial", 15, "bold"), bg='#D1DEE4')
deleteBooktitleLabel.place(x=80, y=132)
deleteBooktitleval = StringVar()
deleteBooktitleEntry = Entry(miniDeletebookframe2, textvariable=deleteBooktitleval, bg='#dbe9ff', font=("Arial", 14),
                           bd=0, relief=FLAT,
                           width=30)
deleteBooktitleEntry.place(x=190, y=130)
deleteBookauthorLabel = Label(miniDeletebookframe2, text="Author", font=("Arial", 15, "bold"), bg='#D1DEE4')
deleteBookauthorLabel.place(x=80, y=182)
deleteBookauthorval = StringVar()
deleteBookauthorEntry = Entry(miniDeletebookframe2, textvariable=deleteBookauthorval, bg='#dbe9ff', font=("Arial", 14),
                            bd=0,
                            relief=FLAT,
                            width=30)
deleteBookauthorEntry.place(x=190, y=180)
deleteBookeditionLabel = Label(miniDeletebookframe2, text="Edition", font=("Arial", 15, "bold"), bg='#D1DEE4')
deleteBookeditionLabel.place(x=80, y=232)
deleteBookeditionval = StringVar()
deleteBookeditionEntry = Entry(miniDeletebookframe2, textvariable=deleteBookeditionval, bg='#dbe9ff', font=("Arial", 14),
                             bd=0,
                             relief=FLAT, width=30)
deleteBookeditionEntry.place(x=190, y=230)
deleteBookpriceLabel = Label(miniDeletebookframe2, text="Price", font=("Arial", 15, "bold"), bg='#D1DEE4')
deleteBookpriceLabel.place(x=80, y=282)
deleteBookpriceval = StringVar()
deleteBookpriceEntry = Entry(miniDeletebookframe2, textvariable=deleteBookpriceval, bg='#dbe9ff', font=("Arial", 14),
                           bd=0, relief=FLAT,
                           width=15)
deleteBookpriceEntry.place(x=190, y=280)
def BookDeletebtnfun():
    delCon = messagebox.askyesno("CONFIRM","Do You Really Want To Delete These Book  !!!",parent = dashwin)
    if delCon == True :
        query = 'DELETE FROM storebook  WHERE bookid = %s'
        res = mycursor.execute(query, (deleteBookidEntryval.get()))
        if res == True:
            messagebox.showinfo("INFORMATION", "Book SuccessFully Deleted !!!", parent=dashwin)
            deleteBooktitleval.set('')
            deleteBookauthorval.set('')
            deleteBookeditionval.set('')
            deleteBookpriceval.set('')
            deleteBookidEntryval.set('')
            miniDeletebookframe2.place_forget()
            miniDeletebookframe.place(x=100, y=20)
        else:
            messagebox.showerror("ERROR", "Book Failed To Delete !!!", parent=dashwin)
            deleteBooktitleval.set('')
            deleteBookauthorval.set('')
            deleteBookeditionval.set('')
            deleteBookpriceval.set('')
            deleteBookidEntryval.set('')
            miniDeletebookframe2.place_forget()
            miniDeletebookframe.place(x=100, y=20)
def noDelete():
    deleteBooktitleval.set('')
    deleteBookauthorval.set('')
    deleteBookeditionval.set('')
    deleteBookpriceval.set('')
    deleteBookidEntryval.set('')
    miniDeletebookframe2.place_forget()
    miniDeletebookframe.place(x=100, y=20)
DeleteBookbookdeletebtn = Button(miniDeletebookframe2, text="DELETE", bg='#092042', fg='white',  activebackground='#095070',
                             bd=0,
                             activeforeground='white'
                             , width=8, font=("Arial", 15, "bold"), command = BookDeletebtnfun)
DeleteBookbookdeletebtn.place(x=80, y=360)
DeleteBookbookdeletebtn = Button(miniDeletebookframe2, text="Cancel", bg='#092042', fg='white',  activebackground='#095070',
                             bd=0,
                             activeforeground='white'
                             , width=8, font=("Arial", 15, "bold"), command = noDelete)
DeleteBookbookdeletebtn.place(x=200, y=360)











# ==============================================================================================================================================
# =================================================================== Show Book ===============================================================
def showAllBooks():
    showBookframe = Frame(dashwin, bg="#092042", relief='flat', bd=0)
    showBookframe.place(x=0, y=0, relwidth=1,relheight=1)
    ShowbookframeBgImg = Label(showBookframe, image=bg)
    ShowbookframeBgImg.place(x=0, y=0, relwidth=1, relheight=1)
    showbookbackbtn = Button(showBookframe, bd=0, font=("Arial", 15, "bold"), image=back,
                               command=lambda: dashboardframe.tkraise(),bg= '#092042', activebackground='#092042')
    showbookbackbtn.place(x=10, y=10)
    MinisearchbookFrame = Frame(showBookframe, width=800, height=60, bd=0, relief='flat', bg='#092042')
    MinisearchbookFrame.place(x=250, y=10)
    SearchBookidLabel = Label(MinisearchbookFrame, text="Book ID :", font=("Arial", 15, "bold"),foreground='white', bg='#092042')
    SearchBookidLabel.place(x=40, y=17)
    SearchBookidEntryval = StringVar()
    SearchBookidEntry = Entry(MinisearchbookFrame, textvariable=SearchBookidEntryval, bg='snow',
                              font=("Arial", 14), bd=0,
                              relief=FLAT,
                              width=40)
    SearchBookidEntry.place(x=150, y=15)
    def SecBooksubmitbtnfun():
        if SearchBookidEntryval.get() == '':
            query = 'SELECT bookid,title,author,edition,price, issue_status from storebook;'
            r= mycursor.execute(query)
            data = mycursor.fetchall()
            allBookinfoTable.delete(*allBookinfoTable.get_children())
            for i in data:
                    tabVal = [i[0], i[1], i[2], i[3], i[4], i[5]]
                    allBookinfoTable.insert('', END, values=tabVal)
        else:
            query = 'SELECT bookid,title,author,edition,price, issue_status FROM storebook WHERE bookid = %s ;'
            r = mycursor.execute(query, SearchBookidEntryval.get())
            if r == True:
                query = 'select bookid,title,author,edition,price,issue_status from storebook WHERE bookid = %s ;'
                mycursor.execute(query, SearchBookidEntryval.get())
                data = mycursor.fetchall()
                for i in data:
                    allBookinfoTable.delete(*allBookinfoTable.get_children())
                    tabVal = [i[0], i[1], i[2], i[3], i[4], i[5]]
                    allBookinfoTable.insert('', END, values=tabVal)
            else:
                messagebox.showinfo('INFORMATION', 'No Book Available With Such Book Id...', parent=dashwin)
    SearchBookbooksubmitbtn = Button(MinisearchbookFrame, text="Search", bg='#2b5eab', fg='white',
                                      activebackground='#1857b5',
                                     bd=0,
                                     activeforeground='white'
                                     , width=8, font=("Arial", 15, "bold"), command=SecBooksubmitbtnfun)
    SearchBookbooksubmitbtn.place(x=600, y= 10)
    MinishowbookFrame = Frame(showBookframe, width=850, height=10, bd=0, relief='flat',bg = '#092042')
    MinishowbookFrame.place(x=25, y=90)
    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview', font=('arial', 15, ''),fieldbackground = '#1b4585',borderwidth=0,rowheight=30,
                    background = '#092042',foreground='white', )
    style.configure('Treeview.Heading', font=('arial', 15, 'bold') ,padding=(0,10),foreground='white',activebackground='#095070', background='#092042',)
    style.map('Treeview',background = [('selected','#1857b5')])
    style.map("Treeview.Heading",
          background=[("active", "#1857b5")]) 
    
    Scroll_x = ttk.Scrollbar(MinishowbookFrame, orient=HORIZONTAL,style="Horizontal.TScrollbar")
    Scroll_y = ttk.Scrollbar(MinishowbookFrame, orient=VERTICAL  ,style="Vertical.TScrollbar")
    allBookinfoTable = ttk.Treeview(MinishowbookFrame, columns=('Book ID', 'Name', 'Author', 'Edition', 'Price', 'issue_status'),
                                xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set,)
    Scroll_x.pack(side=BOTTOM, fill=X ,anchor = W)
    Scroll_y.pack(side=RIGHT, fill=Y ,anchor = N)
    Scroll_x.configure(command=allBookinfoTable.xview)
    Scroll_y.configure(command=allBookinfoTable.yview)
    allBookinfoTable.column('Book ID', width=230, anchor=CENTER)
    allBookinfoTable.column('Name', width=280, anchor=CENTER)
    allBookinfoTable.column('Author', width=230, anchor=CENTER)
    allBookinfoTable.column('Edition', width=230, anchor=CENTER)
    allBookinfoTable.column('Price', width=230, anchor=CENTER)
    allBookinfoTable.column('issue_status', width=230, anchor=CENTER)
    allBookinfoTable.heading('Book ID', text='Book Id')
    allBookinfoTable.heading('Name', text='Name')
    allBookinfoTable.heading('Author', text='Author')
    allBookinfoTable.heading('Edition', text='Edition')
    allBookinfoTable.heading('Price', text='Price')
    allBookinfoTable.heading('issue_status', text='Issue Status')
    allBookinfoTable.configure(show='headings')

    allBookinfoTable.pack(fill='both')
    query = 'select bookid,title,author,edition,price, issue_status from storebook;'
    mycursor.execute(query)
    data = mycursor.fetchall()
    for i in data:
        tabVal = [i[0], i[1], i[2], i[3], i[4], i[5]]
        allBookinfoTable.insert('', END, values = tabVal)




# ==============================================================================================================================================
# =================================================================== Show Students ===============================================================
def showAllStudents():
    showStudentframe = Frame(dashwin, bg="#092042", relief='flat', bd=0)
    showStudentframe.place(x=0, y=0, relwidth=1,relheight=1)
    ShowStudentframeBgImg = Label(showStudentframe, image=bg)
    ShowStudentframeBgImg.place(x=0, y=0, relwidth=1, relheight=1)
    showbookbackbtn = Button(showStudentframe, bd=0, font=("Arial", 15, "bold"), image=back,
                               command=lambda: dashboardframe.tkraise(),bg= '#092042', activebackground='#092042')
    showbookbackbtn.place(x=10, y=10)
    MinisearchbookFrame = Frame(showStudentframe, width=800, height=60, bd=0, relief='flat', bg='#092042')
    MinisearchbookFrame.place(x=250, y=10)
    SearchBookidLabel = Label(MinisearchbookFrame, text="Student ID :", font=("Arial", 15, "bold"),foreground='white', bg='#092042')
    SearchBookidLabel.place(x=40, y=17)
    SearchBookidEntryval = StringVar()
    SearchBookidEntry = Entry(MinisearchbookFrame, textvariable=SearchBookidEntryval, bg='snow',
                              font=("Arial", 14), bd=0,
                              relief=FLAT,
                              width=40)
    SearchBookidEntry.place(x=165, y=15)
    def SecStudentsubmitbtnfun():
        if SearchBookidEntryval.get() == '':
            query = 'SELECT  roll_no,student_name,student_course,phone,college_name from storebook;'
            r= mycursor.execute(query)
            data = mycursor.fetchall()
            allStudentinfoTable.delete(*allStudentinfoTable.get_children())
            for i in data:
                    tabVal = [i[0], i[1], i[2], i[3], i[4], i[5]]
                    allStudentinfoTable.insert('', END, values=tabVal)
        else:
            query = 'SELECT roll_no,student_name,student_course,phone,college_name FROM student_data WHERE roll_no = %s ;'
            r = mycursor.execute(query, SearchBookidEntryval.get())
            if r == True:
                query = 'select roll_no,student_name,student_course,phone,college_name from student_data WHERE roll_no = %s ;'
                mycursor.execute(query, SearchBookidEntryval.get())
                data = mycursor.fetchall()
                for i in data:
                    allStudentinfoTable.delete(*allStudentinfoTable.get_children())
                    tabVal = [i[0], i[1], i[2], i[3], i[4], i[5]]
                    allStudentinfoTable.insert('', END, values=tabVal)
            else:
                messagebox.showinfo('INFORMATION', 'No Student Available With Such Student Id...', parent=dashwin)
    SearchBookbooksubmitbtn = Button(MinisearchbookFrame, text="Search", bg='#2b5eab', fg='white',
                                      activebackground='#1857b5',
                                     bd=0,
                                     activeforeground='white'
                                     , width=8, font=("Arial", 15, "bold"), command=SecStudentsubmitbtnfun)
    SearchBookbooksubmitbtn.place(x=615, y= 10)
    MinishowStudentframe = Frame(showStudentframe, width=850, height=10, bd=0, relief='flat',bg = '#092042')
    MinishowStudentframe.place(x=25, y=90)
    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview', font=('arial', 15, ''),fieldbackground = '#1b4585',borderwidth=0,rowheight=30,
                    background = '#092042',foreground='white', )
    style.configure('Treeview.Heading', font=('arial', 15, 'bold') ,padding=(0,10),foreground='white',activebackground='#095070', background='#092042',)
    style.map('Treeview',background = [('selected','#1857b5')])
    style.map("Treeview.Heading",
          background=[("active", "#1857b5")]) 
    
    Scroll_x = ttk.Scrollbar(MinishowStudentframe, orient=HORIZONTAL,style="Horizontal.TScrollbar")
    Scroll_y = ttk.Scrollbar(MinishowStudentframe, orient=VERTICAL  ,style="Vertical.TScrollbar")
    allStudentinfoTable = Treeview(MinishowStudentframe, columns=('roll_no', 'student_name', 'student_course', 'phone', 'college_name'),
                                xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
    Scroll_x.pack(side=BOTTOM, fill=X ,anchor = W)
    Scroll_y.pack(side=RIGHT, fill=Y ,anchor = N)
    Scroll_x.configure(command=allStudentinfoTable.xview)
    Scroll_y.configure(command=allStudentinfoTable.yview)
    allStudentinfoTable.column('roll_no', width=280, anchor=CENTER)
    allStudentinfoTable.column('student_name', width=320, anchor=CENTER)
    allStudentinfoTable.column('student_course', width=280, anchor=CENTER)
    allStudentinfoTable.column('phone', width=280, anchor=CENTER)
    allStudentinfoTable.column('college_name', width=280, anchor=CENTER)
    # Treeview Heading Tect
    allStudentinfoTable.heading('roll_no', text='Roll No.')
    allStudentinfoTable.heading('student_name', text='Name')
    allStudentinfoTable.heading('student_course', text='Course')
    allStudentinfoTable.heading('phone', text='Phone')
    allStudentinfoTable.heading('college_name', text='College')
    allStudentinfoTable.configure(show='headings')
    allStudentinfoTable.pack(fill='both')
    query = 'SELECT roll_no,student_name,student_course,phone,college_name from student_data;'
    mycursor.execute(query)
    data = mycursor.fetchall()
    for i in data:
        tabVal = [i[0], i[1], i[2], i[3], i[4]]
        allStudentinfoTable.insert('', END, values = tabVal)









# ==============================================================================================================================================
# =================================================================== Add Student  ===============================================================
AddStudframe = Frame(dashwin, bg="#092042", relief='flat', bd=0)
AddStudframe.place(x=0, y=0, relwidth=1,relheight=1)
Label(AddStudframe, image= bg).place(x=0, y=0, relwidth=1, relheight=1)
Button(AddStudframe, bd=0, font=("Arial", 15, "bold"),bg= '#092042',activebackground='#1857b5', image=back,command=lambda: dashboardframe.tkraise()).place(x=10, y=10)

miniaddStudframe = Frame(AddStudframe, bg='#d1dbeb', height=480, width=600, relief='flat', bd=0)
miniaddStudframe.place(x=100, y=20)
addStudframe_title = Label(miniaddStudframe, text="Add Student", bg="#092042", font=("Arial", 16, "bold"),
                           relief='flat', fg='white', width=44, height=2)
addStudframe_title.place(x=10, y=10)
StudidLabel = Label(miniaddStudframe, text="Student ID :", font=("Arial", 15, "bold"), bg='#D1DBEB')
StudidLabel.place(x=60, y=92)
Studidval = StringVar()
StudidEntry = Entry(miniaddStudframe, textvariable=Studidval, bg='#DBE9FF', font=("Arial", 14), bd=0, relief=FLAT,
                width=15)
StudidEntry.place(x=210, y=90)
StudNameLabel = Label(miniaddStudframe, text="Name :", font=("Arial", 15, "bold"), bg='#D1DBEB')
StudNameLabel.place(x=80, y=142)
StudNameval = StringVar()
StudNameEntry = Entry(miniaddStudframe, textvariable = StudNameval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,
                   width=20)
StudNameEntry.place(x=210, y=140)
StudCourseLabel = Label(miniaddStudframe, text="Course : ", font=("Arial", 15, "bold"), bg='#D1DBEB')
StudCourseLabel.place(x=80, y=192)
StudCourseval = StringVar()
StudCourseEntry = Entry(miniaddStudframe, textvariable = StudCourseval, bg='#DBE9FF', font=("Arial", 14), bd=0,
                    relief=FLAT,
                    width=20)
StudCourseEntry.place(x=210, y=190)
StudPhoneLabel = Label(miniaddStudframe, text="Contact : ", font=("Arial", 15, "bold"), bg='#D1DBEB')
StudPhoneLabel.place(x=80, y=242)
StudPhoneval = StringVar()
StudPhoneEntry = Entry(miniaddStudframe, textvariable = StudPhoneval, bg='#DBE9FF', font=("Arial", 14), bd=0,
                     relief=FLAT, width=20)
StudPhoneEntry.place(x=210, y=240)
StudClgLabel = Label(miniaddStudframe, text="College", font=("Arial", 15, "bold"), bg='#D1DBEB')
StudClgLabel.place(x=80, y=292)
StudClgval = StringVar()
StudClgEntry = Entry(miniaddStudframe, textvariable = StudClgval, bg='#DBE9FF', font=("Arial", 14), bd=0, relief=FLAT,
                   width=30)
StudClgEntry.place(x=210, y=290)
def addStudsubmitbtnfunc():
    if (
            Studidval.get() == "" or StudNameval.get() == "" or StudCourseval.get() == "" or StudPhoneval.get() == "" or StudClgval.get() == ""):
        messagebox.showinfo("Info", "All Fields are requi#095070...", parent=dashwin)
    else:
        if len(StudPhoneval.get()) == 10:
            query = "Select roll_no ,student_name ,student_course ,phone ,college_name from student_data where roll_no=%s"
            r = mycursor.execute(query, (Studidval.get()))
            if (r == True):
                messagebox.showinfo("Info", "Student ID already exists!!!", parent=dashwin)
            else:
                query = "insert into student_data(roll_no,student_name,student_course,phone,college_name) values(%s,%s,%s,%s,%s);"
                r = mycursor.execute(query, (
                Studidval.get(), StudNameval.get(), StudCourseval.get(), StudPhoneval.get(), StudClgval.get()))
                if (r == True):
                    messagebox.showinfo("Notification", "Student Successfully Added...", parent=dashwin)
                con.commit()
                Studidval.set("")
                StudNameval.set("")
                StudCourseval.set("")
                StudPhoneval.set("")
                StudClgval.set("")
        else:
            messagebox.showinfo('Information','Student Contact Must Contain 10 digits' ,parent = dashwin)
def addStudResetbtnfunc():
    Studidval.set("")
    StudNameval.set("")
    StudCourseval.set("")
    StudPhoneval.set("")
    StudClgval.set("")
AddStudsubmitbtn = Button(miniaddStudframe, text="Submit", bg='#092042', fg='white',  activebackground='#095070', bd =0,
                          activeforeground='white'
                          , width=16, font=("Arial", 15, "bold"), command=addStudsubmitbtnfunc)
AddStudsubmitbtn.place(x=80, y=350)
AddStudResetbtn = Button(miniaddStudframe, text="Reset", bg='#092042', fg='white',  activebackground='#095070', bd=0,
                          activeforeground='white'
                          , width=16, font=("Arial", 15, "bold"), command=addStudResetbtnfunc)
AddStudResetbtn.place(x=300, y=350)
## ADD Student Dashboard Button



addbookframe = Frame(dashwin, bg="#092042",relief = 'flat' ,bd= 0)
addbookframe.place(x=0,y=0,relwidth = 1, relheight=1)
Label(addbookframe, image=bg).place(x=0, y=0,relwidth = 1 ,relheight = 1)
Button(addbookframe, bd=0, image=back, command=lambda: dashboardframe.tkraise(),bg = '#092042', activebackground='#1857b5').place(x=10, y=10)
miniaddbookframe = Frame(addbookframe, bg='#d1dbeb',height =500,width =600 ,relief = 'flat' ,bd = 4)
miniaddbookframe.place(x=100, y=20)
addbookframe_title = Label(miniaddbookframe, text="Add Book", bg="#092042", font=("Arial", 16, "bold"),relief = 'flat' ,fg='white',width = 44, height=2)
addbookframe_title.place(x=6, y=10)
idval = StringVar()
idLabel = Label(miniaddbookframe, text="Book Id :", font=("Arial", 15, "bold"), bg='#D1DEE4')
idLabel.place(x=80, y=92)
idEntry = Entry(miniaddbookframe, textvariable=idval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT, width=15)
idEntry.place(x=190, y=90)
titleLabel = Label(miniaddbookframe, text="Title :", font=("Arial", 15, "bold"), bg='#D1DEE4')
titleLabel.place(x=80, y=142)
titleval = StringVar()
titleEntry = Entry(miniaddbookframe, textvariable=titleval , bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,
                   width=30)
titleEntry.place(x=190, y=140)
authorLabel = Label(miniaddbookframe, text="Author :", font=("Arial", 15, "bold"), bg='#D1DEE4')
authorLabel.place(x=80, y=192)
authorval = StringVar()
authorEntry = Entry(miniaddbookframe, textvariable=authorval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,
                    width=30)
authorEntry.place(x=190, y=190)
editionLabel = Label(miniaddbookframe, text="Edition :", font=("Arial", 15, "bold"), bg='#D1DEE4')
editionLabel.place(x=80, y=242)
editionval = StringVar()
editionEntry = Entry(miniaddbookframe, textvariable=editionval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,width=30)
editionEntry.place(x=190, y=240)
priceLabel = Label(miniaddbookframe, text="Price :", font=("Arial", 15, "bold"), bg='#D1DEE4')
priceLabel.place(x=80, y=292)
priceval = StringVar()
priceEntry = Entry(miniaddbookframe, textvariable=priceval, bg='#dbe9ff', font=("Arial", 14), bd=0, relief=FLAT,
                   width=15)
priceEntry.place(x=190, y=290)
def addbooksubmitbtnfunc():
    if (
            idval.get() == "" or titleval.get() == "" or authorval.get() == "" or editionval.get() == "" or priceval.get() == ""):
        messagebox.showinfo("Info", "All Fields are requi#095070...", parent=dashwin)
    else:
        query = "Select bookid,title,author,edition,price from storebook where bookid=%s"
        r = mycursor.execute(query, (idval.get()))
        if (r == True):
            messagebox.showinfo("Info", "Book ID already exists!!!", parent=dashwin)
        else:
            query = "insert into storebook(bookid,title,author,edition,price) values(%s,%s,%s,%s,%s);"
            r = mycursor.execute(query,
                                 (idval.get(), titleval.get(), authorval.get(), editionval.get(), priceval.get()))
            if (r == True):
                messagebox.showinfo("Notification", "Book Added Successfully...", parent=dashwin)
            con.commit()
            idval.set("")
            titleval.set("")
            authorval.set("")
            editionval.set("")
            priceval.set("")
def addbookResetbtnfunc():
    idval.set("")
    titleval.set("")
    authorval.set("")
    editionval.set("")
    priceval.set("")
addbooksubmitbtn = Button(miniaddbookframe, text="Submit", bg='#092042', fg='white',  activebackground='#095070', bd =0,
                          activeforeground='white'
                          , width=16, font=("Arial", 15, "bold"), command=addbooksubmitbtnfunc)
addbooksubmitbtn.place(x=80, y=340)
addbookResetbtn = Button(miniaddbookframe, text="Reset", bg='#092042', fg='white',  activebackground='#095070', bd=0,
                          activeforeground='white'
                          , width=16, font=("Arial", 15, "bold"), command=addbookResetbtnfunc)
addbookResetbtn.place(x=300, y=340)












# ==============================================================================================================================================
# =================================================================== Main Frame ===============================================================
dashboardframe = Frame(dashwin)
dashboardframe.pack()
imageLabel = Label(dashboardframe, image=bg,bd = 0, bg="#092042")
imageLabel.pack()
title = Label(dashboardframe, text = 'Library Management System', font=("Courier", 40, "bold underline"), fg='#b5dbff', bg='#111f33', pady=24, padx=24)
title.place(x=350, y=80)
desc = Label(dashboardframe, text = '"Revolutionizing the Way You Manage Books"', font=("Courier", 18, "bold italic"), fg='#ffffff', bg='#111f33', pady=10, padx=24)
desc.place(x=440, y=204)

addBooksButton = Button(dashboardframe, text="Add book", font=("Arial", 18, "bold "), fg='white', pady=4, padx=24,
                      bg="#142a4a",
                       activebackground='#092042'
                      , activeforeground='white', bd=0, compound='left',
                      command=lambda:addbookframe.tkraise())
addBooksButton.place(x= 450 ,y = 320 )
addBooksButton.bind("<Enter>", lambda e: addBooksButton.config(fg='white', bg='#153769'))
addBooksButton.bind("<Leave>", lambda e: addBooksButton.config(fg='white', bg='#142a4a'))

editBookButton = Button(dashboardframe, text="Edit Book", font=("Arial", 18, "bold "), fg='white', pady=4, padx=24,
                      bg="#142a4a",
                       activebackground='#092042'
                      , activeforeground='white', bd=0, compound='left',
                      command=lambda:editBookframe.tkraise())
editBookButton.place(x= 675 ,y = 320 )
editBookButton.bind("<Enter>", lambda e: editBookButton.config(fg='white', bg='#153769'))
editBookButton.bind("<Leave>", lambda e: editBookButton.config(fg='white', bg='#142a4a'))

deleteBookButton = Button(dashboardframe, text="Delete Book", font=("Arial", 18, "bold "), fg='white', pady=4, padx=24,
                    bg="#142a4a",
                       activebackground='#092042'
                      , activeforeground='white', bd=0, compound='left',
                      command=lambda:deleteBookframe.tkraise())
deleteBookButton.place(x= 900 ,y = 320 )
deleteBookButton.bind("<Enter>", lambda e: deleteBookButton.config(fg='white', bg='#153769'))
deleteBookButton.bind("<Leave>", lambda e: deleteBookButton.config(fg='white', bg='#142a4a'))

showBooksButton = Button(dashboardframe, text="Show Books", font=("Arial", 18, "bold "), fg='white', pady=4, padx=24,
                       bg="#142a4a",
                       activebackground='#092042'
                      , activeforeground='white', bd=0, compound='left',
                      command=showAllBooks)
showBooksButton.place(x= 450 ,y = 400 )
showBooksButton.bind("<Enter>", lambda e: showBooksButton.config(fg='white', bg='#153769'))
showBooksButton.bind("<Leave>", lambda e: showBooksButton.config(fg='white', bg='#142a4a'))

issueBookButton = Button(dashboardframe, text="Issue Book", font=("Arial", 18, "bold "), fg='white', pady=4, padx=24,
                     bg="#142a4a",
                       activebackground='#092042'
                      , activeforeground='white', bd=0, compound='left',
                      command=lambda:issuebookframe.tkraise())
issueBookButton.place(x= 675 ,y = 400 )
issueBookButton.bind("<Enter>", lambda e: issueBookButton.config(fg='white', bg='#153769'))
issueBookButton.bind("<Leave>", lambda e: issueBookButton.config(fg='white', bg='#142a4a'))

returnBookButton = Button(dashboardframe, text="Return Book", font=("Arial", 18, "bold "), fg='white', pady=4, padx=24,
                       bg="#142a4a",
                       activebackground='#092042'
                      , activeforeground='white', bd=0, compound='left',
                      command=lambda:ReturnBookframe.tkraise())
returnBookButton.place(x= 900 ,y = 400 )
returnBookButton.bind("<Enter>", lambda e: returnBookButton.config(fg='white', bg='#153769'))
returnBookButton.bind("<Leave>", lambda e: returnBookButton.config(fg='white', bg='#142a4a'))

addStudentButton = Button(dashboardframe, text="Add Student", font=("Arial", 18, "bold "), fg='white', pady=4, padx=24,
                      bg="#142a4a",
                       activebackground='#092042'
                      , activeforeground='white', bd=0, compound='left',
                      command=lambda:AddStudframe.tkraise())
addStudentButton.place(x= 450 ,y = 480 )
addStudentButton.bind("<Enter>", lambda e: addStudentButton.config(fg='white', bg='#153769'))
addStudentButton.bind("<Leave>", lambda e: addStudentButton.config(fg='white', bg='#142a4a'))

showStudentsButton = Button(dashboardframe, text="Show Students", font=("Arial", 18, "bold "), fg='white', pady=4, padx=24,
                        bg="#142a4a",
                       activebackground='#092042'
                      , activeforeground='white', bd=0, compound='left',
                      command=showAllStudents)
showStudentsButton.place(x= 675 ,y = 480 )
showStudentsButton.bind("<Enter>", lambda e: showStudentsButton.config(fg='white', bg='#153769'))
showStudentsButton.bind("<Leave>", lambda e: showStudentsButton.config(fg='white', bg='#142a4a'))

dashwin.mainloop()