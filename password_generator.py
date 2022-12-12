from tkinter import  *
from random import randint

root=Tk()
root.title("Strong Password Generator")
root.geometry("500x300")



def new_rand():
    pw_ent.delete(0, END)
    pw_length=int(ent1.get())
    my_password=""
    for x in range(pw_length):
        my_password += chr(randint(33, 126))
    pw_ent.insert(0,my_password)
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_ent.get())


lbl_f=LabelFrame(root,text="How Many Character ?")
lbl_f.pack(pady=20)
ent1=Entry(lbl_f,font=("Helvetica",24))
ent1.pack(pady=20,padx=20)

pw_ent=Entry(root,text="",font=("Helvetica",24),bd=0,bg="systembuttonface")
pw_ent.pack(pady=20)

#creating frame for button
my_frm=Frame(root)
my_frm.pack(pady=20)

btn1=Button(my_frm,text="Generate Strong Password",command=new_rand)
btn1.grid(row=0,column=0,padx=10)
btn2=Button(my_frm,text="Copy To Clipboard",command=clipper)
btn2.grid(row=0,column=1,padx=10)

root.mainloop()