from CalculadoraIRRF import CalculadoraIRRF

import unittest


class TestCalculadora(unittest.TestCase):
    def test(self):
        calc = CalculadoraIRRF()

        self.assertEqual(calc.subtrairBaseIRRF(3000), 1096.02)
        self.assertEqual(calc.subtrairBaseIRRF(5000), 3096.02)
        self.assertEqual(calc.subtrairBaseIRRF(7000), 5096.02)
        self.assertEqual(calc.subtrairBaseIRRF(9000), 7096.02)

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCalculadora)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)


if __name__ == '__main__':
   runTests()
