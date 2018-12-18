from comm.http_request import Http_request
import unittest,requests
from ddt import ddt,unpack,data
from comm.DO_excel import Do_excel
from comm.log_decorator import log_decorator
cookies=""
@ddt
class Http_test(unittest.TestCase):
    register_data=Do_excel().read_excel("testdatas.xlsx","register")
    login_data=Do_excel().read_excel("testdatas.xlsx","login")
    recharge_data=Do_excel().read_excel("testdatas.xlsx","recharge")
    @data(*register_data)
    @log_decorator
    def test_1register(self,item):
        """用unpack时，测试用例的方法中接受的参数必须跟字典的键相同"""
        res=Http_request(item.url,item.method,params=item.test_data) 
        actual=res.get_json()["msg"]
        item.actual=actual
        self.assertEqual(actual,item.expect["msg"])
    @data(*login_data)
    @log_decorator
    def test_2login(self,item):
        res=Http_request(item.url,item.method,params=item.test_data) 
        actual=res.get_json()["msg"]
        item.actual=actual
        self.assertEqual(actual,item.expect["msg"])
        global cookies
        cookies=res.get_cookiese()
    @data(*recharge_data)
    @log_decorator 
    def test_3recharge(self,item):
        res=Http_request(item.url,item.method,params=item.test_data,cookies=cookies) 
        actual=res.get_json()["msg"]
        item.actual=actual
        self.assertEqual(actual,item.expect["msg"]) 
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 