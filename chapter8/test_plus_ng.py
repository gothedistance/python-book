#chapter8/test_plus_ng.py
import unittest

#テスト対象のplus関数
def plus(a,b):
    return a + b

class PlusTest(unittest.TestCase):
    #テストプログラム
    def test_plus(self):
        self.assertEqual(10, plus(2,8))
        self.assertEqual(20, plus(2,8))

if __name__ == "__main__":
    unittest.main()
