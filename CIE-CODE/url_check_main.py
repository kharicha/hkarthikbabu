##################################################################################
#
# url_check_main - 
#    Main backend module that receives the URL and does the following,
#	Validate the given URL whether it is actually given in an URL Format
#	Connect to the MongoDB
#	Verify if the given URL is present in the Invalid URL Database
#	Verify if the given URL is present in the valid URL Database
#	If the given URL is not present in both the database it will be treated
#        as unknown and will be declared as invalid URL for security reasons (this could be changed to valid also)
#	So this is the main code which looks up in db for malwares returns the result with URL is safe or Malware back to the application.
#
#  Revision History
#    * 1.0 - 5.28.21 - Karthik Babu Harichandra Babu - Initial version
#
#################################################################################

import re
from pymongo import MongoClient

class URL_Check():
    def __init__(self,url):
        self.url = url

    def url_verify(self):
        
        ########################
        # VALIDATE THE GIVEN URL
        ########################
        try:
            pattern = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
            matches = pattern.findall(self.url)
            if matches:
                for match in matches:
                    if match:
                        proto, dom, tld, v= match
                        dom = dom.strip(r'www.')
                        full_dom = f"{dom}.{tld}"
            else:
                return False, True
        except Exception as e:
            raise Exception("The Given URL is not in Valid URL Format\n")

	#########################
        # CONNECT TO THE MONGO DB
        #########################

        try:
            mongo_uri = "mongodb://localhost:27017/"
            client = MongoClient(mongo_uri)
        except Exception as e:
            raise Exception("Not able to connect to the Mongo DB\n")

        ######################################
        # VERIFY THE URL PRESENT IN INVALID DB
        ######################################
      
        db = client.invalid_db
        collection = db.demoCollection
        result = collection.find_one({"url": full_dom})
        if result:
            return False, False
  
        ####################################
        # VERIFY THE URL PRESENT IN VALID DB
        ####################################
      
        db = client.valid_db
        collection = db.demoCollection
        result = collection.find_one({"url": full_dom})
        if result:
            return True, False 

        # If the given URL is not present in both the valid/invalid db, for security reason blocking the unknown url as unvalid
        return False, False

