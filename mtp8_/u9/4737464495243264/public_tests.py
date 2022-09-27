import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

   @classmethod
   def setUpClass(cls):
        global reduz_matriz
        undertest = __import__(module)
        reduz_matriz = getattr(undertest, 'reduz_matriz', None)

   def test_exemplo(self):
        m = [
          [1, 0, 0, 3, 2, 2, 0],
          [2, 1, 3, 0, 0, 1, 0],
          [0, 0, 1, 2, 1, 0, 0],
          [0, 0, 1, 0, 1, 1, 1],
          [0, 1, 2, 0, 3, 1, 2],
          [1, 2, 1, 1, 0, 0, 0],
          [2, 2, 0, 0, 1, 1, 0]]
        assert reduz_matriz(m) == 24
        assert m == [
          [1, 3, 0, 0, 1],
          [0, 1, 2, 1, 0],
          [0, 1, 0, 1, 1],
          [1, 2, 0, 3, 1],
          [2, 1, 1, 0, 0]]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
