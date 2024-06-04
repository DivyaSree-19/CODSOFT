from tkinter import *
root=Tk()
root.geometry("545x450+100+200")
root.title("simple calculater")
root.configure(bg='black')
root.resizable(False,False)


def click():
    pass


e=Entry(root,width=85)
e.grid(row=0,column=0,columnspan=3,pady=2)

btn_1=Button(root,text="1",padx=60,pady=25,command=click)
btn_2=Button(root,text="2",padx=60,pady=25,command=click)
btn_3=Button(root,text="3",padx=60,pady=25,command=click)
btn_add=Button(root,text="+",padx=60,pady=25,command=click)

btn_4=Button(root,text="4",padx=60,pady=25,command=click)
btn_5=Button(root,text="5",padx=60,pady=25,command=click)
btn_6=Button(root,text="6",padx=60,pady=25,command=click)
btn_sub=Button(root,text="-",padx=60,pady=25,command=click)

btn_7=Button(root,text="7",padx=60,pady=25,command=click)
btn_8=Button(root,text="8",padx=60,pady=25,command=click)
btn_9=Button(root,text="9",padx=60,pady=25,command=click)
btn_div=Button(root,text="/",padx=60,pady=25,command=click)

btn_0=Button(root,text="0",padx=60,pady=25,command=click)
btn_d=Button(root,text=".",padx=60,pady=25,command=click)
btn_eq=Button(root,text="=",padx=60,pady=25,command=click)
btn_mul=Button(root,text="*",padx=60,pady=25,command=click)
btn_clear=Button(root,text="Clear",padx=70,pady=25,command=click)


btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)
btn_add.grid(row=3,column=3)


btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_sub.grid(row=2,column=3)

btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)
btn_div.grid(row=1,column=3)

btn_0.grid(row=4,column=0)
btn_d.grid(row=4,column=1)
btn_eq.grid(row=4,column=2)
btn_mul.grid(row=4,column=3)

btn_clear.grid(row=5,column=0)

root.mainloop()
