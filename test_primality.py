# Write the tests for the isprime.py file here
class CheckPrime(unittest.TestCase):

    def test_checkPrime(self):
        self.assertEqual(checkPrime(3), True)   

    def test_checkPrime2(self):
        self.assertTrue(checkPrime(5))         
        self.assertFalse(checkPrime(4))         

    def test_checkPrime3(self):
        # Check that providing a string input produces an error
        with self.assertRaises(TypeError):
            checkPrime('1')

if __name__ == '__main__':
    unittest.main()