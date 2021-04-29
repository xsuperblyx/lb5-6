import unittest
import re
import module1

class Test_test_1(unittest.TestCase):
    def test_A(self):
        list_mail = ["", "1", "m1@", "@mail", "regr@_ru", "@mail.r", "mail.ru", "@ru.mail"] 
        for i in range (len(list_mail)):
            regex=re.search(r'([@]mail[.]ru)', list_mail[i])
            if (regex==None):
                a=False
            if (regex!=None):
                a=True
        self.assertFalse(a)

if __name__ == '__main__':
    unittest.main()
