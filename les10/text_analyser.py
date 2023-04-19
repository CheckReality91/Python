import unittest
import os

def analyse_text(filename):
    """
    Het aantal regels in een bestand berekenen.
    
    Args:
        filename: De naam van het te analyseren bestand.
        
    Werpt op:
        IOError: al "filename" niet bestaat
        
    Retouneer:
        Het aantal regels in het bestand
    """
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

class TextAnalysisTests(unittest.TestCase):
    
    def setUp(self):
        # Fixture die een bestand maakt voor de testmethoden
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war,\n'
                    'testing whether that nation, \n'
                    'or any nation so conceived and so dedicated, \n'
                    'can long endur.')
            
    def tearDown(self):
        try:
            os.remove(self.filename)
        except OSError:
            pass
        
    def test_function_runs(self):
        analyse_text(self.filename)
        
    def test_line_count(self):
        self.assertEqual(analyse_text(self.filename), 4)
        
if __name__ == "__main__":
    unittest.main()