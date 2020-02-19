from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter import filedialog
import os
from tkinter.messagebox import askokcancel

class mynote(Frame):
    def __init__(self,parent=None,file=None):
        Frame. __init__(self, parent)
        self.frame = Frame(parent)
        self.frame.pack(fill=X)
        self.layout = Frame(app)
        self.createFile()
        parent.title("MyNote")
        self.createMenu()
        self.textarea()
        self.index = 1.0
        self.path = ''

    def createMenu(self):
        menubar = Menu(app, bg='black',fg='white', relief='sunken')
        menubar.add_command(label="Open",command=self.openf)
        menubar.add_command(label="Save",command=self.savef)
        menubar.add_command(label="Exit",command=self.quitf)
        app.config(menu=menubar)

    def textarea(self):
        scroll = Scrollbar(self)
        paper = Text(self,relief=SUNKEN)
        scroll.config(command=paper.yview)
        paper.config(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        paper.pack(side=LEFT, fill=BOTH, expand=YES)
        self.paper = paper
        self.pack(expand=YES, fill=BOTH)

    def savef(self):
        print(self.path)

        if self.path:
            alltext = self.getText()
            open(self.path, 'w+').write(alltext)
            messagebox.showinfo('Success', 'Your file hane been saved')

        else :
            filetype = [('Text File', '*.txt'), ('Python File','*.py'), ('Word File', '*.doc'), ('All File', '.*')]
            filename = asksaveasfilename(filetypes=(filetype),initialfile=self.ftitle.get())

            if filename:
                alltext = self.getText()
                open(filename, 'w+').write(alltext)
                self.path = filename

    def quitf(self):
        alert = askokcancel('Exit', 'Do you really want to quit ?')    
        if alert:
            Frame.quit(self)

    def setText(self, text='', file=None):
        if file:
            text = open(file,'r+').read()
            self.paper.delete('1.0',END)
            self.paper.insert('1.0',text)
            self.paper.mark_set(INSERT,'1.0')
            self.paper.focus()

    def getText(self):
        return self.paper.get('1.0',END+'-1c')

    def createFile(self):
        self.layout.pack(fill=BOTH, expand=1,padx=17,pady=5)
        title = Label(self.layout,text='File name: ')
        title.pack(side=LEFT)
        self.ftitle = Entry(self.layout)
        self.ftitle.pack(side=LEFT, expand=YES, fill=X)

    def openf(self):
        ext = [('All File','.*'),('Text File','*.txt'),('Word Document','*.doc'),('Python File','*.py')]
        opn = filedialog.askopenfilename(filetypes=ext)
        if opn != '':
            text = self.readFile(opn)

            if text:
                self.path = opn
                name = os.path.basename(opn)
                self.ftitle.delete(0,END)
                self.ftitle.insert(END,name)
                self.paper.delete('0.1',END)
                self.paper.insert(END,text)

    def readFile(self,filename):
        try:
            fn = open(filename,'r+')
            text = fn.read()
            return text
        except:
            messagebox.showerror("Oops! Something Wrong!")
            return None

app = Tk()
mynote(app)
mainloop()