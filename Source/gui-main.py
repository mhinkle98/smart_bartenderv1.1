from PyQt5 import QtWidgets, uic
import speech_rec as speech
import drinks
import time


####### Window Setup #######

app = QtWidgets.QApplication([])
dlg = uic.loadUi(r"C:\Users\Max Hinkle\Desktop\Code\Python\Bartender\SmartBartenderV1.1\SmartBartenderV1.1\SmartBartenderV1.1\Source\mainwindow.ui")
dlg.setWindowTitle("Smart Bartender Version 1.1")
customizationWidgets = [dlg.label, dlg.label_2, dlg.label_3, dlg.drinksList, dlg.sizeSpinBox, dlg.strengthSpinBox, dlg.startButton]
statusWidgets = [dlg.drinkProgressBar, dlg.label_4]

####### Functions ######

def showOptions():
    for widget in customizationWidgets:
        widget.setVisible(True)
    for widget in statusWidgets:
        widget.setVisible(False)
def hideOptions():
    for widget in customizationWidgets:
        widget.setVisible(False)
def hideProgress():
    for widget in statusWidgets:
        widget.setVisible(False)
def showRestartButton():
    dlg.restartButton.setVisible(True)

def showProgress(percent):
    for widget in statusWidgets:
        widget.setVisible(True)
    dlg.drinkProgressBar.setValue(percent)    
    showRestartButton()
            

def makeDrink():
    selection = str(dlg.drinksList.item)
    print(selection)
    strength = dlg.strengthSpinBox.value
    print(strength)
    for drink in drinks.drinks_list:
        if selection == drink.name:
            drink.pour(strength)

def appRun():
    hideOptions()
    hideProgress()
    dlg.restartButton.setVisible(False)
    
    


###### Connections ######

dlg.makeDrinkButton.clicked.connect(showOptions)
dlg.startButton.clicked.connect(showProgress)
dlg.startButton.clicked.connect(makeDrink)
dlg.restartButton.clicked.connect(appRun)






appRun() # Set initial conditions



####### executive #######

dlg.show()
app.exec()

