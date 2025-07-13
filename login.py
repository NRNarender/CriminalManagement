import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import subprocess
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "misurina-sunset.jpg")
        if not os.path.exists(image_path):
            messagebox.showerror("Error", f"Image file '{image_path}' not found")
            self.root.destroy()
            return

        self.bg = ImageTk.PhotoImage(file=image_path)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        get_str = Label(frame, text="ADMIN LOGIN", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=80, y=100)

        # Labels
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=50, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=50, y=220)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = mysql.connector.connect(
                    host=os.getenv('DB_HOST'),
                    user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASSWORD'),
                    database=os.getenv('DB_NAME')
                )
                cur = con.cursor()
                cur.execute("SELECT * FROM login WHERE userid=%s AND password=%s",
                            (self.txtuser.get(), self.txtpass.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid User ID or Password")
                else:
                    messagebox.showinfo("Successful", "Welcome")
                    self.root.destroy()
                    next_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crime_management_system.py")
                    subprocess.call([sys.executable, next_script])
                con.close()
            except Exception as er:
                messagebox.showerror('Error', f'Due to: {str(er)}')

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()