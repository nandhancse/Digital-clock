from tkinter import*
from time import*
def update():
    timestr=strftime('%I:%M:%S %p')# we can find this value  like I,M,S from the web
    #they do specific things
    time.config(text=timestr)# the label is connected with the time funcion
    time.after(1000, update)

def update1():
    datestr=strftime('%A')
    date.config(text=datestr)
window = Tk()

time=Label(window,font=('impact',20),bg='Black',fg='Green',width=11)
time.pack()
update()
date=Label(window,font=('Ink Free',10),bg='#f2c268',fg='blue',width=20)
date.pack()
update1()
window.mainloop()