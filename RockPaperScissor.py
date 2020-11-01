import tkinter
import tkinter.messagebox as box
import random 

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("200x200")

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.radioFrame = tkinter.Frame(self.mainWindow)
        # self.middle_frame = tkinter.Frame(self.main_window)
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        # Pack the frames.
        self.radioFrame.pack()
        self.buttonFrame.pack()

        # Create an StringVar object to use with
        # the Radiobuttons.
        self.radioVar = tkinter.StringVar()

        # Set the strVar object to 1.(initialize)
        self.radioVar.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text='Rock', variable=self.radioVar, value='Rock')
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text='Paper', variable=self.radioVar, value='Paper')
        self.rb3 = tkinter.Radiobutton(self.radioFrame, text='Scissors', variable=self.radioVar, value='Scissors')

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Set up buttons
        self.playButton = tkinter.Button(self.buttonFrame, text='Play', command=self.showOption)
        self.quitButton = tkinter.Button(self.buttonFrame, text='Quit', command=self.mainWindow.destroy)

        # Pack the Buttons.
        self.playButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Start the mainloop.
        tkinter.mainloop()

        #list of choices
        self.options = ['Rock','Paper','Scissors']

    #function to generate computer move 
    def getCompOption(self):
        compOption = random.choice(self.options)
        #return compOption
        return compOption

    #show the player's and computer's randomly selection option in pop up window
    def showOption(self):
        box.showinfo('Selection', 'You selected: ' + self.radioVar.get()+'\nComputer Selected: '+ self.getCompOption())


demoGUI = MyGUI()
