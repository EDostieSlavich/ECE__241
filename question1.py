class Hw1Q1():
    """Attributes of class are in terms of seconds. Method converts seconds new format"""

    def __init__(self):
        self.second = 1
        self.minute = 60                                                    # seconds in a minute
        self.hour = 60*60                                                   # "           " hour
        self.day = 60*60*24                                                 # "           " day

    def timeConvert(self, input_seconds):
        """Input number of seconds to convert to # day(s) # hour(s) # minute(s) # second(s)"""
        condensed = {}
        numDays = input_seconds/self.day                                    # calculate number of days
        numHours = (input_seconds - int(numDays)*self.day)/self.hour        # "                 " hours
        numMin = (numHours*self.hour - int(numHours)*self.hour)/self.minute # "                 " minutes
        numSec = (numMin*self.minute - int(numMin)*self.minute)/self.second # "                 " seconds))
        convert = {"days": int(numDays),                                    # dictionary of time keys and values
                   "hours": int(numHours),
                   "minutes": int(numMin),
                   "seconds": int(numSec)
                   }
        for x, y in convert.items():                                        # remove keys and values that are zero
            if y > 0:
                condensed.update({x: y})
                if y == 1:                                                  # update plural keys if necessary
                    condensed[x.strip('s')] = condensed[x]
                    del condensed[x]
        printedForm = ''
        for x, y in condensed.items():                                      # formatting print style
            printedForm = printedForm+str(y)+" "+x+" "
        return print(printedForm)


if __name__ == '__main__':
    time = Hw1Q1()
    Hw1Q1.timeConvert(time, 100000)
    Hw1Q1.timeConvert(time, 100)
