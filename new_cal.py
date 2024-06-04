from tkinter import *

root=Tk()
root.geometry("372x450+150+200")
root.title("simple calculater")
root.configure(bg='black')
root.resizable(False,False)

eq=""

def show(value):
    global eq
    eq+=value
    e.config(text=eq)
    
def clear():
    global eq
    eq=""
    e.config(text=eq)

def cal():
    global eq
    res=""
    if eq != "":
        try:
            res=eval(eq)
        except:
            res="error"
            eq=""
    e.config(text=res)

e=Label(root,width=79,height=2,text="",font=("Helvetica",25,"bold"))
e.pack()


btn_c=Button(root,text="C",padx=24,pady=10,font=("Helvetica",18,"bold"),bg="#3697f5",fg="#fff",bd=2,command=lambda:clear()).place(x=10,y=85)
btn_s=Button(root,text="/",padx=27,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("/")).place(x=100,y=85)
btn_p=Button(root,text="%",padx=25,pady=15,font=("Helvetica",16,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("%")).place(x=189,y=85)
btn_mul=Button(root,text="*",padx=27,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("*")).place(x=280,y=85)

btn_7=Button(root,text="7",padx=25,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("7")).place(x=10,y=155)
btn_8=Button(root,text="8",padx=25,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("8")).place(x=100,y=155)
btn_9=Button(root,text="9",padx=25,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("9")).place(x=190,y=155)
btn_sub=Button(root,text="-",padx=25,pady=10,font=("Helvetica",22,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("-")).place(x=280,y=155)

btn_5=Button(root,text="4",padx=25,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("4")).place(x=10,y=225)
btn_4=Button(root,text="5",padx=25,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("5")).place(x=100,y=225)
btn_6=Button(root,text="6",padx=25,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("6")).place(x=190,y=225)
btn_add=Button(root,text="+",padx=25,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("+")).place(x=280,y=225)

btn_1=Button(root,text="1",padx=25,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("1")).place(x=10,y=295)
btn_2=Button(root,text="2",padx=25,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("2")).place(x=100,y=295)
btn_3=Button(root,text="3",padx=25,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("3")).place(x=190,y=295)

btn_0=Button(root,text="0",padx=70,pady=10,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show("0")).place(x=11,y=365)
btn_d=Button(root,text=".",padx=26,pady=8,font=("Helvetica",20,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:show(".")).place(x=190,y=365)
btn_eq=Button(root,text="=",padx=25,pady=45,font=("Helvetica",18,"bold"),bg="#2a2d36",fg="#fff",bd=2,command=lambda:cal()).place(x=280,y=295)

root.mainloop()
