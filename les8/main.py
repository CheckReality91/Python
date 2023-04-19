class CursistenRegister:
    
    def __init__(self, first_name, last_name, adress, email):
        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress
        self.email = email
        
    def welkomstbericht(self):
        print(f"Welkom {self.first_name} {self.last_name}. Uw boekenpakket is verstuur naar {self.adress}. U krijgt hiervan een bevestiging op het door u opgegeven e-mailadres: {self.email} ")
        

laurens = CursistenRegister('Laurens', 'Schaap', "Janninksplein 6", "l.schaap91@gmail.com")

laurens.welkomstbericht()