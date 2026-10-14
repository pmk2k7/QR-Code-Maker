import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image,ImageTk
import os
import sys
from tkinter import messagebox

root=tk.Tk()
root.title("QR Code Maker 0.1")
root.geometry("500x600")

lbl1=tk.Label(root,text="Enter Text or URL",width=60,font=('Arial',10))
lbl1.pack()
text1=tk.Entry(root,width=60,font=('Arial',10))
text1.pack()
lbl2=tk.Label(root,text="Enter your Logo Path...(Click Browse to select)",width=60,font=('Arial',10))
lbl2.pack()

def on_focus(event):
    if text2.get()=="":
        messagebox.showerror("Empty Logo","Enter Logo is Must")
        text2.focus()
        
text2=tk.Entry(root,width=60,font=('Arial',10))
text2.pack()
text2.bind("<FocusOut>",on_focus)

def brow_file():
    file_path=filedialog.askopenfilename()
    if file_path:
        text2.insert(0,file_path)

butbrowse=tk.Button(root,text="Browse File",command=brow_file)
butbrowse.pack()
lbl3=tk.Label(root,text="File name (type which filename to save QRcode)",width=60,font=('Arial',10))
lbl3.pack()
text3=tk.Entry(root,width=60,font=('Arial',10))
text3.pack()

#GET Local EXE File Path...
if getattr(sys,'frozen',False):
    application_path=os.path.dirname(sys.executable)
else:
    application_path=os.path.dirname(os.path.abspath(__file__))

def create_qr():
    url=text1.get() #"https://pochampallilions.blogspot.com"
    qr_img=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

    qr_img.add_data(url)
    qr_img.make(fit=True)
    qr_img=qr_img.make_image(fill_color="black",back_color="white").convert('RGB')
    logo=Image.open(text2.get())
    qr_size = qr_img.size[0]
    logo_size = qr_size // 4

    logo=logo.resize((logo_size,logo_size))
    pos=((qr_img.size[0]-logo.size[0])//2,(qr_img.size[1]-logo.size[1])//2)
    qr_img.paste(logo,pos)
    
    qr_img.save(text3.get()+".png")

    #show image in tkinter label.
    imgpath=os.path.join(application_path, text3.get()+".png")
    imgqrcode=Image.open(imgpath)
    #image = image.resize((300, 300), Image.ANTIALIAS)
    showimgqrcode=ImageTk.PhotoImage(imgqrcode)
    lblqrphoto.config(image=showimgqrcode)
    lblqrphoto.image=showimgqrcode
    
butcreate=tk.Button(root,text="Create",command=create_qr)
butcreate.pack()
lblqrphoto=tk.Label(root)
lblqrphoto.pack()

lblabout1=tk.Label(root,text="About:\nCreated by தகவல் தொழில்நுட்ப மன்ற மாணவிகள் 2024-2025 ,\nGGHSS,Pochampalli,\nStudents.\n1)S.Srilekha-12 CS\n2)S.Brindha-12CS\n3)K.Haripriya-12CS")
lblabout1.pack()
root.mainloop()
