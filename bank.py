# import tkinter as tk
# from tkinter import messagebox
# from time import gmtime, strftime

# #Here, in this project, we will use the Tkinter library that will help us in GUI development and the time module that will basically be used to get local time.

# def is_number(s):
#     try:
#         float(s)
#         return 1
#     except ValueError:
#         return 0

# def check_acc_nmb(num):
# 	try:
# 		fpin=open(num+".txt",'r')
# 	except FileNotFoundError:
# 		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
# 		return 0
# 	fpin.close()
# 	return 
#     #  is_number(): It is a combination of the try and except block that returns a floating-point number and the except block handles the ValueError.

#     #check_acc_nmb(): This function is used to check whether the account number with which the user is trying to log in is present or not. For every new user that registers, a new text file with the credentials of the user is created. Here, in this function, we used fopen() to open the file and if the file is not present then a message is displayed using messagebox.showinfo()

# def home_return(master):
#  master.destroy()
# Main_Menu()

# #This function is responsible to take the user back home. This is performed using a destroy() function that destroys the widget and then the Main_Menu() function is called.

# def write(master,name,oc,pin):
	
# 	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
# 		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
# 		master.destroy()
# 		return 

# 	f1=open("Accnt_Record.txt",'r')
# 	accnt_no=int(f1.readline())
# 	accnt_no+=1
# 	f1.close()

# 	f1=open("Accnt_Record.txt",'w')
# 	f1.write(str(accnt_no))
# 	f1.close()

# 	fdet=open(str(accnt_no)+".txt","w")
# 	fdet.write(pin+"\n")
# 	fdet.write(oc+"\n")
# 	fdet.write(str(accnt_no)+"\n")
# 	fdet.write(name+"\n")
# 	fdet.close()

# 	frec=open(str(accnt_no)+"-rec.txt",'w')
# 	frec.write("Date                             Credit      Debit     Balance\n")
# 	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
# 	frec.close()
	
# 	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
# 	master.destroy()
# 	return

#     # responsible for creating a new user’s account. First, it checks whether the user is entering data in a correct format, i.e the name field cannot have a number, etc. If the user entered a value in any field incorrectly then an error is displayed “Error, Invalid Credentials. Please try again.”
# # Now if data is submitted successfully then we opened an Accnt_Record.txt file to read the line and store it in account_no and then the account_no is incremented. This is done in order to assign each user a different account no. Suppose, in the file, there is a number 63710015000, then the account_no will have the value 63710015001 (after increment).
# # Once this is done, this incremented value is written to the Accnt_Record.txt fie. And this account number will be assigned to the user.
# # Now, fdet=open(str(accnt_no)+”.txt”,”w”) this will create a file with the account number that is assigned to the user. And in this file, all the user info will be stored.
# # Another file using frec=open(str(accnt_no)+”-rec.txt”,’w’) is made, and this file will store the transaction details of the user.
# # This file will show the credit, debit, and balance everything with a timestamp.
# # In the end, the user’s account number is displayed and that widget is destroyed using master.destroy().

# def crdt_write(master,amt,accnt,name):

#     # This function crdt_write() in Bank Management System in Python is responsible for crediting the amount. This simply means that whenever the user wants to credit the amount.

# 	if(is_number(amt)==0):
# 		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
# 		master.destroy()
# 		return 
# # First, if block is used to check whether the user entered the number in digits or not. If the user entered the value in the alphabet then an error is displayed. We used our previous function is_number() for this purpose.        

# 	fdet=open(accnt+".txt",'r')
# 	pin=fdet.readline()
# 	camt=int(fdet.readline())
# 	fdet.close()
# 	amti=int(amt)
# 	cb=amti+camt
# 	fdet=open(accnt+".txt",'w')
# 	fdet.write(pin)
# 	fdet.write(str(cb)+"\n")
# 	fdet.write(accnt+"\n")
# 	fdet.write(name+"\n")
# 	fdet.close()
# 	frec=open(str(accnt)+"-rec.txt",'a+')
# 	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
# 	frec.close()
# 	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
# 	master.destroy()
# 	return

#     # Now, if the user enters the amount correctly and presses the submit button then the following process takes place:
# # We opened a file with the format <account_number.txt> and read its first line and stored the output in the variable “pin” and read another line that is the existing amount in the account and stored it in the “camt” variable.
# # The input from the user is stored in the “amti” variable. Now we again opened the account_number.txt file to write the pin, updated balance (previous balance + credited balance), account number, and name.
# # Now we opened a file with format <account_number-rec.txt> and added details like date, time, credit/debit, and balance. We used strftime that returns date and time in string form and gmtime(). The last lines are to display the message and destroy the widget.

# def debit_write(master,amt,accnt,name):

