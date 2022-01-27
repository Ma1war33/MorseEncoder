try:
    import morse
except:
    print("ERROR: morse MODULE NOT FOUND. ERROR #0001 CONTACT DEVLOPER.")

try:
    import sys
except:
    print("ERROR: sys MODULE NOT FOUND. ERROR #0002 MAKE SURE sys IS INSTALLED.")

try:
    import playsound
except:
    print("ERROR: playsound MODULE NOT FOUND. ERROR #0003 MAKE SURE playsound IS INSTALLED.")

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


#setting up application
app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #window size and title
        self.setWindowTitle("Morse Coder 3000")
        self.setMinimumHeight(290)
        self.setMaximumHeight(290)
        self.setMinimumWidth(400)

        #creating label1
        l1 = QLabel()
        l1.setText("Enter Message:")

        #blank label (allow it)
        l2 = QLabel()
        l2.setText(" ")

        #play sound button
        b1 = QPushButton()
        b1.setText("Play Morse")
        b1.clicked.connect(buttonpress)

        #creating textinput box
        global inputbox
        inputbox = QPlainTextEdit()
        inputbox.setPlainText("This program can encode text and decode morse code.")
        inputbox.selectAll()
        inputbox.textChanged.connect(self.textchanged)
        inputbox.setMaximumHeight(100)

        #creating morse code output box
        global outputbox
        outputbox = QPlainTextEdit()
        outputbox.setPlainText("Waiting...")
        outputbox.setReadOnly(True)
        outputbox.setMaximumHeight(100)



        #creating layout for label/button etc.
        layout = QVBoxLayout()
        layout.addWidget(l1)
        layout.addWidget(inputbox)
        layout.addWidget(l2)
        layout.addWidget(outputbox)
        layout.addWidget(b1)


        #creating widget/container
        container = QWidget() #creating a widget
        container.setLayout(layout) #setting layout of widget to "layout"
        self.setCentralWidget(container) #Moving widget to center

    #runs when text is changed in inputbox
    def textchanged(self):
        #getting input from inputbox
        input = inputbox.toPlainText()

        global text
        text = str()

        counter = 0
        temp = input.replace(" ", "") #removing all spaces

        #counting number of . and - in string and comparing to length of string (to see whether string contains letters)
        for i in temp:
            if i == "." or i == "-":
                counter = counter + 1
            else:
                pass
        
        if counter == len(temp):

            boolletters = False
        else:
            boolletters = True


        #translating or untranslating
        if boolletters == True:
            #runs if there are letters in input

            #uses morse.py to encode text
            try:
                text = morse.translate(input).lower().capitalize()
            except:
                text = "Encoding Failed."

        elif ("." in input or "-" in input) and boolletters == False:
            #runs if input is only morse code

            #uses morse.py to decode morse code
            try:
                text = morse.untranslate(input).lower().capitalize()
            except:
                text = "Encoding Failed."

        elif input == "":
            text = ""
        
        else:
            #prints if error
            print("Error")
        

        #checking if output is blank or not
        if text != "":
            #if not blank set textbox text to var(text)
            outputbox.setPlainText(text)
        else:
            #if blank set textbox text to waiting...
            outputbox.setPlainText("Waiting...")
            text = str()

def buttonpress():
    print("Button Pushed! Wow!")

#showing window
window = MainWindow()
window.show()

#App loop
app.exec()