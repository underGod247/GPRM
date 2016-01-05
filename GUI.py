'''
GUI for the gran prix race management interface
Tabs: Registration, Race Admin, Device Admin
'''

from tkinter import ttk
import tkinter

def gui():
	root = tkinter.Tk()
	root.title("PyGP Managment GUI")
	root.minsize(width=500, height=500)
	
	tabs = ttk.Notebook(root)
	
	regTab = ttk.Frame(tabs)
	raceTab = ttk.Frame(tabs)
	devTab = ttk.Frame(tabs)
	
	tabs.add(regTab, text='Registration')
	tabs.add(raceTab, text='Race Admin')
	tabs.add(devTab, text='Device Admin')
	
	tabs.pack(expand=1, fill="both")
	
	root.mainloop()
	
if __name__ == "__main__":
	gui()