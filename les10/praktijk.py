import unittest

def gemiddelde(cijfers):
    return str(sum(cijfers)/len(cijfers))

class TestGemiddelder(unittest.TestCase):
    def test_functie_gemiddelde_met_niet_lege_lijst(self):
        print("Het gemiddelde is: " + gemiddelde([5, 6, 7, 8, 9]))
        
    def test_function_gem_met_lege_lijst(self):
        with self.assertRaises(ZeroDivisionError):
            gemiddelde([])
            
if __name__ == "__main__":
    unittest.main()