#!/usr/bin/env python
# coding: utf-8

# In[65]:


#The following block imports the libraries we will be using
from tkinter import *
import tkinter as tk 
from tkinter import filedialog


#These lines of code generate the GUI from tkinter
write = {'Started': [], 'Finished': [], 'Hours': [], 'Minutes':[], 'Seconds':[], 'Money($)':[]}
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







