class HW1Q1():
    """Attributes of class are in terms of seconds. Method converts seconds new format"""

    def __init__(self):
        self.second = 1
        self.minute = 60                                                    # seconds in a minute
        self.hour = 60*60                                                   # "           " hour
        self.day = 60*60*24                                                 # "           " day

    def timeConvert(self, input_seconds):
        """Input number of seconds to convert to # day(s) # hour(s) # minute(s) # second(s)"""
        numDays = input_seconds/self.day                                    # calculate number of days
        numHours = (input_seconds - int(numDays)*self.day)/self.hour        # "                 " hours
        numMin = (numHours*self.hour - int(numHours)*self.hour)/self.minute # "                 " minutes
        numSec = (numMin*self.minute - int(numMin)*self.minute)/self.second # "                 " seconds
        if int(numDays) == 1:                                               # change each quantity to string
            strDays = str(int(numDays))+' day '                             # or remove if quantity is 0
        elif int(numDays) > 1:
            strDays = str(int(numDays))+' days '
        else:
            strDays = ''
        if int(numHours) == 1:
            strHours = str(int(numHours))+' hour '
        elif int(numHours) > 1:
            strHours = str(int(numHours))+' hours '
        else:
            strHours = ''
        if int(numMin) == 1:
            strMin = str(int(numMin))+' minute '
        elif int(numMin) > 1:
            strMin = str(int(numMin))+' minutes '
        else:
            strMin = ''
        if int(numSec) == 1:
            strSec = str(int(numSec))+' second '
        elif int(numSec) > 1:
            strSec = str(int(numSec))+' seconds '
        else:
            strSec = ''
        return print(strDays+strHours+strMin+strSec)                        # return new format


if __name__ == '__main__':
    time = HW1Q1()
    hundredThousand = HW1Q1.timeConvert(time, 100000)
    hundred = HW1Q1.timeConvert(time, 100)
