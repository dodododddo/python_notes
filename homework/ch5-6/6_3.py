import unittest

def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# 测试
class TestReverseString(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")

if __name__ == '__main__':
    unittest.main()