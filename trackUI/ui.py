########################################################################
# track app                                                            #
# version 1.0, pickhacks 2019                                          #
# Authors: Brian Middleton, Adam Bateman, Luke Smith, Katherine Latta  #
########################################################################

# Importation of packages
import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
from notify_run import Notify
import notify_run as nr
import webbrowser
import pymongo
import pandas as pd
from pymongo import MongoClient

# Class that displays the main window
class App(tk.Frame):
	
	def __init__(self, master = None):
		super().__init__(master)
		self.master = master
		master.title("track")
		self.pack()
		self.drawWidgets()
		
	# Function that creates the widgets on the main window, including the logo and buttons. 	
	def drawWidgets(self):
		
		# Logo
		image = Image.open("logo.png")
		logo = ImageTk.PhotoImage(image)
		self.label = tk.Label(self, image=logo, highlightthickness=0,borderwidth=0,bg='#FDFDFD')
		self.label.image = logo
		self.label.grid(columnspan=3,rowspan=3,sticky='ew')
		
		# Subscribe button
		self.subImage = tk.PhotoImage(file='registerButton.png')
		self.sub = tk.Button(self,image=self.subImage,command = self.subscribe,height=45,width=170,bg='#FDFDFD',borderwidth=0)
		self.sub.grid(row=3,column=0,columnspan=3,sticky='ew')
		# Main event buttons
		## Connect to button images
		self.baseballImage = tk.PhotoImage(file='baseballButton.png')
		self.marathonImage = tk.PhotoImage(file='marathonButton.png')
		self.triathlonImage = tk.PhotoImage(file='triathlonButton.png')
		## Draw buttons
		self.baseball = tk.Button(self,image=self.baseballImage,command = self.baseball,height = 45,width = 170,bg = '#FDFDFD',borderwidth=0)
		self.marathon = tk.Button(self,image=self.marathonImage,command = self.marathon,height = 45,width = 170,bg = '#FDFDFD',borderwidth=0)
		self.triathlon = tk.Button(self,image=self.triathlonImage,command = self.triathlon,height = 45,width = 170,bg = '#FDFDFD',borderwidth=0)
		## Manage geometry and placement
		self.baseball.grid(row=4,column=0,sticky='ew')
		self.marathon.grid(row=4,column=1,sticky='ew')
		self.triathlon.grid(row=4,column=2,sticky='ew')
		# Exit Button
		self.exitImage = tk.PhotoImage(file='exitButton.png')
		self.exit = tk.Button(self,image=self.exitImage,command = root.destroy,height=45,width=170,bg = '#FDFDFD',borderwidth=0)
		self.exit.grid(row=5,column=0,columnspan=3,stick='ew')
	
	# baseball button functionality
	def baseball(self):
		event = "baseball"
		top = tk.Toplevel(self,bg="#FDFDFD")
		top.title("Scheduling Assistant")
		msg = tk.Label(top,text="What is the date of the baseball game?",font=("Courier",18),bg='#FDFDFD')
		msg.grid(column = 0, row =0, columnspan = 7)
		dayLabel = tk.Label(top,text="Day: ",font=("Courier",10),bg="#FDFDFD")
		monthLabel = tk.Label(top,text="Month: ",font=("Courier",10),bg="#FDFDFD")
		yearLabel = tk.Label(top,text="Year: ",font=("Courier",10),bg="#FDFDFD")
		monthLabel.grid(column = 2, row = 1)
		dayLabel.grid(column = 3, row = 1)
		yearLabel.grid(column = 4, row = 1)
		self.day = tk.Entry(top,bg="#9C9A9B")
		self.month = tk.Entry(top,bg="#9C9A9B")
		self.year = tk.Entry(top,bg="#9C9A9B")
		self.month.grid(column = 2, row = 2)
		self.day.grid(column = 3, row = 2)
		self.year.grid(column = 4, row = 2)
		top.submitImage = tk.PhotoImage(file='submitButton.png')
		top.submitButton = tk.Button(top,image=top.submitImage,command=lambda : self.saveInput(self.day,self.month,self.year,event),height=45,width=170,bg='#FDFDFD',borderwidth=0)
		top.submitButton.grid(column=3,row=3,sticky = 'ew')
		top.cancelImage = tk.PhotoImage(file='cancelImage.png')
		top.cancelButton = tk.Button(top, image=top.cancelImage,command=top.destroy,height=45,width=170,bg = '#FDFDFD',borderwidth=0)
		top.cancelButton.grid(column=3,row=4, stick = 'ew')
	# marathon button functionality
	def marathon(self):
		event = "marathon"
		top = tk.Toplevel(self,bg="#FDFDFD")
		top.title("Scheduling Assistant")
		msg = tk.Label(top,text="What is the date of the marathon?",font=("Courier",18),bg='#FDFDFD')
		msg.grid(column = 0, row =0, columnspan = 7)
		dayLabel = tk.Label(top,text="Day: ",font=("Courier",10),bg="#FDFDFD")
		monthLabel = tk.Label(top,text="Month: ",font=("Courier",10),bg="#FDFDFD")
		yearLabel = tk.Label(top,text="Year: ",font=("Courier",10),bg="#FDFDFD")
		monthLabel.grid(column = 2, row = 1)
		dayLabel.grid(column = 3, row = 1)
		yearLabel.grid(column = 4, row = 1)
		self.day = tk.Entry(top,bg="#9C9A9B")
		self.month = tk.Entry(top,bg="#9C9A9B")
		self.year = tk.Entry(top,bg="#9C9A9B")
		self.month.grid(column = 2, row = 2)
		self.day.grid(column = 3, row = 2)
		self.year.grid(column = 4, row = 2)
		top.submitImage = tk.PhotoImage(file='submitButton.png')
		top.submitButton = tk.Button(top,image=top.submitImage,command=lambda : self.saveInput(self.day,self.month,self.year,event),height=45,width=170,bg='#FDFDFD',borderwidth=0)
		top.submitButton.grid(column=3,row=3,sticky = 'ew')
		top.cancelImage = tk.PhotoImage(file='cancelImage.png')
		top.cancelButton = tk.Button(top, image=top.cancelImage,command=top.destroy,height=45,width=170,bg = '#FDFDFD',borderwidth=0)
		top.cancelButton.grid(column=3,row=4, stick = 'ew')
	# triathlon button functionality
	def triathlon(self):
		event = "triathlon"
		top = tk.Toplevel(self,bg="#FDFDFD")
		top.title("Scheduling Assistant")
		msg = tk.Label(top,text="What is the date of the triathlon?",font=("Courier",18),bg='#FDFDFD')
		msg.grid(column = 0, row =0, columnspan = 7)
		dayLabel = tk.Label(top,text="Day: ",font=("Courier",10),bg="#FDFDFD")
		monthLabel = tk.Label(top,text="Month: ",font=("Courier",10),bg="#FDFDFD")
		yearLabel = tk.Label(top,text="Year: ",font=("Courier",10),bg="#FDFDFD")
		monthLabel.grid(column = 2, row = 1)
		dayLabel.grid(column = 3, row = 1)
		yearLabel.grid(column = 4, row = 1)
		self.day = tk.Entry(top,bg="#9C9A9B")
		self.month = tk.Entry(top,bg="#9C9A9B")
		self.year = tk.Entry(top,bg="#9C9A9B")
		self.month.grid(column = 2, row = 2)
		self.day.grid(column = 3, row = 2)
		self.year.grid(column = 4, row = 2)
		top.submitImage = tk.PhotoImage(file='submitButton.png')
		top.submitButton = tk.Button(top,image=top.submitImage,command=lambda : self.saveInput(self.day,self.month,self.year,event),height=45,width=170,bg='#FDFDFD',borderwidth=0)
		top.submitButton.grid(column=3,row=3,sticky = 'ew')
		top.cancelImage = tk.PhotoImage(file='cancelImage.png')
		top.cancelButton = tk.Button(top, image=top.cancelImage,command=top.destroy,height=45,width=170,bg = '#FDFDFD',borderwidth=0)
		top.cancelButton.grid(column=3,row=4, stick = 'ew')
	# register button functionality	
	def subscribe(self):
		#notify-run script
		notify = Notify()
		end = notify.register()
		endP = str(end)
		webbrowser.open((endP.split('open: ')[1]).split('\n')[0])
		
		#notify.send("Subscribed Succesfully")
	
	# database querying function, using MongoDB as backend
	def eventTime(self,month,day,year):
		#query database
		#findone from database numWeeks from eventTYpe
		client = pymongo.MongoClient("mongodb+srv://root:trackstar@track-tyc0p.gcp.mongodb.net/test?retryWrites=true")
		db = client.track
		collection = db.Baseball
		data = pd.DataFrame(list(collection.find()))
		print(data)
		#sendTo = Notify()
		#sendTo.send(month + " " + day + " " + year )
		
	# saving user input for use in above buttons
	def saveInput(self,month,day,year,type):
		day = self.day.get()
		if day.isalpha():
			tk.messagebox.showerror("Error","Please enter a valid day. (1-31)")
		elif day == '':
			tk.messagebox.showerror("Error","Please enter a valid day. (1-31)")
		else :
			dayDate = int(day)
			if dayDate < 0 or dayDate > 31:
				tk.messagebox.showerror("Error","Please enter a valid day. (1-31)")
				
		month = self.month.get()
		if month.isalpha():
			tk.messagebox.showerror("Error","Please enter a valid month. (1-12)")
		elif month == '':
			tk.messagebox.showerror("Error","Please enter a valid month. (1-12)")
		else :
			monthDate = int(month)
			if monthDate < 0 or monthDate > 12:
				tk.messagebox.showerror("Error","Please enter a valid month. (1-12)")
				
		year = self.year.get()
		if year.isalpha():
			tk.messagebox.showerror("Error","Please enter a valid year in the format yyyy (e.g 2020)")
		elif year == '':
			tk.messagebox.showerror("Error","Please enter a valid year in the format yyyy (e.g 2020)")
		else :
			if len(year) != 4:
				tk.messagebox.showerror("Error","Please enter a valid year in the format yyyy (e.g 2020)")
				
		print(month + '/' + day + '/' + year)
		self.eventTime(month,day,year)
				
		
		
		
# This code block runs the main application window, as well as sets it's look and geometry		
root = tk.Tk()
root.configure(bg ='#FDFDFD')
gui = App(master = root)
gui.mainloop()