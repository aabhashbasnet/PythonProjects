# tkinter is one of the method used to create GUI 
import tkinter

m = tkinter.Tk(className="Tiktok")
m.title("Counting Seconds")
button = tkinter.Button(m,text="Stop",width=50,height=50,command=m.destroy)
button.pack()
m.mainloop()
