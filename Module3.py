from tkinter import *
from tkinter import messagebox   
import os
import smtplib
import mimetypes
from email.message import EmailMessage 
 
def register():
    global register_screen 
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.attributes('-fullscreen', True) 
    Label(register_screen ,text="Register",bg="orange",fg="white",width=250,font=("Arial", 15,"bold"), height="4").pack() 
 
    global username
    global password
    global mail
    global username_entry
    global password_entry
    global mail_entry
    username = StringVar()
    password = StringVar()
    mail = StringVar() 
 
    Label(register_screen, text="Please enter details below", bg="blue",fg="white",width="300", height="4", font=("Arial", 20,"bold")).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack() 
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    mail_lable = Label(register_screen, text="Mail Id ")
    mail_lable.pack() 
    mail_entry = Entry(register_screen, textvariable=mail)
    mail_entry.pack()
    Label(register_screen, text="").pack() 
    Button(register_screen, text="Register",activebackground="black",activeforeground="white",bg="DarkGoldenrod2",bd=10,command=register_user).pack()
    Button(register_screen, text="Go back",activebackground="black",activeforeground="white",bg="brown",bd=10,command=start1).pack()
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.attributes('-fullscreen', True)
    Label(login_screen,text="LOGIN",bg="dodger blue",fg="white",width=250,font=("Times New Roman", 15,"bold"), height="4").pack()  
    Label(login_screen, text="Please enter details below to login",bg="light steel blue").pack()
    Label(login_screen, text="",bg="light steel blue").pack()
    login_screen['background']="light steel blue"
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ",bg="light steel blue").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="",bg="light steel blue").pack() 
    Label(login_screen, text="Password * ",bg="light steel blue").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="",bg="light steel blue").pack()
    Button(login_screen, text="  Login  ",activebackground="black",activeforeground="white",bg="green",bd=10,command=login_verify).pack()
    Button(login_screen, text="Go back",activebackground="black",activeforeground="white",bg="brown",bd=10,command=start).pack()
 
def register_user(): 
    global file 
    global username_info 
    global password_info
    global mail_info
 
    username_info = username.get()
    password_info = password.get() 
    mail_info = mail.get()
    
    
    file = open(username_info+".txt","w") 
    u="Your user name---"
    p="Your password--- "
    e="Your mail-id----"
    file.write(u + "\n")
    file.write(username_info + "\n")
    file.write(p + "\n")
    file.write(password_info) 
    file.write(e + "\n")
    file.write(mail_info) 
    file.close() 
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success",fg="green", font=("calibri", 11)).pack()
 
def login_verify():
    username1 = (username_verify.get()+".txt") 
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END) 
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines() 
        if password1 in verify:
            login_sucess() 
        else:
            password_not_recognised()
    else:
        user_not_found()

def login_sucess(): 
    global login_success_screen 
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Logged in Successfully") 
    login_success_screen.attributes('-fullscreen', True) 
    Label(login_success_screen, text="HOME PAGE ",bg="dodger blue",fg="white",width=250, height="4", font=("Times New Roman", 15,"bold")).pack() 
    Label(text="").pack()
    login_success_screen['background']="light steel blue"
    Button(login_success_screen,text="Calculate BMI index",activebackground="black",activeforeground="white",bg="grey63",bd=20,command=bmi).pack()
    Label(text=" ").pack()
    Button(login_success_screen,text="    Add food diet      ",activebackground="black",activeforeground="white",bg="grey63",bd=20,command=food).pack()
    Label(text=" ").pack()
    Button(login_success_screen,text="   Add sleep time      ",activebackground="black",activeforeground="white",bg="grey63",bd=20,command=sleep).pack()
    Label(text=" ").pack()
    Button(login_success_screen,text="  Add workout time  ",activebackground="black",activeforeground="white",bg="grey63",bd=20,command=workout).pack()
    Label(text=" ").pack()
    Button(login_success_screen,text="    Genrate Report      ",activebackground="black",activeforeground="white",bg="grey63",bd=20,command=Mail).pack() 
    Label(text=" ").pack()
    Button(login_success_screen,text="         Log out          ",activebackground="black",activeforeground="white",bg="red2",bd=25,command=out).pack()
    Label(text=" ").pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
def out():
    main_screen.destroy()
    
def out1():
    p1.destroy()
    
def out2():
    p2.destroy() 
    
def out3():
    p3.destroy() 
    
def out4():
    p4.destroy() 
    
def out5():
    p5.destroy() 
    
def start():
    login_screen.destroy() 
    
def start1():
    register_screen.destroy() 

