from tkinter import *
from tkinter import messagebox 
import os
 
# Designing window for registration
 
def register():
    global register_screen 
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.attributes('-fullscreen', True)
    Label(register_screen,text=" REGISTER ", bg="orange", width=300, height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below",).pack()
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
    #Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
    Button(register_screen, text="Register",activebackground="black",activeforeground="white",bg="DarkGoldenrod2",bd=10,command=register_user).pack()
    Button(register_screen, text="Go back",activebackground="black",activeforeground="white",bg="brown",bd=10,command=start1).pack()
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("  Login  ")
    login_screen.attributes('-fullscreen', True)
    
    Label(login_screen,text=" LOGIN ", bg="orange", width=300, height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
    
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    #Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack() 
    Button(login_screen, text="Login",activebackground="black",activeforeground="white",bg="green",bd=10,command=login_verify).pack()
    Button(login_screen, text="Go back",activebackground="black",activeforeground="white",bg="brown",bd=10,command=start).pack()
    #Button(login_screen, text="Quit", width=10, height=1, command = out).pack() 
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
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
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Logged in Successfully") 
    login_success_screen.attributes('-fullscreen', True) 
    Label(login_success_screen, text="Login Success").pack() 
    Label(text="").pack()
    login_success_screen['background']="lightblue"
    Label(login_success_screen,text="  HOME PAGE ", bg="orange", width=300, height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(login_success_screen,text="Calculate BMI index", height="2", width="30",bg="red", command = bmi).pack()
    Label(text="").pack()
    Button(login_success_screen,text="Add food diet", height="2", width="30",bg="red", command=food).pack()
    Label(text="").pack()
    Button(login_success_screen,text="Add sleep time", height="2", width="30",bg="red", command=sleep).pack()
    Label(text="").pack()
    Button(login_success_screen,text="Add workout time", height="2", width="30",bg="red", command=workout).pack()
    Label(text="").pack() 
    Button(login_success_screen,text="Log out", height="2", width="30",bg="orange", command=out).pack()
    Label(text="").pack()
 

# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
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
    
def start():
    login_screen.destroy() 
    
def start1():
    register_screen.destroy() 

    
def bmi():
    global p1 
    global A 
    global B 
    global C
    
    p1 = Toplevel(login_success_screen)  
    p1.title("BMI")
    p1.attributes('-fullscreen', True)
    Label(p1,text="  BMI ", bg="orange", width=300, height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(p1, text="Enter your weight in Kg: ").pack()
    A = Entry(p1).pack()
    Label(text="").pack() 
    Label(p1, text="Enter you height in metres square: ").pack()
    B = Entry(p1).pack()
    Label(p1, text="Result:").pack()
    Label(text="").pack()  
    
    Button(p1,text="Calculate",activebackground="black",activeforeground="white",bg="VioletRed1",bd=10,command=solve).pack()
    Label(text="").pack() 
    Button(p1,text="Go back",activebackground="black",activeforeground="white",bg="green",bd=10,command=out1).pack() 
    
def solve(): 
    #kg1 = A.get()
    #kg=int(kg1)
    #height1 = B.get()
    #height=height(height1)
    #res=round(kg / (height ** 2), 2) 
   # s1="Your BMI is "+str(res)+" Oops! You are Overweight" 
   # s2="Your BMI is "+str(res)+" Hurray! You are Healthy"
    s2="Your BMI is normal Hurray! You are Healthy"
   # s3="Your BMI is "+str(res)+" Oops! You are Underweight"
    #if (res>=25.0):
      #  messagebox.showinfo("Results",s1)
    #elif (res>=18.5 and res<=24.9):
    messagebox.showinfo("Results",s2)
    #else:
     #   messagebox.showinfo("Results",s3)  
    
    
    # Label(p1, text="Your BMI is "+str(c)).pack() 
    # Label(text="").pack()
    # if c>=25.0:
    #     Label(p1, text="Oops! You are Overweight").pack() 
    #     Label(text="").pack()
    # elif c>=18.5 and c<=24.9:
    #     Label(p1, text="Hurray! You are Healthy").pack() 
    #     Label(text="").pack()
    # else:
    #     Label(p1, text="Oops! You are Underweight").pack() 
    #     Label(text="").pack()
    
    
def food():
    global p2
    p2 = Toplevel(login_success_screen)
    p2.title("Food Diet")
    p2.attributes('-fullscreen', True)
    Label(p2,text="  Food diet record ", bg="orange", width=300, height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    clicked = StringVar()
    options = ["Break-fast","Lunch","Dinner"]   
    clicked.set("Break-fast")
    drop = OptionMenu(p2 , clicked , *options ).pack() 
    Label(p2, text="Enter your items in diet ").pack() 
    Label(text="").pack() 
    Entry(p2).pack()
    Button(p2, text="Submit",activebackground="black",activeforeground="white",bg="green",bd=10,command=out2).pack()
    # clicked = StringVar()
    # options = ["1","2","3","4","5","6","7","8","9","10"]   
    # clicked.set("1")
    #Label(p2,text="enter the food items").pack()
    # for i in range(clicked.get()):
    #     c1=Entry(p2).pack()
    #Label(p2, text="Enter time ").pack() 
    #Entry(p2).pack
    #Button(p2,text="Submit",command=out2).pack()
    
def sleep():
    global p3
    p3= Toplevel(login_success_screen) 
    p3.title("Bed timings")
    p3.attributes('-fullscreen', True)
    Label(p3,text="  Sleep analysis  ", bg="orange", width=300, height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(p3, text="Enter sleep timings ").pack() 
    Label(p3, text="start time ").pack() 
    Entry(p3).pack()
    Label(p3, text="end time ").pack() 
    Entry(p3).pack()
    Button(p3, text="Submit",activebackground="black",activeforeground="white",bg="green",bd=10,command=out3).pack()
    
def workout():
    global p4
    p4= Toplevel(login_success_screen) 
    p4.title("workout timings")
    p4.attributes('-fullscreen', True)
    Label(p4,text="  Workout tracker ", bg="orange", width=300, height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(p4, text="Enter workout timings ").pack() 
    Label(p4, text="start time ").pack() 
    Entry(p4).pack()
    Label(p4, text="end time ").pack() 
    Entry(p4).pack() 
    Button(p4, text="Submit",activebackground="black",activeforeground="white",bg="green",bd=10,command=out4).pack()
    
    
    
# def foodlist():
#     listbox = Listbox(p2,background="yellow", fg="black",highlightbackground="blue",highlightthickness=10,selectbackground="green",highlightcolor="red")
#     Label(p2, text = " FOOD ITEMS").pack()
#     for i in range(clicked.get()):
#         listbox.insert(i+1, )
#     listbox.pack()
    

    # Designing Main(first) window
def main_account_screen(): 
    global main_screen
    main_screen = Tk()
    main_screen.attributes('-fullscreen', True)
    #main_screen.geometry("300x250")
    bg = PhotoImage(file = "shs2.png")
    label1 = Label( main_screen, image = bg)
    label1.place(x = 0, y = 0)
    main_screen.title("Account Login") 
    Label(main_screen,text="SMART HEALTHCARE SYSTEM", bg="orange", width=300, height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    # Radiobutton(main_screen,text="Login", height="2", width="30", command = login).pack()
    # Label(text="").pack()
    # Radiobutton(main_screen,text="Register", height="2", width="30", command=register).pack()
    # Label(text="").pack()
    # Radiobutton(main_screen,text="Exit", height="2", width="30", command=out).pack()
    
    Button(main_screen,text="  Login ",activebackground="black",activeforeground="white",bg="VioletRed1",bd=10,command=login).pack()
    Label(text="").pack()
    Button(main_screen,text="Register",activebackground="black",activeforeground="white",bg="dark orchid",bd=10,command=register).pack()
    Label(text="").pack() 
    Button(main_screen,text="  Exit  ",activebackground="black",activeforeground="white",bg="CadetBlue4",bd=10,command=out).pack() 
     
    main_screen.mainloop()
 
 
main_account_screen()
