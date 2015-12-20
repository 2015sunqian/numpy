#tkMessagebox_Test.py
from Tkinter  import *
import tkMessageBox
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.nameInput =Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self,text='Hello',command=self.hello)
		self.alertButton.pack()
	def hello(self):
		#self.nameInput.get()获取用户输入的文本
		name =self.nameInput.get() or 'world'
		tkMessageBox.showinfo('sunqian','hello,%s'%name)#tkMessageBox.showinfo()可以弹出消息对话框
app = Application()
app.master.title('hello world')
app.mainloop()

