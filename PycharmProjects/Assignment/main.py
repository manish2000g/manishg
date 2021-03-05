from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector as ms
from tkinter import filedialog
import os
import random

root = Tk()

class MainWindow:
    def __init__(self):
        self.root = root
        self.root.title("STUDENT MANAGEENT SYSTEM")
        self.root.geometry('1530x790+0+0')
        self.root.resizable(FALSE, FALSE)
        self.frame = Frame(self.root, bg='#DC143C', relief='flat')
        self.frame.place(x=0, y=0, width=1530, height=100)

        self.heading_image = ImageTk.PhotoImage(Image.open('university (1).png'))
        self.label0 = Label(self.root, image = self.heading_image)
        self.label0.image = self.heading_image
        self.heading_label = Label(self.frame, text='Student Management System', fg='black', bg='#DC143C',
                                   font=('times new roman', 35, 'bold'))
        self.heading_label.place(x=0, y=10, width=1530)
        self.heading_label.config(image=self.heading_image, compound=LEFT)

        self.frame2 = Frame(self.root, bg='#B0C4DE', relief='flat')
        self.frame2.place(x=10, y=110, width=1090, height=330)

        self.label = Label(self.frame2, text='Manage Student', font=('times new roman', 22, 'bold'), bg='black',
                           fg='white')
        self.label.place(x=0, y=0, width=1090)

        self.fname = Label(self.frame2, text='First Name :', font=('times new roman', 20, 'bold'), fg='black',
                           bg='#B0C4DE')
        self.fname.place(x=30, y=50)

        self.fentry = Entry(self.frame2, font=('times new roman', 18, 'bold'), relief=RIDGE)
        self.fentry.place(x=30, y=90, width=250)

        self.lname = Label(self.frame2, text='Last Name :', font=('times new roman', 20, 'bold'), fg='black',
                           bg='#B0C4DE')
        self.lname.place(x=320, y=50)

        self.lentry = Entry(self.frame2, font=('times new roman', 18, 'bold'), relief=RIDGE)
        self.lentry.place(x=320, y=90, width=250)

        self.class_label = Label(self.frame2, text='Class :', font=('times new roman', 20, 'bold'), fg='black',
                                 bg='#B0C4DE')
        self.class_label.place(x=610, y=50)

        i = ['First Year(CS)', 'Second Year(CS)', 'Third Year(CS)', 'First Year(IT)', 'Second Year(IT)',
             'Third Year(IT)']
        self.class_combo = ttk.Combobox(self.frame2, values=i, font=('times new roman', 18, 'bold'))
        self.class_combo.place(x=610, y=90, width=250)
        self.class_combo.config(state='readonly')
        self.class_combo.set('        Select Class       ')

        self.rollno = Label(self.frame2, text='ID No :', font=('times new roman', 20, 'bold'), fg='black', bg='#B0C4DE')
        self.rollno.place(x=30, y=130)

        self.rollno_entry = Entry(self.frame2, font=('times new roman', 18, 'bold'), relief=RIDGE)
        self.rollno_entry.place(x=30, y=170, width=250)

        self.h_label = Label(self.frame2, text='', font=('Elephant', 12, 'bold'), fg='red', bg='#B0C4DE')
        self.h_label.place(x=30, y=200)

        self.rollno_entry.bind("<Enter>", self.hover)
        self.rollno_entry.bind("<Leave>", self.hoverleave)

        self.email = Label(self.frame2, text='Email', font=('times new roman', 20, 'bold'), fg='black', bg='#B0C4DE')
        self.email.place(x=320, y=130)

        self.email_entry = Entry(self.frame2, font=('times new roman', 15, 'bold'), relief=RIDGE)
        self.email_entry.place(x=320, y=170, width=250)

        self.contact = Label(self.frame2, text='Contact', font=('times new roman', 20, 'bold'), fg='black',
                             bg='#B0C4DE')
        self.contact.place(x=610, y=130)

        self.contact_entry = Entry(self.frame2, font=('times new roman', 18, 'bold'), relief=RIDGE)
        self.contact_entry.place(x=610, y=170, width=250)

        self.DOB = Label(self.frame2, text='D-O-B :', font=('times new roman', 20, 'bold'), fg='black', bg='#B0C4DE')
        self.DOB.place(x=30, y=230)

        self.DOB_entry = Entry(self.frame2, font=('times new roman', 18, 'bold'), relief=RIDGE)
        self.DOB_entry.place(x=30, y=270, width=250)

        self.Address = Label(self.frame2, text='Address', font=('times new roman', 20, 'bold'), fg='black',
                             bg='#B0C4DE')
        self.Address.place(x=320, y=210)

        self.Address_entry = Text(self.frame2, font=('times new roman', 18, 'bold'), relief=RIDGE)
        self.Address_entry.place(x=320, y=250, width=250, height=70)

        self.gender = Label(self.frame2, text='Gender :', font=('times new roman', 20, 'bold'), fg='black',
                            bg='#B0C4DE')
        self.gender.place(x=610, y=210)

        j = ['Male', 'Female']
        self.gender_entry = ttk.Combobox(self.frame2, values=j, font=('times new roman', 18, 'bold'))
        self.gender_entry.place(x=610, y=250, width=250)
        self.gender_entry.set('Select Gender')
        self.gender_entry.config(state='readonly')

        self.addbutton = Button(self.frame2, text='ADD', font=('times new roman', 15, 'bold'), relief=GROOVE, bd=4,
                                fg='black', bg='#7FFFD4', command=self.add_student)
        self.addbutton.place(x=890, y=80, width=190)

        self.updatebutton = Button(self.frame2, text='UPDATE', font=('times new roman', 15, 'bold'), relief=GROOVE,
                                   bd=4, fg='black', bg='#7FFFD4', command=self.update)
        self.updatebutton.place(x=890, y=140, width=190)

        self.DELETEbutton = Button(self.frame2, text='DELETE', font=('times new roman', 15, 'bold'), relief=GROOVE,
                                   bd=4, fg='black', bg='#7FFFD4', command=self.delete)
        self.DELETEbutton.place(x=890, y=200, width=190)

        self.CLEARbutton = Button(self.frame2, text='CLEAR', font=('times new roman', 15, 'bold'), relief=GROOVE, bd=4,
                                  fg='black', bg='#7FFFD4', command=self.clear)
        self.CLEARbutton.place(x=890, y=260, width=190)

        self.frame3 = Frame(self.root, relief='flat')
        self.frame3.place(x=1110, y=110, width=410, height=330)

        self.photo = ImageTk.PhotoImage(Image.open("student (2).png"))
        self.blabel = Label(self.frame3, image=self.photo)
        self.blabel.image = self.photo
        self.blabel.pack()

        self.frame4 = Frame(self.root, relief=FLAT, bg='#B0C4DE')
        self.frame4.place(x=10, y=450, width=1510, height=330)

        self.subf = Frame(self.frame4, relief=FLAT, bg='white')
        self.subf.place(x=5, y=5, width=1485, height=55)

        self.searchby = Label(self.subf, text='Search By', font=('times new roman', 20, 'bold'), fg='black', bg='white')
        self.searchby.place(x=200, y=10)

        self.k = ['Select Option', 'ID_No', 'Email', 'Contact']
        self.scombo = ttk.Combobox(self.subf, values=self.k, font=('times new roman', 18, 'bold'))
        self.scombo.place(x=350, y=10, width=200)
        self.scombo.set('Select Option')
        self.scombo.config(state='readonly')

        self.sentry = Entry(self.subf, font=('times new roman', 18, 'bold'), relief=RIDGE, bd=2, bg='#F5F5DC')
        self.sentry.place(x=590, y=10, width=300)

        self.search_button = Button(self.subf, text='Search', font=('times new roman', 15, 'bold'), relief=GROOVE, bd=4,
                                    fg='black', bg='#7FFFD4', command=lambda: self.search())
        self.search_button.place(x=920, y=5, width=200)

        self.show_button = Button(self.subf, text='Show All', font=('times new roman', 15, 'bold'), relief=GROOVE, bd=4,
                                  fg='black', bg='#7FFFD4', command=lambda: self.showall())
        self.show_button.place(x=1150, y=5, width=200)

        self.scroll_x = ttk.Scrollbar(self.frame4, orient=VERTICAL)
        self.scroll_y = ttk.Scrollbar(self.frame4, orient=HORIZONTAL)
        self.treview = ttk.Treeview(self.frame4, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show='headings', height=11,
                                    xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=RIGHT, fill=Y)
        self.scroll_y.pack(side=BOTTOM, fill=X)
        self.style = ttk.Style()
        self.style.configure('Treeview', background='lightgray', foreground='black', rowheight=20)
        self.style.map('Treeview', background=[('selected', 'green')])

        self.scroll_x.config(command=self.treview.yview)

        self.treview.heading(1, text='FIRST NAME')
        self.treview.heading(2, text='LAST_NAME')
        self.treview.heading(3, text="CLASS")
        self.treview.heading(4, text='ROll NO')
        self.treview.heading(5, text='EMAIL ID')
        self.treview.heading(6, text='CONTACT')
        self.treview.heading(7, text='D-O-B')
        self.treview.heading(8, text='ADDRESS')
        self.treview.heading(9, text='GENDER')

        self.treview.column(1, width=100, anchor=CENTER)
        self.treview.column(2, width=120, anchor=CENTER)
        self.treview.column(3, width=120, anchor=CENTER)
        self.treview.column(4, width=100, anchor=CENTER)
        self.treview.column(5, width=120, anchor=CENTER)
        self.treview.column(6, width=140, anchor=CENTER)
        self.treview.column(7, width=100, anchor=CENTER)
        self.treview.column(8, width=140, anchor=CENTER)
        self.treview.column(9, width=120, anchor=CENTER)

        self.treview.place(x=5, y=65, width=1485)
        #self.tree()
        self.treview.bind("<ButtonRelease-1>", self.click_insert)

    def add_student(self):
        if self.fentry.get() == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.lentry.get() == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.class_combo.get() == 'Select Class ':
            messagebox.showerror("Error", 'Please Select Class')
        elif self.DOB_entry.get() == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.contact_entry.get() == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.Address_entry.get(1.0, END) == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.gender_entry.get() == 'Select Gender':
            messagebox.showerror("Error", 'Please Select Gender')
        elif self.email_entry.get() == '':
            messagebox.showerror("Error", 'All fields are required')

        else:
            self.Id_No = random.randrange(10000, 90000)
            print(self.Id_No)

            con = ms.connect(host='localhost',user='root',password='manish1#',\
                            database='student_management')
            cur = con.cursor()
            cur.execute(
                "Insert into Student(First_Name,Last_Name,Class,ID_No,Emai,Contact,DOB,Address,Gender) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                self.fentry.get(), self.lentry.get(), self.class_combo.get(), self.Id_No, self.email_entry.get(),
                self.contact_entry.get(), self.DOB_entry.get(), self.Address_entry.get(1.0, END),
                self.gender_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Successfully", 'Student Added Successfully')
            self.tree()
            self.rollno_entry.insert(0, self.Id_No)

    def tree(self):
        con = ms.connect(host='localhost',user='root',password='manish1#',\
                            database='student_management')
        cur = con.cursor()
        cur.execute("Select * from Student")
        self.row = cur.fetchall()
        if len(self.row) != 0:
            self.treview.delete(*self.treview.get_children())
            for i in self.row:
                self.treview.insert('', 'end', values=i)
                con.commit()

    def hover(self, ev):
        self.h_label.config(text='* Do not enter For New Registration')

    def hoverleave(self, ev):
        self.h_label.configure(text='')

    def update(self):
        if self.fentry.get() == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.lentry.get() == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.class_combo.get() == 'Select Class ':
            messagebox.showerror("Error", 'Please Select Class')
        elif self.DOB_entry.get() == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.contact_entry.get() == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.Address_entry.get(1.0, END) == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.gender_entry.get() == 'Select Gender':
            messagebox.showerror("Error", 'Please Select Gender')
        elif self.email_entry.get() == '':
            messagebox.showerror("Error", 'All fields are required')

        else:
            con = ms.connect(host='localhost',user='root',password='manish1#',\
                            database='student_management')
            cur = con.cursor()
            cur.execute(
                "Update Student set First_Name=%s, Last_Name=%s, Class=%s,Emai=%s, Contact=%s, DOB=%s, Address=%s, Gender=%s Where ID_No=%s",
                (self.fentry.get(), self.lentry.get(), self.class_combo.get(), self.email_entry.get(),
                 self.contact_entry.get(), self.DOB_entry.get(), self.Address_entry.get(1.0, END),
                 self.gender_entry.get(), self.rollno_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", 'Data Updated Successfully')
            self.tree()

    def clear(self):
        self.fentry.delete(0, END)
        self.lentry.delete(0, END)
        self.rollno_entry.delete(0, END)
        self.DOB_entry.delete(0, END)
        self.class_combo.set('Select Class')
        self.Address_entry.delete(1.0, END)
        self.contact_entry.delete(0, END)
        self.gender_entry.set('Select Gender')
        self.email_entry.delete(0, END)

    def click_insert(self, ev):
        self.clear()
        self.cur_row = self.treview.focus()
        self.contents = self.treview.item(self.cur_row)
        self.info = self.contents['values']
        print(self.info)
        self.fentry.insert(0, self.info[0])
        self.lentry.insert(0, self.info[1])
        self.class_combo.set(self.info[2])
        self.rollno_entry.insert(0, self.info[3])
        self.email_entry.insert(0, self.info[4])
        self.contact_entry.insert(0, self.info[5])
        self.DOB_entry.insert(0, self.info[6])
        self.Address_entry.insert(1.0, self.info[7])
        self.gender_entry.set(self.info[8])

    def delete(self):
        if self.rollno_entry.get() == '':
            messagebox.showerror("Error", 'please Enter Roll No')
        else:
            con = ms.connect(host='localhost',user='root',password='manish1#',\
                            database='student_management')
            cur = con.cursor()
            cur.execute("Delete From Student Where ID_No=%s", (self.rollno_entry.get(),))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Student Delete Successfully')
            self.tree()

    def search(self):
        if self.scombo.get() == 'ID_No':
            con = ms.connect(host='localhost',user='root',password='manish1#',\
                            database='student_management')
            cur = con.cursor()
            cur.execute("Select * from Student Where ID_No=%s", (self.sentry.get(),))
            self.data = cur.fetchall()
            if len(self.data) != 0:
                self.treview.delete(*self.treview.get_children())
                for i in self.data:
                    self.treview.insert('', 'end', values=i)
                    con.commit()
        elif self.scombo.get() == 'Email':
            con = ms.connect(host='localhost',user='root',password='manish1#',\
                            database='student_management')
            cur = con.cursor()
            cur.execute("Select * from Student Where Emai=%s", (self.sentry.get(),))
            self.data = cur.fetchall()
            if len(self.data) != 0:
                self.treview.delete(*self.treview.get_children())
                for i in self.data:
                    self.treview.insert('', 'end', values=i)
                    con.commit()

        elif self.scombo.get() == 'Contact':
            con = ms.connect(host='localhost',user='root',password='manish1#',\
                            database='student_management')
            cur = con.cursor()
            cur.execute("Select * from Student Where Contact=%s", (self.sentry.get(),))
            self.data = cur.fetchall()
            if len(self.data) != 0:
                self.treview.delete(*self.treview.get_children())
                for i in self.data:
                    self.treview.insert('', 'end', values=i)
                    con.commit()

        else:
            messagebox.showerror("Error", 'Please Select Search Option')

    def showall(self):
        self.tree()


m = MainWindow()
root.mainloop()