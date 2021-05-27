#!/usr/bin/python

import re
from pymongo import MongoClient

class URL_Check():
    def __init__(self,url):
        self.url = url
        print(self.url)

    def url_verify(self):
        
        ########################
        # VALIDATE THE GIVEN URL
        ########################
        try:
            pattern = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
            matches = pattern.findall(self.url)
            for match in matches:
                if match:
                    print(f"karthik match is {match}")
                    proto, dom, tld, v= match
                    dom = dom.strip(r'www.')
                    print(f"karthik dom is {dom}")
                    full_dom = f"{dom}.{tld}"
        except Exception as e:
            raise Exception("The Given URL is not in Valid URL Format\n")

        print(full_dom)
 
	#########################
        # CONNECT TO THE MONGO DB
        #########################

        try:
            mongo_uri = "mongodb://localhost:27017/"
            client = MongoClient(mongo_uri)
            print(client.list_database_names())
        except Exception as e:
            raise Exception("Not able to connect to the Mongo DB\n")

        ######################################
        # VERIFY THE URL PRESENT IN INVALID DB
        ######################################
      
        db = client.invalid_db
        collection = db.demoCollection
        print(full_dom)
        result = collection.find_one({"url": full_dom})
        if result:
            print("karthik")
            return False 
        print("babu")
        print(result)
  
        ####################################
        # VERIFY THE URL PRESENT IN VALID DB
        ####################################
      
        db = client.valid_db
        collection = db.demoCollection
        print(full_dom)
        result = collection.find_one({"url": full_dom})
        if result:
            print("karthik1")
            return True 
        print("babu1")
        print(result)

        # If the given URL is not present in both the valid/invalid db, for security reason blocking the unknown url as unvalid
        return False

