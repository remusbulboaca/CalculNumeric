from tkinter import *
from tkinter import filedialog

from tkinter.ttk import *
from time import strftime
from main import *


def Upload(root):
    def UploadAction():
        filename = filedialog.askopenfilename()
        main(filename,"File",0)
        configfile = Text(root, wrap=WORD, width=45, height=65)
        with open("out.txt", 'r') as f:
            configfile.insert(INSERT, f.read())
        configfile.pack(fill="none", expand=TRUE)


    def Generate():
        main(0, "Generate", user_input.get())


        configfile = Text(root, wrap=WORD, width=45, height=65)
        with open("out.txt", 'r') as f:
            configfile.insert(INSERT, f.read())
        configfile.pack(fill="none", expand=TRUE)



    button = Button(root, text='Import Matrix', command=UploadAction)

    button.pack(pady=35)

    user_input = StringVar(root)
    e1 = Entry(root, textvariable=user_input)
    e1.insert(END, 'Marimea matricii')
    e1.pack()

    button = Button(root, text='Generate', command=Generate)
    button.pack()



app = Tk()
app.geometry("500x500")
Upload(app)

app.mainloop()
