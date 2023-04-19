import unittest

class Test(unittest.TestCase):
    
    def test_zelfde_waarde(self):
        # Test of de beide waardes hetzelfde zijn.
        waarde1 = 100
        waarde2 = 100
        self.assertEqual(waarde1, waarde2)
    
if __name__ == "__main__":
     unittest.main()