def bmi():
    global p1 
    global A
    global B
    global C
    A=IntVar()
    B=IntVar() 
    p1 = Toplevel(login_success_screen)  
    p1.title("BMI")
    p1.attributes('-fullscreen', True)
    p1['background']="light steel blue"
    Label(p1,text="BMI",bg="orange",fg="white",width=250,font=("Times New Roman", 15,"bold"), height="4").pack()
    Label(p1, text="Enter your weight in Kg: ",bg="light steel blue").pack()
    Entry(p1,textvariable = A).pack() 
    Label(text="").pack() 
    Label(p1, text="Enter you height in centimeters: ",bg="light steel blue").pack()
    Entry(p1, textvariable=B).pack() 
    Label(p1, text="Result:").pack()
    Label(text="").pack()  
    Button(p1,text="Calculate and add data to cloud",activebackground="black",activeforeground="white",bg="green",bd=10,command=solve).pack()
    Label(text="").pack() 
    Button(p1,text="          Go back       ",activebackground="black",activeforeground="white",bg="red2",bd=10,command=out1).pack() 
    
def solve(): 
    kg = int(A.get())
    height = int(B.get())
    height = height /100.0
    res= kg / (height ** 2)
    res1="{:.2f}".format(res)
    one="Your BMI is "+str(res1)+" Oops! You are Overweight" 
    two="Your BMI is "+str(res1)+" Hurray! You are Healthy"
    three="Your BMI is "+str(res1)+" Oops! You are Underweight"
    file = open("analysis.txt","w")
    if (res>=25):
        Label(p1, text=one, fg="green", font=("calibri", 12,"bold")).pack() 
        file.write(one)
        file.write("\n")
        file.write("\n")
    elif (res>=18 and res<=24):
        Label(p1, text=two, fg="green", font=("calibri", 12,"bold")).pack() 
        file.write(two)
        file.write("\n")
        file.write("\n")
    else:
        Label(p1, text=three, fg="green", font=("calibri", 12,"bold")).pack() 
        file.write(three)
        file.write("\n")   
        file.write("\n")
    file.close()
      
def food():
    global p2
    global hear
    hear = StringVar() 
    p2 = Toplevel(login_success_screen)
    p2.title("Food Diet")
    p2.attributes('-fullscreen', True)
    p2['background']="light steel blue"
    Label(p2,bg="orange",text=" Food diet record",fg="white",width=250,font=("Times New Roman", 15,"bold"), height="4").pack() 
    Label(text="").pack() 
    clicked = StringVar()
    options = ["Break-fast","Lunch","Dinner"]   
    clicked.set("Break-fast")
    drop = OptionMenu(p2 , clicked , *options ).pack() 
    Label(p2, text="Enter your items in diet ",bg="light steel blue").pack() 
    Label(text="").pack() 
    Entry(p2,textvariable=hear).pack()
    Label(text="").pack() 
    Button(p2, text="Add data",activebackground="black",activeforeground="white",bg="green",bd=10,command=save).pack()
    Label(text="").pack() 
    Button(p2, text="   Done  ",activebackground="black",activeforeground="white",bg="red2",bd=10,command=out2).pack()
    
def save():
    hear_info = hear.get()
    Label(p2, text="Data added successfully",bg="light steel blue", fg="green", font=("Brush Script MT", 15,"bold")).pack() 
    file = open("analysis.txt","a") 
    file.write("Food items consumed : ")  
    file.write(str(hear_info) + "\n")
    file.write("\n")
    file.close() 
           
def sleep():
    global p3
    global s1
    global e1
    s1 = StringVar()
    e1 = StringVar() 
    p3= Toplevel(login_success_screen) 
    p3.title("Bed timings")
    p3.attributes('-fullscreen', True)
    p3['background']="light steel blue"
    Label(p3,text="Sleep analysis",bg="orange",fg="white",width=250,font=("Times New Roman", 15,"bold"), height="4").pack()
    Label(p3, text="Enter sleep timings ",bg="light steel blue").pack() 
    Label(p3, text="start time ",bg="light steel blue").pack() 
    Entry(p3, textvariable=s1).pack()
    Label(p3, text="end time ",bg="light steel blue").pack() 
    Entry(p3, textvariable=e1).pack() 
    Button(p3, text="Add data",activebackground="black",activeforeground="white",bg="green",bd=10,command=save1).pack()
    Label(text="").pack() 
    Button(p3, text="Done",activebackground="black",activeforeground="white",bg="red2",bd=10,command=out3).pack()
    
def save1():
    s1_info = s1.get()
    e1_info = e1.get() 
    Label(p3, text="Data added successfully",bg="light steel blue" ,fg="green", font=("Brush Script MT", 15,"bold")).pack() 
    file = open("analysis.txt","a") 
    file.write("Timings of Bed time :")  
    file.write("\n")
    file.write("Time of Sleep : "+str(s1_info) + "\n")
    file.write("Wake up : "+str(e1_info) + "\n")
    file.write("\n")
    file.close()     
    
