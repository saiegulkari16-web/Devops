import tkinter as tk #GUI
from time import strftime

root = tk.Tk()
root.title('Digital Clock')

def time():
    string = strftime('%H:%M:%S %p \n %D') # Hour,minutes,seconds,pm/am,date,month
    label.config(text=string) #for changing with time
    label.after(1000,time) #to update time every second

label = tk.Label(root, font=('calibri', 40, 'bold'),\
                  background='black', foreground='lavender')

label.pack(anchor='center') 
time() 

root.mainloop() #start
