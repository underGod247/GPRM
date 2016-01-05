'''
GUI for the gran prix race management interface
Tabs: Registration, Race Admin, Device Admin
'''

from tkinter import ttk
from tkinter import *
import tkinter
import serial
from time import sleep

#create a placeholder for the serial port
finishLine = serial.Serial()
finishLine.baudrate = 9600
finishLine.timeout = 1

#define subroutines here

#the subroutine to set the port number
def setPort():
	finishLine.port = serialPortString.get()
	finishLine.open()
	finishLine.flushInput();
	finishLine.flushOutput();
	root.after(500, readSerial)
	
#the subroutine to send a command to the finish line (default to the version command)
def sendCommand(commandChar = "V"):
	if(finishLine.isOpen()==False):
		print("ERROR: Serial Port Not Open")
		return "break"
	finishLine.write(commandChar.encode())
	return "break"
	
#the subroutine to just read data off of the serial port
def readSerial():
	if(finishLine.isOpen()==False):
		print("ERROR: Serial Port Not Open")
		return "break"
	if(finishLine.in_waiting > 0):
		print(finishLine.read(finishLine.in_waiting).decode())
	root.after(500, readSerial)
	return "break"

#the subroutine to clean up and get out
def getOut():
	finishLine.close()
	root.destroy()
	

#initialize the main application
root = tkinter.Tk()
root.title("PyGP Management GUI")
root.minsize(width=500, height=500)

#define variables here
serialPortString = StringVar()
serialPortString.set('COM1')

#initialize the main three tabs
tabs = ttk.Notebook(root)
regTab = ttk.Frame(tabs)
raceTab = ttk.Frame(tabs)
devTab = ttk.Frame(tabs)
tabs.add(regTab, text='Registration')
tabs.add(raceTab, text='Race Admin')
tabs.add(devTab, text='Device Admin')

tabs.pack(expand=1, fill="both")
Label(devTab, text="Port:").grid(row = 0, column = 1, sticky = W)
Entry(devTab, textvariable = serialPortString).grid(row = 0, column = 2, columnspan = 2, sticky = (E, W))
Button(devTab, text="Set Port", command = setPort).grid(row = 0, column = 4, sticky = (E, W))
Button(devTab, text="0 Pg Mem", command=lambda: sendCommand("D")).grid(row = 1, column = 1, sticky = (E, W))
Button(devTab, text="Version", command=lambda: sendCommand("V")).grid(row = 1, column = 2, sticky = (E, W))
Button(devTab, text="Results", command=lambda: sendCommand("L")).grid(row = 1, column = 3, sticky = (E, W))
Button(devTab, text="All Pixels Disp", command=lambda: sendCommand("T")).grid(row = 1, column = 4, sticky = (E, W))
Button(devTab, text="SensorState", command=lambda: sendCommand("O")).grid(row = 2, column = 1, sticky = (E, W))
Button(devTab, text="Rotating Disp", command=lambda: sendCommand("Q")).grid(row = 2, column = 2, sticky = (E, W))
Button(devTab, text="Reset Timer", command=lambda: sendCommand("R")).grid(row = 2, column = 3, sticky = (E, W))
Button(devTab, text="Flash LED", command=lambda: sendCommand("F")).grid(row = 2, column = 4, sticky = (E, W))
Button(devTab, text="Start Timer", command=lambda: sendCommand("S")).grid(row = 3, column = 1, sticky = (E, W))
Button(devTab, text="QUIT", command=getOut).grid(row = 4, column = 1, columnspan =4, sticky = (E, W))

root.mainloop()