def workout():
    global p4
    global s2
    global e2
    s2 = StringVar() 
    e2 = StringVar() 
    p4= Toplevel(login_success_screen) 
    p4.title("workout timings")
    p4.attributes('-fullscreen', True)
    p4['background']="light steel blue"
    Label(p4,text="Workout tracker",bg="orange",fg="white",width=250,font=("Times New Roman", 15,"bold"), height="4").pack() 
    Label(p4, text="Enter workout timings ",bg="light steel blue").pack() 
    Label(p4, text="start time ",bg="light steel blue").pack() 
    Entry(p4 , textvariable = s2).pack()
    Label(p4, text="end time ",bg="light steel blue").pack() 
    Entry(p4, textvariable = e2).pack() 
    Button(p4, text="Add data",activebackground="black",activeforeground="white",bg="green",bd=10,command=save2).pack()
    Label(text="").pack() 
    Button(p4, text="Submit",activebackground="black",activeforeground="white",bg="red2",bd=10,command=out4).pack()
    
def save2():
    s2_info = s2.get()
    e2_info = e2.get() 
    Label(p4, text="Data added successfully",bg="light steel blue", fg="green", font=("Brush Script MT", 12,"bold")).pack() 
    file = open("analysis.txt","a") 
    file.write("Workout timings :")   
    file.write("\n")
    file.write("Start time : "+str(s2_info) + "\n")
    file.write("End time : "+str(e2_info) + "\n")
    file.write("\n")
    file.write("Nice work !!") 
    file.close() 

def Mail():
    global p5
    global op
    op = StringVar() 
    p5= Toplevel(login_success_screen) 
    p5.title("e-Mail Entry ")
    p5.attributes('-fullscreen', True)
    p5['background']="light steel blue"
    Label(p5,text="REPORT",bg="orange",fg="white",width=250,font=("Times New Roman", 15,"bold"), height="4").pack() 
    Label(p5, text="Enter you E-mail* ",bg="light steel blue").pack()  
    Entry(p5, textvariable = op).pack()
    Button(p5,text="Send",activebackground="black",activeforeground="white",bg="green",bd=10,command=email).pack() 
    Label(text="").pack() 
    Button(p5, text="Done",activebackground="black",activeforeground="white",bg="red2",bd=10,command=out5).pack() 

def email():
    op_info = op.get()
    message = EmailMessage()
    Label(p5, text="Mail sent successfully.",bg="light steel blue", fg="green", font=("calibri", 12,"bold")).pack() 
    sender = "enter your mail"
    recipient = op_info  
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'SMART HEALTH CARE'
    body = """Hello,
              Hope, you are doing well.
              Below are the attachments of you monthly report
              Thank you. Take care."""
    message.set_content(body)
    mime_type, _ = mimetypes.guess_type('analysis.txt')
    mime_type, mime_subtype = mime_type.split('/')
    with open('analysis.txt', 'rb') as file:
        message.add_attachment(file.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename='analysis.txt')
    print(message)
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com') 
    mail_server.set_debuglevel(1)
    mail_server.login("<EMAIL>@gmail.com", 'Password') 
    mail_server.send_message(message)
    mail_server.quit() 
        
def main_account_screen(): 
    global main_screen
    main_screen = Tk()
    main_screen.attributes('-fullscreen', True) 
    main_screen.title("Account Login") 
    s="""WELCOME TO SMART HEALTH CARE
                                        """
    s1="- More than a Doctor"
    Label(main_screen,text=s, bg="dodger blue",fg="white",width=300, height="4", font=("Copperplate Gothic Light", 15,"bold")).pack()
    Label(text="").pack()
    l=Label(main_screen,text=s1,bg="dodger blue",fg="white", font=("Brush Script MT", 20,"bold"))
    l.place(x=800,y=50)
    bg = PhotoImage(file = "shs2.png")
    label1 = Label( main_screen, image = bg)
    label1.place(x = 0, y = 90)
    Button(main_screen,text="  Login   ",activebackground="black",activeforeground="white",bg="VioletRed1",bd=25,command=login).pack()
    Label(text="").pack()
    Button(main_screen,text="Register",activebackground="black",activeforeground="white",bg="dark orchid",bd=25,command=register).pack()
    Label(text="").pack()  
    Button(main_screen,text="   Exit    ",activebackground="black",activeforeground="white",bg="CadetBlue4",bd=30,command=out).pack() 
    Label(text="").pack() 
    #Label(main_screen, bg="orange", width=300, height="25", font=("Calibri", 13)).pack()
    main_screen.mainloop()
 
main_account_screen()
