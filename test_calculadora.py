import calculadora
import unittest

class TestCalculadora(unittest.TestCase):

	def test_adicao(self):
		self.assertEqual(calculadora.adicao(13,13), 26)
		self.assertEqual(calculadora.adicao(-3,-6), -9)
		self.assertEqual(calculadora.adicao(0,0), 0)

	def test_subtracao(self):
		self.assertEqual(calculadora.subtracao(12,6), 6)
		self.assertEqual(calculadora.subtracao(-2,2), -4)
		self.assertEqual(calculadora.subtracao(-3,-3), 0)

if __name__ == '__main__':
	unittest.main()