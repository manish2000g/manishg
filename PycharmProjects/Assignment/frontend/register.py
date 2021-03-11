from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import model.user
import backend.dbconnection


class Register_Page:
    def __init__(self, root):
        self.root = root
        self.root.title('User registration')
        self.root.geometry('950x700')
        self.db = backend.dbconnection.DBConnect()
        self.photo = ImageTk.PhotoImage(Image.open("background_img.png"))
        self.label = Label(self.root, image=self.photo)
        self.label.image = self.photo
        self.label.pack()
        main_frame1 = Frame(self.root, bg='gray', relief=RAISED)
        main_frame1.place(x=300, y=150, width=400, height=400)
        title = Label(main_frame1, text="Create Account!!", relief=GROOVE,
                      font=("times new roman", 20, "bold"), bg="lightblue", fg="black")
        title.pack(side=TOP, fill=X)
        lbl_uname = Label(main_frame1, text='User Name', font=('arial', 14, 'bold'),
                          bg='lavender', fg='blue')
        lbl_uname.place(x=10, y=120)
        self.ent_uname = Entry(main_frame1, font=('arial', 14, 'bold'))
        self.ent_uname.place(x=140, y=120, width=200)
        lbl_password = Label(main_frame1, text='Password', font=('arial', 14, 'bold'),
                             bg='lavender', fg='blue')
        lbl_password.place(x=10, y=160)
        self.ent_password = Entry(main_frame1, font=('arial', 14, 'bold'))
        self.ent_password.place(x=140, y=160, width=200)
        lbl_add = Label(main_frame1, text='Address', font=('arial', 14, 'bold'),
                        bg='lavender', fg='blue')
        lbl_add.place(x=10, y=200)
        self.ent_add = Entry(main_frame1, font=('arial', 14, 'bold'))
        self.ent_add.place(x=140, y=200, width=200)
        lbl_cmb = Label(main_frame1, text='Gender', font=('arial', 15, 'bold'),
                        background='lavender', fg='blue')
        lbl_cmb.place(x=10, y=240)
        self.cmb_gender = ttk.Combobox(main_frame1, font=('arial', 15, 'bold'))
        self.cmb_gender['values'] = ('Male', 'Female', 'Others')
        self.cmb_gender.place(x=140, y=240, width=200)
        btn_register = Button(main_frame1, text='Register', font=('arial', 14, 'bold'), width=8, bd=5, relief=GROOVE,
                              command=self.add_click,
                              padx=5)
        btn_register.place(x=50, y=300)
        btn_reset = Button(main_frame1, text='Reset', font=('arial', 14, 'bold'), width=8, bd=5, relief=GROOVE,
                           command=self.reset_click, padx=5)
        btn_reset.place(x=200, y=300)

    def reset_click(self):
        self.ent_uname.delete(0, END)
        self.ent_password.delete(0, END)
        self.ent_add.delete(0, END)
        self.ent_uname.insert(0, '')
        self.ent_password.insert(0, '')
        self.ent_add.insert(0, '')

    def add_click(self):
        username = self.ent_uname.get()
        password = self.ent_password.get()
        add = self.ent_add.get()
        gender = self.cmb_gender.current()
        gender = self.cmb_gender.get()
        if username == '' or password == '' or add == '' or gender == '':
            messagebox.showerror('Error', 'plz fill the empty field')
            return

        u = model.user.User(username, password, add, gender)
        query = "insert into user(Username,Password,Address,Gender) values(%s,%s,%s,%s)"
        values = (u.get_username(), u.get_password(), u.get_address(), u.get_gender())
        self.db.insert(query, values)
        messagebox.showinfo('Success', 'User Registration successful')
        self.root.destroy()

# root = Tk()
# ob = Register_Page(root)
# root.mainloop()
# #
#
