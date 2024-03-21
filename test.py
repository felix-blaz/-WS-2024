import HtmlTestRunner
import unittest
import requests



def checkServiceForWord(url, keyword):
    try:
        x = requests.get(url)
        print(x.text)
        serverStatus=1
        if keyword in x.text:
            print("found keyword")
        return True
    except:
        print("error")
        return False


class TestStringMethods(unittest.TestCase):
    def test_twoValuesAreEqual(self):
        value1=True
        #value2=True

        url = 'http://localhost:5000/getProducts'
        result = checkServiceForWord(url, '1')
        print(result)

        self.assertEqual(value1, result)
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_output'))