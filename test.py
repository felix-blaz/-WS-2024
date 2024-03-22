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


    def test_getProductsEndpoint(self):
        url = 'http://localhost:5000/getProducts'
        result = checkServiceForWord(url, '1')
        self.assertTrue(result)
        saveResult('Test1', url, result)

    def test_getTitlesEndpoint(self):
        url = 'http://localhost:5000/getTitles'
        result = checkServiceForWord(url, 'bread')
        self.assertTrue(result)
        saveResult('Test2', url, result)

    def test_rootEndpointKeyword(self):
        url = 'http://localhost:5000/'
        result = checkServiceForWord(url, 'Will')
        self.assertTrue(result)
        saveResult('Test3', url, result)


    def test_insertProductsEndpointKeyword(self):
        url = 'http://localhost:5000/insertProducts'
        headers = {'Content-Type': 'application/json', 'api_key': 'aaa'}
        data = {
            'ProductId': '123',
            'Title': 'Test Product',
            'Quantity': 10
        }

        response = requests.post(url, headers=headers, json=data)
        # Check if the request was successful (status code 201)
        self.assertEqual(response.status_code, 201)

        # Save the test result
        saveResult('Test4', url, response.status_code)
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_output'))