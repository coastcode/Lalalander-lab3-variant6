import unittest
from visualized import *


class FactorialTest(unittest.TestCase):
    def test_Factorial(self):
        Lbd = Lambda()
        self.assertEqual(Lbd.FACT(5), 120)
        self.assertEqual(Lbd.FACT(8), 40320)
        dot = Lbd.visualize()
        f = open('fsm.dot', 'w')
        f.write(dot)
        f.close()


if __name__ == '__main__':
    unittest.main()
