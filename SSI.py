import requests
from tkinter import *
from tkinter import ttk, messagebox

class ISS:
	def __init__(self,root):
		#~ this handles the first window
		self.root = root
		self.root.title("ISS Checker")
		self.root.resizable(width="false",height="false")
		self.root.geometry("400x400")
		self.root.config(bg="gray")
		self.front_dec()
		
	def front_dec(self):
		#~ this hadles the first gui display
		#~ self.frame1 = Frame(self.root)
		#~ self.frame1.grid(row=0, column=0, columnspan=100, pady=5, padx=(100,0))
		self.box_title = Label(self.root,relief="sunken", text="ISS information Checker",bg="brown",font=("Arial",19,"bold"))
		self.box_title.grid(row=0, column=0, pady=5, padx=53)
		self.dumb_dir = Label(self.root, text="Click the button below!")
		self.dumb_dir.grid(row=1, column=0, pady=10)
		self.loc_check = Button(self.root, text="Space Station Informations", relief="raised",fg="black",bg="#d2691e", font=("Arial",10,"bold"),command=self.info_show)
		self.loc_check.grid(row=2, column=0, pady=10, sticky=W, padx=(110,0))
		self.info_label = Label(self.root, text="", width=55, height=10,bg="black",fg="brown")
		self.abt_btn = Button(self.root, text="About App",fg="black",bg="#d2691e", font=("Arial",10,"bold"),command=self.about_app)
		self.abt_btn.grid(row=4, column=0, pady=235, sticky=W, padx=(150,0))

	def get_iss_location(self):
		#~ handles iss location
		url = 'http://api.open-notify.org/iss-now.json'
		response = requests.get(url)
		if response.status_code == 200:
			data = response.json()
			latitude = data['iss_position']['latitude']
			longitude = data['iss_position']['longitude']
			self.info_label.config(text=f"Current ISS Position: Latitude: {latitude}, Longitude: {longitude}")
			self.info_label.grid(row=3, column=0, pady=10)
		else:
			messagebox.showerror("Error 404!", "Error fetching data from API")
			
	def get_iss_astronauts(self):
		#~ handles astronaut's name and craft name
		self.root1 = Tk()
		self.root1.title("Astronauts names and craft name")
		self.root1.resizable(width="false",height="false")
		self.name_frame = Frame(self.root1)
		self.name_frame.grid(row=0, column=0)
		self.name_frame.config(bg="brown")
		url = 'http://api.open-notify.org/astros.json'
		response = requests.get(url)
		if response.status_code == 200:
			data = response.json()
			number_of_astronauts = data['number']
			astronauts = data['people']
			
			for idx, astronaut in enumerate(astronauts, start=2):	
				self.info_label1 = Label(self.name_frame,fg="white",bg="black",text=f"{idx - 1}. {astronaut['name']} (Craft: {astronaut['craft']})")
				self.info_label1.grid(row=idx, column=0, pady=10)
		else:
			messagebox.showerror("Error 404!", "Error fetching data from API")

	def info_show(self):
		#~ controls the overall functionality 
		try:
			self.get_iss_location()
			self.get_iss_astronauts()
			self.loc_check.config(state="disabled")
			self.abt_btn.grid(row=4, column=0, pady=55, sticky=W, padx=(150,0))
		except:
			messagebox.showerror("Error 404!","Error fetching data from API \nCheck your network connectivity and try again!")

	def about_app(self):
		messagebox.showinfo("About Application","This app is a mini project created by Fkoan aka TumbCeo \t\nThe main purpose of this app is to provide you with information regarding the current location and names of astronauts currently in the International Space station")

if __name__== "__main__":
	#~ this spectacular app was created by fkoan aka TumbCeo
	root = Tk()
	App = ISS(root)
	root.mainloop()
