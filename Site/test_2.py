import unittest
import re
import module1

class Test_test_2(unittest.TestCase):
    def test_A(self):
        list_mail = ["m.m@mail.ru", "m1@mail.ru","fgfg@mail.ru",'rrfr@mail.ru']
        for i in range (len(list_mail)):
            regex=re.search(r'([@]mail[.]ru)', list_mail[i])
            if (regex==None):
                a=False
            if (regex!=None):
                a=True
        self.assertTrue(a)

if __name__ == '__main__':
    unittest.main()
