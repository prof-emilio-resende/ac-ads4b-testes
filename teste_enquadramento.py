import unittest
import hashlib

class TestStringMethods(unittest.TestCase):
    def teste_enquadramento_01(self):
        self.assertEqual(enquadramento_aliquota(1800), 'Isento')

    def teste_enquadramento_02(self):
        self.assertEqual(enquadramento_aliquota(2000), 7.5)

    def teste_enquadramento_03(self):
        self.assertEqual(enquadramento_aliquota(3000), 15)

    def teste_enquadramento_04(self):
        self.assertEqual(enquadramento_aliquota(4000), 22.5)

    def teste_enquadramento_05(self):
        self.assertEqual(enquadramento_aliquota(5000), 27.5)

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)