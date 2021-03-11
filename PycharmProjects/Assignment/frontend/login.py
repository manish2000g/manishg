from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
from tkinter import messagebox
import backend.dbconnection
import frontend.dashboard
import frontend.register


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("STAFF LOGIN")
        self.root.geometry("1200x700+160+50")
        self.root.config(bg='black')
        self.root.resizable(FALSE, FALSE)
        self.root.grab_set()
        self.db = backend.dbconnection.DBConnect()
        f = font.Font(size=15, slant='italic', underline=TRUE, family='arial')
        self.Login_label = Label(self.root, text="Student management system", font=("times new roman", 16, 'bold'),
                                 bg="yellow", fg="red")
        self.Login_label.place(x=400, y=5)
        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="bisque", fg="black")
        title.pack(side=TOP, fill=X)

        # self.canvas = Canvas(self.root, width=1200, height=700)
        # self.canvas.pack()
        # self.image = PhotoImage(file='student management.jpg')
        # self.canvas.create_image(self,root, image=self.image)
        # #
        self.ph = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\PycharmProjects\\Assignment\\student.png"))
        self.label1 = Label(self.root, image=self.ph)
        self.label1.image = self.ph
        self.label1.pack()
        main_frame = Frame(self.root, bg='purple', relief=RAISED)
        main_frame.place(x=400, y=150, width=400, height=400)
        title = Label(main_frame, text="login!!", relief=GROOVE,
                      font=("times new roman", 20, "bold"), bg="yellow", fg="black")
        title.pack(side=TOP, fill=X)
        lbl_username = Label(main_frame, text='User Name:', font=('arial', 16, 'bold'),
                             fg='Black', bg='white')
        lbl_username.place(x=40, y=80)
        self.ent_username = Entry(main_frame, font=('arial', 14, 'bold'))
        self.ent_username.place(x=180, y=80, width=200)
        self.ent_username.focus_set()
        lbl_password = Label(main_frame, text='Password:', font=('arial', 16, 'bold'),
                             fg='Black', bg='white')
        lbl_password.place(x=40, y=160)
        self.ent_password = Entry(main_frame, font=('arial', 15, 'bold'))
        self.ent_password.place(x=180, y=160, width=200)
        btn_login = Button(main_frame, text='Login', font=('arial', 14, 'bold'),
                           command=self.btn_login_click,
                           bd=5, relief=RAISED)
        btn_login.place(x=70, y=240)
        btn_reset = Button(main_frame, text='Reset', font=('arial', 14, 'bold'),
                           command=self.btn_reset_click,
                           bd=5, relief=RAISED)
        btn_reset.place(x=220, y=240)
        lbl_signup = Label(main_frame, text='No account? Sign Up.', fg='red', bg='white')
        lbl_signup['font'] = f
        lbl_signup.place(x=90, y=300)
        lbl_signup.bind('<Button-1>', self.lbl_signup_click)

    def btn_reset_click(self):
        self.ent_username.delete(0, END)
        self.ent_username.insert(0, "")
        self.ent_password.delete(0, END)
        self.ent_password.insert(0, '')

    def btn_login_click(self):
        uname = self.ent_username.get()
        passw = self.ent_password.get()
        if self.ent_username.get() == '' or self.ent_password.get() == '':
            messagebox.showerror('Error', 'plz fill the empty field')
        else:
            query = "select * from user where Username=%s and Password=%s"
            values = (uname, passw)
            rows = self.db.select(query, values)
            data = []
            if len(rows) != 0:
                for row in rows:
                    data.append(row[0])
                    data.append(row[1])
                print(data)
                if uname == data[0] and passw == data[1]:
                    self.btn_reset_click()
                    messagebox.showinfo('Success', 'Congratulations!! login successful')
                    self.root.destroy()
                    root = Tk()
                    frontend.dashboard.MainWindow(root)
                else:
                    messagebox.showerror('Error', 'Invalid username and password')
            else:
                messagebox.showinfo("Error", "User not registered !! Register first")

    def lbl_signup_click(self, event):
        tk = Toplevel()
        frontend.register.Register_Page(tk)


# root = Tk()
# ob = Login_window(root)
# root.mainloop()
