from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0") #for the measearment of the page
root.title("EL_NORAS TEC Mangement")

text_Input = StringVar()
operator=""

Tops = Frame(root, width= 1600,height=70,bg="light blue" , relief=SUNKEN)
Tops.pack(side=TOP) 

f1 = Frame(root, width= 800,height=700 ,bg="light blue" , relief=SUNKEN)
f1.pack(side=LEFT) 

f2 = Frame(root, width= 300 ,height=700 ,bg="light blue" , relief=SUNKEN)
f2.pack(side=RIGHT) 
#============================TIME==============================
localtime =time.asctime(time.localtime(time.time()))
#============================INFO=================================  
INFO = Label(Tops , font=('arial' , 50 , 'bold') ,text="resturant management system",fg="steel blue", bd=10,anchor='w')
INFO.grid(row=0,column=0)  #this is the heading of the program 

INFO = Label(Tops , font=('arial' , 20 , 'bold') ,text=localtime,fg="steel blue", bd=10,anchor='w')
INFO.grid(row=1,column=0)
#===========================CALCULATOR=========================
def btnClick(num):#this is function for making the button right the num
    global operator
    operator= operator + str(num)
    text_Input.set(operator)


txtDisplay = Entry (f2 , font=('arial' , 20,'bold'),textvariable=text_Input, bd=30,insertwidth=4, bg="light blue", justify='right')

txtDisplay.grid(columnspan=4)
#for button
btn7 =Button(f2,padx=16,pady=16,bd=8 ,fg="Black" , font=('arial',20,'bold'),text="7",bg="light blue",command=lambda:btnClick(7)).grid(row=2,column=0)

btn8 =Button(f2,padx=16,pady=16,bd=8 ,fg="Black" , font=('arial',20,'bold'),text="8",bg="light blue",command=lambda:btnClick(8)).grid(row=2,column=1)

btn9 =Button(f2,padx=16,pady=16,bd=8 ,fg="Black" , font=('arial',20,'bold'),text="9",bg="light blue",command=lambda:btnClick(9)).grid(row=2,column=2)

btn4=Button(f2,padx=16,pady=16,bd=8 ,fg="Black" , font=('arial',20,'bold'),text="4",bg="light blue",command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8 ,fg="Black" , font=('arial',20,'bold'),text="5",bg="light blue",command=lambda:btnClick(5)).grid(row=3,column=1)

root.mainloop()