import HtmlTestRunner
import unittest
import requests


def saveResult(name, url, result):
    with open('test.log', 'w+') as f:
        f.write('Test name:' + str(name) + '\n')
        f.write('Test URL:' + str(url) + '\n')
        f.write('Test result:' + str(result) + '\n')
        f.write('---------------------------------------------\n ')
def checkServiceForWord(url, keyword):
    result = False
    try:
        x = requests.get(url)
        print(x.text)
        serverStatus=1
        if keyword in x.text:
            print("found keyword")
            result=True
    except:
        print("error")
        result= False
    return result


class TestStringMethods(unittest.TestCase):


    def test_getProductsKeyword(self):
        url = 'http://localhost:5000/getProducts'
        result = checkServiceForWord(url, '1')
        self.assertTrue(result)
        saveResult('Test1', url, result)

    def test_rootEndpointKeyword(self):
        url = 'http://localhost:5000/'
        result = checkServiceForWord(url, 'Will')
        self.assertTrue(result)
        saveResult('Test2', url, result)


def test_rootEndpointKeyword(self):
    url = 'http://localhost:5000/'
    result = checkServiceForWord(url, 'Will')
    self.assertTrue(result)
    saveResult('Test2', url, result)
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_output'))