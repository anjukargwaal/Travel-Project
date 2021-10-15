from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
x=Tk()

def quit():
    x.destroy()
x.title('Tours and Travels')
Label(x,text='Username').grid(row=1)
Label(x,text='Password').grid(row=2)
e1=Entry(x)
e1.grid(row=1,column=1)
e2=Entry(x)
e2.grid(row=2,column=1)
def xyz():
    x=Toplevel()
    def pay():
        messagebox.showinfo("Success","Your booking is Successfully Confirmed")
    def chd():
        x=Toplevel()
        Label(x,text="Choose any package to check inclusion and price").grid(row=0,columnspan=4)
        def silver():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=6000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="silver",command=silver).grid(row=1)
        def gold():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=8000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="Gold",command=gold).grid(row=1,column=1)
        def plt():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=10000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
            
        
        Button(x,text="Platinum",command=plt).grid(row=1,column=2)
        def broz():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=4000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
            
            
        Button(x,text="Brooze",command=broz).grid(row=1,column=3)
        Label(x,text="You Can Check The Places To Visit And Available Hotel Options Below").grid(row=2,column=1)
        Label(x,text="palce to Visit").grid(row=3)
        a=["Sukhna Lake","Rock Garden","Rose Garden","Elante Mall","Sector 17"]
        b=Combobox(x,values=a).grid(row=3,column=1)
        Label(x,text="List of Hotels").grid(row=4)
        c=["Hotel Sunrise","Taj Hotel","5 Star","Beleive in Hotel"]
        d=Combobox(x,values=c).grid(row=4,column=1)

        
    Label(x,text='CHOOSE THE PLACE TO VISIT',bg='light pink',font='BOLD').grid(row=0,columnspan=4)
    Button(x,text="Chandigarh",fg="purple",command=chd).grid(row=1)
    def shimla():
        x=Toplevel()
        Label(x,text="Choose any package to check inclusion and price").grid(row=0,columnspan=4)
        def silver():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=6000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="silver",command=silver).grid(row=1)
        def gold():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=8000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="Gold",command=gold).grid(row=1,column=1)
        def plt():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=10000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="Platinum",command=plt).grid(row=1,column=2)
        def broz():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=4000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="Brooze",command=broz).grid(row=1,column=3)
        
        Label(x,text="You Can Check The Places To Visit And Available Hotel Options Below").grid(row=2,column=1)
        Label(x,text="palce to Visit").grid(row=3)
        a=["Mall Road","Hanuman Temple","Rose Garden","Elante Mall","Sector 17"]
        b=Combobox(x,values=a).grid(row=3,column=1)
        Label(x,text="List of Hotels").grid(row=4)
        c=["Hotel Sunrise","Taj Hotel","5 Star","Beleive in Hotel"]
        d=Combobox(x,values=c).grid(row=4,column=1)

        

        
    Button(x,text="Shimla",fg="blue",command=shimla).grid(row=1,column=1)
    def amritsar():
        x=Toplevel()
        Label(x,text="Choose any package to check inclusion and price").grid(row=0,columnspan=4)
        def silver():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=6000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="silver",command=silver).grid(row=1)
        def gold():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=8000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="Gold",command=gold).grid(row=1,column=1)
        def plt():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=10000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="Platinum",command=plt).grid(row=1,column=2)
        def broz():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=4000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="Brooze",command=broz).grid(row=1,column=3)
        
        Label(x,text="You Can Check The Places To Visit And Available Hotel Options Below").grid(row=2,column=1)
        Label(x,text="palce to Visit").grid(row=3)
        a=["Gold Temple","Jaliyawala Bagh","Nehru Park","Airport"]
        b=Combobox(x,values=a).grid(row=3,column=1)
        Label(x,text="List of Hotels").grid(row=4)
        c=["Hotel Sunrise","Taj Hotel","5 Star","Beleive in Hotel"]
        d=Combobox(x,values=c).grid(row=4,column=1)
        
        
    Button(x,text="Amritsar",fg="red",command=amritsar).grid(row=1,column=2)
    def delhi():
        x=Toplevel()
        Label(x,text="Choose any package to check inclusion and price").grid(row=0,columnspan=4)
        def silver():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=6000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="silver",command=silver).grid(row=1)
        def gold():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=8000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="Gold",command=gold).grid(row=1,column=1)
        def plt():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=10000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="Platinum",command=plt).grid(row=1,column=2)
        def broz():
            x=Toplevel()
            Label(x,text="'Package Inclusions:\n\n1.Arrival at ISBT Shimla\n2.Stay at Hotel Sunrise,Star\n3.Visit To All Tourist").grid(row=1)
            Label(x,text="Package Price=4000(taxes Extra)").grid(row=2)
            Button(x,text="Book and pay now",command=pay).grid(row=3)
            def back():
                x.destroy()
            Button(x,text="Back",command=back).grid(row=3,column=1)
            Button(x,text="Quit",command=quit).grid(row=3,column=2)
        Button(x,text="Brooze",command=broz).grid(row=1,column=3)
        
        Label(x,text="You Can Check The Places To Visit And Available Hotel Options Below").grid(row=2,column=1)
        Label(x,text="palce to Visit").grid(row=3)
        a=["India Gate ","Lal Kila","Qutub Minar","Purain Delhi"]
        b=Combobox(x,values=a).grid(row=3,column=1)
        Label(x,text="List of Hotels").grid(row=4)
        c=["Hotel Sunrise","Taj Hotel","5 Star","Beleive in Hotel"]
        d=Combobox(x,values=c).grid(row=4,column=1)
    Button(x,text="Delhi",fg="green",command=delhi).grid(row=1,column=3)
    
   
Button(x,text="Quit",command=quit).grid(row=3,column=1)
def login():
    if e1.get()=="anju" and e2.get()=="1234":
        xyz()
    else:
        messagebox.showerror("Error","Wrong username or password")
        
Button(x,text="Login",command=login).grid(row=3)

x.mainloop
