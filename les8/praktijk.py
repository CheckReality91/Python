class Opteller:
    """Een klasse die twee gestallen bij elkaar opteld"""
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def optellen(self):
        return self.num1 + self.num2
    
    def meer_of_minder(self):
            if self.optellen() > 10:
                print("De waarde is hoger dan 10.")
                
            else:
                print("De waarde is lager dan 10.")
    
    
    
tel = Opteller(8, 5)
tel.meer_of_minder()