import os

from tkinter import *

from tkinter import messagebox

global Collegename 
global year        
global department  
global name       
global mobilenum   
global Email       

try:
    os.mkdir("college_database")
except:
    print("already exit")

class Register:

    
    
    def RegisterFormStore(Self):



        Collegenameget = Collegename.get()
        yearget        = year.get()
        deptget        = department.get()
        nameget        = name.get()
        mobileget      = mobilenum.get()
        Emailget       = Email.get()

        print(Collegenameget)
        print(yearget)
        print(deptget)
        print(nameget)
        print(mobileget)
        print(Emailget)

        try:
            os.mkdir("college_database/"+Collegenameget)
        except:
            print("already exist")

        try:
            os.mkdir("college_database/"+Collegenameget+"/"+yearget)
        except:
            print("already exist")

        try:
            os.mkdir("college_database/"+Collegenameget+"/"+yearget+"/"+deptget)
        except:
            print("already exist")

        file = open("college_database/"+Collegenameget+"/"+yearget+"/"+deptget+"/"+deptget+".csv",'a')

        file.write("\n"+nameget+", \t"+mobileget+", \t"+Emailget)

        file.close()
        
        
    def register_init(self):


        
        global Collegename 
        global year        
        global department  
        global name       
        global mobilenum   
        global Email       

    
        register_form = Tk()
        
        register_form.geometry("1600x1000")

        register_form.configure(bg = "green")

        Collegename = StringVar()
        year        = StringVar()
        department  = StringVar()
        name        = StringVar()
        mobilenum   = StringVar()
        Email       = StringVar()


        Label(register_form,text="Register form : ",font=("Aerial",30),bg="purple",fg="white").place(x=0,y=0)

        Label(register_form,text="College name : ",font=("Aerial",15),bg="green",fg="white").place(x=100,y=100)

        Label(register_form,text="year : ",font=("Aerial",15),bg="green",fg="white").place(x=100,y=150)

        Label(register_form,text="department : ",font=("Aerial",15),bg="green",fg="white").place(x=100,y=200)

        Label(register_form,text="Name : ",font=("Aerial",15),bg="green",fg="white").place(x=100,y=250)

        Label(register_form,text="mobile no: ",font=("Aerial",15),bg="green",fg="white").place(x=100,y=300)

        Label(register_form,text="Email: ",font=("Aerial",15),bg="green",fg="white").place(x=100,y=350)
        
 
        Entry(register_form,textvariable=Collegename).place(x=250,y=100,width=300)

        Entry(register_form,textvariable=year).place(x=250,y=150,width=300)

        Entry(register_form,textvariable=department).place(x=250,y=200,width=300)

        Entry(register_form,textvariable=name).place(x=250,y=250,width=300)

        Entry(register_form,textvariable=mobilenum).place(x=250,y=300,width=300)

        Entry(register_form,textvariable=Email).place(x=250,y=350,width=300)

        
        Register_button = Button(register_form, text="Register",font=("Aerial",15), command=self.RegisterFormStore)
        
        Register_button.place(x=250,y=400)

        register_form.mainloop()

     

a=Register()

a.register_init()

