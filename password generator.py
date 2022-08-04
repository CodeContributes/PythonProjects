# pip install tkinter
from tkinter import * 
# pip install pyperclip
import pyperclip 
import secrets
import string

root = Tk()
root.geometry("700x300")
root.title("Password Generator by Julishiamor Harper")
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)
 
 
def generate():  # Function to generate the password
    pass1 = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for x in range(passlen.get()):
        password += secrets.choice(pass1)
    passwrd.set(password)
 
# function to copy the passcode
 
 
def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)
# Labels
 
 
Label(root, text="Password Generator", font="Raleway 30 ").pack()
Label(root, text="Enter length of generated password").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Tap to get", command=generate).pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=3)
Button(root, text="Tap to copy clipboard", command=copyclipboard).pack()
root.mainloop()
