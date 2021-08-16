# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 14:09:06 2021

@author: Tretron
"""

class informer_api_handler:
    __sales_order_url = "https://api.informer.eu/v1/salesorders/"
    __products_url = "https://api.informer.eu/v1/products/"
    __specific_products_url = "https://api.informer.eu/v1/product/{}/"
    
    def __init__(self, json_path):
        self.__json_path=json_path
        self.credentials = None
        self.Securitycode = None
        self.Apikey = None
        
    def __read_json(self):
        if self.__json_path != None:
            with open(self.__json_path) as json_file:
                self.credentials = json.load(json_file)          
    def __get_security_code(self):
        self.__read_json()
        if self.credentials != None:
            return(self.credentials['Securitycode'])
        
    def __get_apikey(self):
        self.__read_json()
        if self.credentials != None:
            return(self.credentials['Apikey'])
    def __fetch_information(self, url):
        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["Securitycode"] = self.__get_security_code()
        headers["Apikey"] = self.__get_apikey()
        
        return (requests.get(url, headers=headers))
    
    def get_orders(self):
        resp = self.__fetch_information(self.__sales_order_url)

        return(json.loads(resp.content))
    
    def fetch_all_products(self):
        resp = self.__fetch_information(self.__products_url)

        return(json.loads(resp.content))
    
    def fetch_specific_product(self,product_id):
        resp = self.__fetch_information(self.__specific_products_url.format(int(product_id)))

        return(json.loads(resp.content))