#     # The debit function debit_write() in our Bank Management System Project in python using Tkinter is responsible for updating the two files when the user debits the amount. We used a conditional that if the user enters the debit amount greater than the balance then an error is displayed.

# 	if(is_number(amt)==0):
# 		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
# 		master.destroy()
# 		return 
			
# 	fdet=open(accnt+".txt",'r')
# 	pin=fdet.readline()
# 	camt=int(fdet.readline())
# 	fdet.close()
# 	if(int(amt)>camt):
# 		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
# 	else:
# 		amti=int(amt)
# 		cb=camt-amti
# 		fdet=open(accnt+".txt",'w')
# 		fdet.write(pin)
# 		fdet.write(str(cb)+"\n")
# 		fdet.write(accnt+"\n")
# 		fdet.write(name+"\n")
# 		fdet.close()
# 		frec=open(str(accnt)+"-rec.txt",'a+')
# 		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
# 		frec.close()
# 		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
# 		master.destroy()
# 		return

#         # Another difference between crdt_write() and debit_write() is that in the previous credit function we used to add the previous balance and the credit balance. But in this function, we simply have to change that line and subtract the debit balance from the previous balance i.e cb=camt-amti.

# def Cr_Amt(accnt,name):
# 	creditwn=tk.Tk()
# 	creditwn.geometry("600x300")
# 	creditwn.title("Credit Amount")
# 	creditwn.configure(bg="SteelBlue1")
# 	fr1=tk.Frame(creditwn,bg="blue")
# 	l_title=tk.Message(creditwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	l1=tk.Label(creditwn,relief="raised",font=("Times",16),text="Enter Amount to be credited: ")
# 	e1=tk.Entry(creditwn,relief="raised")
# 	l1.pack(side="top")
# 	e1.pack(side="top")
# 	b=tk.Button(creditwn,text="Credit",font=("Times",16),relief="raised",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
# 	b.pack(side="top")
# 	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))

#    # We declared a function and in that using geometry() we defined the size of the window. Then using title() we gave the title to our window and finally set a background of that window using configure(bg=”SteelBlue1″)

# # Now on top of the window we added the text “BANK MANAGEMENT SYSTEM” and we then configured the font and size of that text. In the last line, the label is packed using pack()

# # We used a label widget to inform users about entering the amount to be credited and used the Entry() widget to take input from users. A button is placed to perform the credit process. When the user clicks on the button, crdt_write() is called and the required operations are performed.  
# # 

# def De_Amt(accnt,name):
# 	debitwn=tk.Tk()
# 	debitwn.geometry("600x300")
# 	debitwn.title("Debit Amount")	
# 	debitwn.configure(bg="SteelBlue1")
# 	fr1=tk.Frame(debitwn,bg="blue")
# 	l_title=tk.Message(debitwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	l1=tk.Label(debitwn,relief="raised",font=("Times",16),text="Enter Amount to be debited: ")
# 	e1=tk.Entry(debitwn,relief="raised")
# 	l1.pack(side="top")
# 	e1.pack(side="top")
# 	b=tk.Button(debitwn,text="Debit",font=("Times",16),relief="raised",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
# 	b.pack(side="top")
# 	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))

#     # Moving ahead in the Bank Management System Project in python using Tkinter, we have the above function. The explanation is the same as that of Cr_Amt, the only difference is that whenever the user clicks on the Debit button, debit_write() is called.
#     # 

# def disp_bal(accnt):
# 	fdet=open(accnt+".txt",'r')
# 	fdet.readline()
# 	bal=fdet.readline()
# 	fdet.close()
# 	messagebox.showinfo("Balance",bal)  

# # This function simply read the balance from the text file and displays it to the user.
# # 

# def disp_tr_hist(accnt):
# 	disp_wn=tk.Tk()
# 	disp_wn.geometry("900x600")
# 	disp_wn.title("Transaction History")
# 	disp_wn.configure(bg="SteelBlue1")
# 	fr1=tk.Frame(disp_wn,bg="blue")
# 	l_title=tk.Message(disp_wn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	fr1=tk.Frame(disp_wn)
# 	fr1.pack(side="top")
# 	l1=tk.Message(disp_wn,text="Your Transaction History:",font=("Times",16),padx=100,pady=20,width=1000,bg="blue4",fg="SteelBlue1",relief="raised")
# 	l1.pack(side="top")
# 	fr2=tk.Frame(disp_wn)
# 	fr2.pack(side="top")
# 	frec=open(accnt+"-rec.txt",'r')
# 	for line in frec:
# 		l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
# 		l.pack(side="top")
# 	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
# 	b.pack(side="top")
# 	frec.close()

