#install tkinter module by using pip command
#pip install tkinter
from tkinter import *
win = Tk()
#to create a title "Chat bot" to the window
win.title("Chatbot")
#control statements to react to the user's intent
def send():
    send = "You -> "+e.get()
    txt.insert(END, "\n"+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hello")
    elif(user == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I dind't get you")
    e.delete(0, END)
#to create a text area 
txt = Text(win)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(win, width=100)
e.grid(row=1, column=0)
#to create the "SEND" button
send = Button(win, text="Send", command=send).grid(row=1, column=1)
# to run the main loop
win.mainloop()
