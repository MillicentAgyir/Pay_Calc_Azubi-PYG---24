#!/usr/bin/env python
# coding: utf-8

# In[65]:


#The following block imports the libraries we will be using
from tkinter import *
import tkinter as tk 
from tkinter import filedialog
import datetime, time
import pandas as pd

#commented out to add a function with improved capabilities
'''def clock_in():
    global s
    s = time.localtime()
    current_time = time.strftime("%H:%M:%S", s)
    tk.Label(root, text = f"{current_time}").grid(row=2,column=1)'''

def clock_in():
    global s
    if len(write['Started']) < 1 and len(user_name.get()) > 0:   #username must be inputed to start
        s = time.localtime()
        current_time = time.strftime("%H:%M:%S", s)
        tk.Label(root, text = f"{current_time}").grid(row=2,column=1)
        write['Username'].append(user_name.get())                #appending to dictionary to print as csv
        write['Started'].append(time.ctime(time.mktime(s)))
    elif len(user_name.get()) < 1:
        tk.Label(root,text='Error: Please enter a valid username                   ',fg='red').grid(row=6,column=1) #Spaces are necessary to maintain workspace
        #Spaces are necessary to maintain interface
    else:
        tk.Label(root,text='Error: You have already clocked in.                   ',fg='red').grid(row=6,column=1)  #spaces are necessary to maintain work space


#clock out function definition
def clock_out():
    global f
    if (len(write['Finished']) < 1) and (len(write['Started']) == 1): #ensure clock in before clock out
        f = time.localtime()
        current_time = time.strftime("%H:%M:%S", f)
        tk.Label(root, text = f"{current_time}").grid(row=3,column=1)
        write['Finished'].append(time.ctime(time.mktime(f)))
    elif (len(write['Finished'])==1):
        tk.Label(root,text='Error: You have already clocked out                   ',fg='red').grid(row=6,column=1)
    else:
        tk.Label(root,text='Error: Please you must clock in.                      ',fg='red').grid(row=6,column=1)


#commented out to add a function with improved capabilities
'''def clock_out():
    global f
    f = time.localtime()
    current_time = time.strftime("%H:%M:%S", f)
    tk.Label(root, text = f"{current_time}").grid(row=3,column=1)'''

#funtion to convert time
def time_worth():
    global elapsed_time,hours,minutes,seconds
    if len(write['Finished']) == 1 and len(write['Seconds']) < 1:
        elapsed_time = time.mktime(f) - time.mktime(s)
        hours = elapsed_time//3600
        remainder = elapsed_time % 3600
        minutes = remainder// 60
        seconds = remainder % 60
        time_display = Label(root, text = f'{int(hours)} Hours {int(minutes)} Minutes {int(seconds)} Seconds').grid(row = 4,column = 1)
        write['Hours'].append(hours)
        write['Minutes'].append(minutes)
        write['Seconds'].append(seconds)
    elif len(write['Seconds'])==1:
        tk.Label(root,text='Error: Time spent has already been displayed.   ',fg='red').grid(row=6,column=1) #spaces are necessary to maintain workspace formatting
    else:
        tk.Label(root,text='Error: Please clock in and out to find the time',fg='red').grid(row=6,column=1)
        
    return hours,minutes,seconds

#commented out to add a function with improved capabilities    
'''def time_worth():
    global elapsed_time,hours,minutes,seconds
    elapsed_time = time.mktime(f) - time.mktime(s)
    hours = elapsed_time//3600
    remainder = elapsed_time % 3600
    minutes = remainder// 60
    seconds = remainder % 60
    time_display = Label(root, text = f'{hours} Hours {minutes} Minutes {seconds} Seconds').grid(row = 4,column = 1)
    return hours,minutes,seconds'''

#funtion to calculate salary earned
def money_worth():
    global salary
    if len(write['Seconds']) == 1 and len(write['Money($)']) < 1:
        try:
            rate = float(hourly_rate.get())
            salary = round((rate/3600) * elapsed_time,2) 
            results = Label(root, text = "Salary:Earned $%.2f" % salary).grid(row=7, column=1)
            tk.Label(root,text="Thank you for using the PYG-24 Time Tracker.",fg='black').grid(row=6,column=1)
            write['Money($)'].append(salary)
        except ValueError:
            tk.Label(root,text='Error: Enter your valid hourly rate to continue. ',fg='red').grid(row=6,column=1)
    elif len(write['Money($)']) >= 1: #clear and redo
        write['Money($)'].clear()
        try:
            rate = float(hourly_rate.get())
            salary = round((rate/3600) * elapsed_time,2) 
            results = Label(root, text = "Salary:Earned $%.2f" % salary).grid(row=7, column=1)
            tk.Label(root,text="Thank you for using the PYG-24 Time Tracker.",fg='black').grid(row=6,column=1)
            write['Money($)'].append(salary)
        except ValueError:
            tk.Label(root,text='Error: Enter your valid hourly rate to continue. ',fg='red').grid(row=6,column=1)
        
    else:
        tk.Label(root,text='Error: Calculate time spent to continue.          ',fg='red').grid(row=6,column=1)

#commented out to add a function with improved capabilities
'''def money_worth():
    global salary
    rate = float(hourly_rate.get())
    salary = round((rate/3600) * elapsed_time,2) 
    results = Label(root, text = "Week's Pay: $%.2f" % salary).grid(row=6, column=1)'''

#funtion to print to csv
def to_write():
    global df
        #code to make sure changes in name are rectified
    if user_name.get() == write['Username']:
        pass #because no changes is needed
    else:
        write['Username'].clear() #clear the wrong name
        write['Username'].append(user_name.get()) #add the corrected name

    if len(write['Money($)']) > 0:
        df = pd.DataFrame(write)
        export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        df.to_csv (export_file_path, index = False, header=True)
    else:
        tk.Label(root,text='Error: Please fill all your details to continue.  ',fg='red').grid(row=6,column=1)


#These lines of code generate the GUI from tkinter
write = {'Username': [], 'Started': [], 'Finished': [], 'Hours': [], 'Minutes':[], 'Seconds':[], 'Money($)':[]}
root = tk.Tk()
root.geometry('600x300')
root.title('PYG-24 Time Tracker')
can = 0.80
us = 0.85

date = Label(root, text = f"{time.ctime(time.time())}", fg='black').grid(row=0,column=0)
user = Label(root, text = f"   User    ", fg='red').grid(row=1,column=0)

#Declarations
user_name = tk.StringVar(root)
hourly_rate = tk.StringVar(root)

start = Button(root, text = "  Clock In   ", command = clock_in, fg = 'black').grid(row=2,column=0)
finish = Button(root, text = ' Clock Out ', command = clock_out, fg = 'black').grid(row=3,column=0)

#elapsed_time = time.mktime(f) - time.mktime(s)
#a = time_worth(elapsed_time)

time_spent = Button(root, text =f'Time Spent',command = time_worth, fg = 'black').grid(row=4,column=0)
label4 = Label(root, text = "Hourly Rate: ", fg='red').grid(row=1,column=2)

#Calculate Money_made
calculate = Button(root, text=" Calculate   ",command = money_worth).grid(row=5, column=0)
save = Button(root,text='  Save  ',command = to_write).grid(row = 8, column = 2 )




#tkinter.Button(window, text = "Click Me!", command = DataCamp_Tutorial).pack()

#Get Inputs
name = Entry(root, textvariable=user_name).grid(row=1, column=1)
rate = Entry(root, textvariable=hourly_rate).grid(row=1, column=3)


root.mainloop()







