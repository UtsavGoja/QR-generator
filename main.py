import qrcode, PIL
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def createQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 250))
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canva.delete("all")
        qr_canva.create_image(0,0, anchor=tk.NW, image = tkimage)
        qr_canva.image = tkimage
    else:
        messagebox.showwarning("Error", "Enter a link first")
        

def saveQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 250))

        path  = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            resized_img.save(path)
            messagebox.showinfo("Sucess", "QR code is saved")
        else:
            messagebox.showwarning("Error", "Enter a link first")
root = tk.Tk()
root.title("QR Generator")
root.geometry("300x380+600+150")
root.config(bg="light blue")
root.resizable(0, 0)

frame1 = tk.Frame(root, bd = 2, relief=tk.SUNKEN)
frame1.place(x=10,y=0, width = 280, height = 250)

frame2 = tk.Frame(root, bd = 2, relief=tk.SUNKEN)
frame2.place(x=10,y=260, width = 280, height = 90)

cover_img = tk.PhotoImage(file = "py_projects/QR generator/qrcover.png")

qr_canva = tk.Canvas(frame1)
qr_canva.create_image(0,0, anchor = tk.NW, image = cover_img)
qr_canva.bind("<Double-1>", saveQR)
qr_canva.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame2, width=44,font=("times new roman", 10), justify=tk.CENTER)
qr_canva.bind("<Return>", createQR)
text_entry.place(x = 5, y = 5)

btn_1 = ttk.Button(frame2, text="Create", width=10, command=createQR)
btn_1.place(x = 25, y = 50)

btn_2 = ttk.Button(frame2, text="Save", width=10, command=saveQR)
btn_2.place(x = 100, y = 50)

btn_3 = ttk.Button(frame2, text="Exit", width=10, command=root.quit)
btn_3.place(x = 175, y = 50)

root.mainloop()