#     # Line 1 to 15: We have used our usual Tkinter function to design a transaction window.
# # In these lines, we have opened a file that stores the date, time, credit, debit and balance info. We used a for loop to display the data on the window.

#  #Finally we added a Quit button and closed the file. 
#  # 

# def logged_in_menu(accnt,name):
# 	rootwn=tk.Tk()
# 	rootwn.geometry("1600x500")
# 	rootwn.title("CopyAssignment Bank | Welcome - "+name)
# 	rootwn.configure(background='SteelBlue1')
# 	fr1=tk.Frame(rootwn)
# 	fr1.pack(side="top")
# 	l_title=tk.Message(rootwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	label=tk.Label(text="Logged in as: "+name,relief="raised",bg="blue3",font=("Times",16),fg="white",anchor="center",justify="center")
# 	label.pack(side="top")
# 	img2=tk.PhotoImage(file="credit.gif")
# 	myimg2=img2.subsample(2,2)
# 	img3=tk.PhotoImage(file="debit.gif")
# 	myimg3=img3.subsample(2,2)
# 	img4=tk.PhotoImage(file="balance1.gif")
# 	myimg4=img4.subsample(2,2)
# 	img5=tk.PhotoImage(file="transaction.gif")
# 	myimg5=img5.subsample(2,2)
# 	b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))
# 	b2.image=myimg2
# 	b3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
# 	b3.image=myimg3
# 	b4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
# 	b4.image=myimg4
# 	b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
# 	b5.image=myimg5
	
# 	img6=tk.PhotoImage(file="logout.gif")
# 	myimg6=img6.subsample(2,2)
# 	b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))
# 	b6.image=myimg6
# 	b2.place(x=100,y=150)
# 	b3.place(x=100,y=220)
# 	b4.place(x=900,y=150)
# 	b5.place(x=900,y=220)
# 	b6.place(x=500,y=400)

#     #Line 1 to 12: We again used our usual functions to design the window like geometry(), configure() etc.
# # We used PhotoImage() which displays an image for a particular label or widget.
# # Now we used a Button() widget to display 5 buttons on the window.
# #For eg :command=lambda: Cr_Amt(accnt, name), simply means that whenever the Credit Amount to your Account is clicked Cr_Amt()function is called and the same goes on for the other 4 buttons.
# # We used to place() to place the buttons at different places.  
# # 

# def logout(master):
	
# 	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
# 	master.destroy()
# 	Main_Menu()

# def check_log_in(master,name,acc_num,pin):
# 	if(check_acc_nmb(acc_num)==0):
# 		master.destroy()
# 		Main_Menu()
# 		return

# 	if( (is_number(name))  or (is_number(pin)==0) ):
# 		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
# 		master.destroy()
# 		Main_Menu()
# 	else:
# 		master.destroy()
# 		logged_in_menu(acc_num,name)

#         # The logout() function simply destroys the logged-in menu widget and takes the user to the main screen.
       
#        #check_log_in() this function simply checks if the account number, pin, and name are in the current format or not. And if wrong then takes the user to the Main menu.

# def log_in(master):
# 	master.destroy()
# 	loginwn=tk.Tk()
# 	loginwn.geometry("600x300")
# 	loginwn.title("Log in")
# 	loginwn.configure(bg="SteelBlue1")
# 	fr1=tk.Frame(loginwn,bg="blue")
# 	l_title=tk.Message(loginwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
# 	l_title.config(font=("Arial","50","bold"))
# 	l_title.pack(side="top")
# 	l1=tk.Label(loginwn,text="Enter Name:",font=("Times",16),relief="raised")
# 	l1.pack(side="top")
# 	e1=tk.Entry(loginwn)
# 	e1.pack(side="top")
# 	l2=tk.Label(loginwn,text="Enter account number:",font=("Times",16),relief="raised")
# 	l2.pack(side="top")
# 	e2=tk.Entry(loginwn)
# 	e2.pack(side="top")
# 	l3=tk.Label(loginwn,text="Enter your PIN:",font=("Times",16),relief="raised")
# 	l3.pack(side="top")
# 	e3=tk.Entry(loginwn,show="*")
# 	e3.pack(side="top")
# 	b=tk.Button(loginwn,text="Submit",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
# 	b.pack(side="top")
# 	b1=tk.Button(text="HOME",font=("Times",16),relief="raised",bg="blue4",fg="white",command=lambda: home_return(loginwn))
# 	b1.pack(side="top")
# 	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))

    # We designed this window using various widgets. When submit button is clicked check_log_in() and all the values entered by the user are passed as an argument to that function.
    
    #A home button is added to take the user directly to the main menu. The home_return function is called when the home button is clicked. (Refer to above for a detailed explanation)       

      

