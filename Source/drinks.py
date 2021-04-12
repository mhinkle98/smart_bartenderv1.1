from pyfirmata import Arduino, util
import time


#board = Arduino("COM3") # defines arduino board connection

pump_1 = 0#board.get_pin('d:3:o') # pin 3 connects to first relay -> first pump
pump_2 = 0#board.get_pin('d:4:o') # pin 4 connects to second relay -> second pump
pump_3 = 0#board.get_pin('d:5:o') # pin 5 connects to third relay -> third pump

pumps = {
    "Vodka": pump_1,
    "Rum": pump_2,
    "Sprite": pump_3,
    "Tequila": pump_1,
    "Coke": pump_2,
    "Lemonade": pump_3,
    "Iced Tea": pump_2
    }

pourTimes = [5, 10, 15]

class drinks:
    percent_finished = 0

    def __init__ (self, name, alc_pumps, mixers):
        self.name = name
        self.alc_pumps = alc_pumps
        self.mixers = mixers
    
    def getTime(self, strength):
        total_pumps = length(self.alc_pumps) + length(self.mixers)
        total_time = pourTimes[strength - 1] * total_pumps
        return total_time

    def pour(self, strength):
        self.percent_finished = 0
        print("Making a " + self.name)
        time_needed = getTime(strength)
        time_taken = 0
        gui-main.showProgress(self.percent_finished)
        for drink in self.alc_pumps, self.mixers:
            #drink.write(1)
            time.sleep(pourTimes[strength - 1])
            time_taken += pourTimes[strength - 1]
            #drink.write(0)
            self.percent_finished = (time_taken/time_needed * 100)
            gui-main.showProgress(self.percent_finished)
        print("Finished!")


vodka_sprite = drinks("Vodka Sprite", pumps["Vodka"], pumps["Sprite"])
john_daley = drinks("John Daley", pumps["Vodka"], [pumps["Iced Tea"], pumps["Lemonade"]])


drinks_list = [vodka_sprite, john_daley]