import webbrowser
from tkinter import Frame,Label,Entry,Button,StringVar,Tk
import numpy as np
root =Tk()
root.configure(bg='#5e515b')

# setting the windows size
root.geometry("800x800")
    
def clearentry():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    entry3.delete(0,'end')
    entry4.delete(0,'end')
    entry5.delete(0,'end')
    entry6.delete(0,'end')
    entry7.delete(0,'end')
    entry8.delete(0,'end')
    entry9.delete(0,'end')
    entry10.delete(0,'end')
    entry11.delete(0,'end')
    entry12.delete(0,'end')
    entry13.delete(0,'end')
    outputlabel.configure(text= 'Output will be shown here')
    
    
def callback(url):
    webbrowser.open_new(url)
    

def take_data():
    d1 = []
    d1.append(entry1.get())
    d1.append(entry2.get())
    d1.append(entry3.get())
    d1.append(entry4.get())
    d1.append(entry5.get())
    d1.append(entry6.get())
    d1.append(entry7.get())
    d1.append(entry8.get())
    d1.append(entry9.get())
    d1.append(entry10.get())
    d1.append(entry11.get())
    d1.append(entry12.get())
    d1.append(entry13.get())
    d2 = []
    d2.append(d1)
    if dt.predict(d2)==1:
        outputlabel.configure(text='EARTHQUAKE DETECTED')
        print("EARTHQUAKE DETECTED")
    else:  
        outputlabel.configure(text='NO EARTHQUAKE DETECTED')
        print("NO EARHTQUAKE")
    
displayFrame = Frame(root,bg ='#6787d6')
displayFrame.pack(pady=20)

detailsframe = Frame(displayFrame,bg='#d8dbe3')
detailsframe.pack()
desclabel= Label(detailsframe,text = 'Earthquake Detection Using Machine Learning Techinque ',height=2,bg='#d8dbe3',font=('default',20))
desclabel.grid(columnspan=10)

asklabel= Label(detailsframe,text = 'Enter input data to check',font=('default',14),bg='#d8dbe3',height=2)
asklabel.grid(row=1,padx=80,columnspan=10)

label1 = Label(detailsframe,text='Latitude',bg='#d8dbe3',font=('default',10))
label1.grid(pady=3,row = 2,column=4)

entry1 = Entry(detailsframe,width=8,font=('default',10))
entry1.grid(row = 2,column=5)

label2 = Label(detailsframe,text='Longitude',bg='#d8dbe3',font=('default',10))
label2.grid(pady=3,row = 3,column=4)

entry2 = Entry(detailsframe,width=8,font=('default',10))
entry2.grid(row = 3,column=5)

label3 = Label(detailsframe,text='Depth',bg='#d8dbe3',font=('default',10))
label3.grid(pady=3,row = 4,column=4)

entry3 = Entry(detailsframe,width=8,font=('default',10))
entry3.grid(row = 4,column=5)

label4 = Label(detailsframe,text='Depth Error',bg='#d8dbe3',font=('default',10))
label4.grid(pady=3,row = 5,column=4)

entry4 = Entry(detailsframe,width=8,font=('default',10))
entry4.grid(row = 5,column=5)

label5 = Label(detailsframe,text='Depth Seismic Stations',bg='#d8dbe3',font=('default',10))
label5.grid(pady=3,row = 6,column=4)

entry5 = Entry(detailsframe,width=8,font=('default',10))
entry5.grid(row = 6,column=5)

label6 = Label(detailsframe,text='Magnitude',bg='#d8dbe3',font=('default',10))
label6.grid(pady=3,row = 7,column=4)

entry6 = Entry(detailsframe,width=8,font=('default',10))
entry6.grid(row = 7,column=5)

label7 = Label(detailsframe,text='Magnitude Type',bg='#d8dbe3',font=('default',10))
label7.grid(pady=3,row = 8,column=4)

entry7 = Entry(detailsframe,width=8,font=('default',10))
entry7.grid(row = 8,column=5)

label8 = Label(detailsframe,text='Magnitude Error',bg='#d8dbe3',font=('default',10))
label8.grid(pady=3,row = 9,column=4)

entry8 = Entry(detailsframe,width=8,font=('default',10))
entry8.grid(row = 9,column=5)

label9 = Label(detailsframe,text='Magnitude Seismic Stations',bg='#d8dbe3',font=('default',10))
label9.grid(pady=3,row = 10,column=4)

entry9 = Entry(detailsframe,width=8,font=('default',10))
entry9.grid(row = 10,column=5)

label10 = Label(detailsframe,text='Azimuthal Gap',bg='#d8dbe3',font=('default',10))
label10.grid(pady=3,row = 11,column=4)

entry10 = Entry(detailsframe,width=8,font=('default',10))
entry10.grid(row = 11,column=5)

label11 = Label(detailsframe,text='Horizontal Distance',bg='#d8dbe3',font=('default',10))
label11.grid(pady=3,row = 12,column=4)

entry11 = Entry(detailsframe,width=8,font=('default',10))
entry11.grid(row = 12,column=5)

label12 = Label(detailsframe,text='Horizontal Error',bg='#d8dbe3',font=('default',10))
label12.grid(pady=3,row =13,column=4)

entry12 = Entry(detailsframe,width=8,font=('default',10))
entry12.grid(row = 13,column=5)

label13 = Label(detailsframe,text='Root Mean Square',bg='#d8dbe3',font=('default',10))
label13.grid(pady=3,row = 14,column=4)

entry13 = Entry(detailsframe,width=8,font=('default',10))
entry13.grid(row = 14,column=5)

clearbutton = Button(detailsframe,text='Clear All',bg='#de4b69',font=('default',8),command=lambda:clearentry())
clearbutton.grid(row = 8,column=7,padx=5,pady=5)


checkbutton = Button(detailsframe,text='Check',width=10,bg='#6787d6',font=('default',13),command=lambda:take_data())
checkbutton.grid(columnspan=10,pady=10)

outputlabel = Label(detailsframe,text='output will be shown here',font=('default',12),bg='#d8dbe3',height=2)
outputlabel.grid(padx=80,columnspan=10,pady=5)

link1 = Label(detailsframe, text="Know more about earthquake", fg="blue", cursor="hand2",font=('default',12),bg='#d8dbe3',height=2)
link1.grid(columnspan=10,pady=5)
link1.bind("<Button-1>", lambda e: callback("https://en.wikipedia.org/wiki/Earthquake"))

root.mainloop()
