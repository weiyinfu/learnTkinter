import tkinter

class MyButton:
    def __init__(self, root, canvas, label, type):
        self.root = root
        self.canvas = canvas
        self.label = label
        if type == 0:
            button = tkinter.Button(root, text='Draw Line', command=self.DrawLine)
        elif type == 1:
            button = tkinter.Button(root, text='Draw Arc', command=self.DrawArc)
        elif type == 2:
            button = tkinter.Button(root, text='Draw Rec', command=self.DrawRec)
        else:
            button = tkinter.Button(root, text='Draw Oval', command=self.DrawOval)
        button.pack(side = 'left')
    def DrawLine(self):
        self.label.text.set('Draw Line')
        self.canvas.SetStatus(0)
    def DrawArc(self):
        self.label.text.set('Draw Arc')
        self.canvas.SetStatus(1)
    def DrawRec(self):
        self.label.text.set('Draw Rectangle')
        self.canvas.SetStatus(2)
    def DrawOval(self):
        self.label.text.set('Draw Oval')
        self.canvas.SetStatus(3)

class MyCanvas:
    def __init__(self, root):
        self.status = 0
        self.draw = 0
        self.root = root
        self.canvas = tkinter.Canvas(root, bg='white', width=600, height=480)
        self.canvas.pack()
        self.canvas.bind('<ButtonRelease-1>', self.Draw)
        self.canvas.bind('<Button-2>', self.Exit)
        self.canvas.bind('<Button-3>', self.Del)
        self.canvas.bind_all('<Delete>', self.Del)
        self.canvas.bind_all('<KeyPress-d>', self.Del)
        self.canvas.bind_all('<KeyPress-e>', self.Exit)
    def Draw(self, event):
        if self.draw == 0:
            self.x = event.x
            self.y = event.y
            self.draw = 1
        else:
            if self.status == 0:
                self.canvas.create_line(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 1:
                self.canvas.create_arc(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 2:
                self.canvas.create_rectangle(self.x, self.y, event.x, event.y)
                self.draw = 0
            else:
                self.canvas.create_oval(self.x, self.y, event.x, event.y)
                self.draw = 0
    def Del(self, event):
        items = self.canvas.find_all()
        for item in items:
            self.canvas.delete(item)
    def Exit(self, event):
        self.root.quit()
    def SetStatus(self, status):
        self.status = status

class MyLabel:
    def __init__(self, root):
        self.root = root
        self.canvas = canvas
        self.text = tkinter.StringVar()
        self.text.set('Draw Line')
        self.label = tkinter.Label(root, textvariable=self.text, fg='red', width=50)
        self.label.pack(side='left')

root = tkinter.Tk()
canvas = MyCanvas(root)
label = MyLabel(root)
MyButton(root, canvas, label, 0)
MyButton(root, canvas, label, 1)
MyButton(root, canvas, label, 2)
MyButton(root, canvas, label, 3)
root.mainloop()