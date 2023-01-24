from tkinter import *
import mysql.connector 
import tkinter.messagebox as msg

root=Tk()
root.geometry("350x350")
root.title("My Tkinter")
root.resizable(width=False,height=False)

def mysql_connect(): 
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tkinter"
        )

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Alert","All Fields are Mandatory !!!")

    else:
        conn = mysql_connect()
        cursor = conn.cursor()
        query = "insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Sucessfully")

def search_data():

    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    
    if e_id.get()=="":
        msg.showinfo("Alert","Id is Mandatory !!!")

    else:
        conn = mysql_connect()
        cursor = conn.cursor()
        query = "select * from student where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
        else:
            msg.showinfo("Search Status","Id Not Found !!!")
            
        conn.commit()
        conn.close()

def update_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" or e_id.get()=="":
        msg.showinfo("Alert","All Fields are Mandatory !!!")

    else:
        conn = mysql_connect()
        cursor = conn.cursor()
        query = "update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Sucessfully")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Alert","ID is  Mandatory !!!")

    else:
        conn = mysql_connect()
        cursor = conn.cursor()
        query = "delete from student where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Sucessfully")


l_id=Label(root,text="ID")
l_id.place(x=40,y=40)

l_fname=Label(root,text="FNAME")
l_fname.place(x=40,y=70)

l_lname=Label(root,text="LNAME")
l_lname.place(x=40,y=100)

l_email=Label(root,text="EMAIL")
l_email.place(x=40,y=130)

l_mobile=Label(root,text="CONTACT")
l_mobile.place(x=40,y=160)

e_id=Entry(root)
e_id.place(x=140,y=40)

e_fname=Entry(root)
e_fname.place(x=140,y=70)

e_lname=Entry(root)
e_lname.place(x=140,y=100)

e_email=Entry(root)
e_email.place(x=140,y=130)

e_mobile=Entry(root)
e_mobile.place(x=140,y=160)

btn1=Button(root,text="SAVE",fg="white",bg="black",font=("Arial 10"),command=insert_data)
btn1.place(x=40,y=200)

btn2=Button(root,text="SEARCH",fg="white",bg="black",font=("Arial 10"),command=search_data)
btn2.place(x=90,y=200)

btn2=Button(root,text="UPDATE",fg="white",bg="black",font=("Arial 10"),command=update_data)
btn2.place(x=158,y=200)

btn3=Button(root,text="DELETE",fg="white",bg="black",font=("Arial 10"),command=delete_data)
btn3.place(x=225,y=200)

root.mainloop()









