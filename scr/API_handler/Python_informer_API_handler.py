# -*- coding: utf-8 -*-
"""
Python informer API handler.

Auther: Tretron
Licence: MIT

for more information about the key self: https://api.informer.eu/docs/#/
"""


import json
import requests
from requests.structures import CaseInsensitiveDict

class informer_api_handler:
    __sales_order_url = "https://api.informer.eu/v1/salesorders/"
    __products_url = "https://api.informer.eu/v1/products/"
    __specific_products_url = "https://api.informer.eu/v1/product/{}/"
    
    def __init__(self, json_path):
        """
        

        Parameters
        ----------
        json_path : STRING
            Setup handler with a path to the json file storing the securitycode and apikey in the following format:
            {
            	"Securitycode": "securitycode",
            	"Apikey": "apikey"
            }

        Returns
        -------
        None.

        """
        self.__json_path=json_path
        self.credentials = None
        self.Securitycode = None
        self.Apikey = None
        
    def __read_json(self):
        """
        

        Returns
        -------
        None.

        """
        if self.__json_path != None:
            with open(self.__json_path) as json_file:
                self.credentials = json.load(json_file)          
    def __get_security_code(self):
        """
        

        Returns
        -------
        None.

        """
        self.__read_json()
        if self.credentials != None:
            return(self.credentials['Securitycode'])
        
    def __get_apikey(self):
        """
        

        Returns
        -------
        None.

        """
        self.__read_json()
        if self.credentials != None:
            return(self.credentials['Apikey'])
    def __fetch_information(self, url):
        """
        

        Parameters
        ----------
        url : string
            url to informer api.

        Returns
        -------
        content : OBJECT
            returns an requests object containing both the response code and response from the API.

        """
        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["Securitycode"] = self.__get_security_code()
        headers["Apikey"] = self.__get_apikey()
        
        return (requests.get(url, headers=headers))
    
    def get_orders(self):
        """
        

        Returns
        -------
        orders : JSON string
            returns all orders as json string

        """
        resp = self.__fetch_information(self.__sales_order_url)

        return(json.loads(resp.content))
    
    def fetch_all_products(self):
        """
        

        Returns
        -------
        None.

        """
        resp = self.__fetch_information(self.__products_url)

        return(json.loads(resp.content))
    
    def fetch_specific_product(self,product_id):
        """
        

        Parameters
        ----------
        product_id : string
            the string of a product_id, this is the internal informer product_id NOT the sales product code that is used by the user.

        Returns
        -------
        None.

        """
        resp = self.__fetch_information(self.__specific_products_url.format(int(product_id)))

        return(json.loads(resp.content))