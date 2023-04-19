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
        Een tupel met als eerste element het aantal regels in de bestanden en als tweede element het aantal tekens.
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
        return (lines, chars)

class TextAnalysisTests(unittest.TestCase):
    
    def setUp(self):
        # Fixture die een bestand maakt voor de testmethoden
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war,\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endur. ')
            
    def tearDown(self):
        try:
            os.remove(self.filename)
        except OSError:
            pass
        
    def test_function_runs(self):
        analyse_text(self.filename)
        
    def test_line_count(self):
        self.assertEqual(analyse_text(self.filename)[0], 4)
        
    def test_character_count(self):
        self.assertEqual(analyse_text(self.filename)[1], 131)
        
    def text_no_such_file(self):
        with self.assertRaises(IOError):
            analyse_text('foobar')
            
    def test_no_deletion(self):
        analyse_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))
        
if __name__ == "__main__":
    unittest.main()