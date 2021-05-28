from pymongo import MongoClient
import re

########################
# VALIDATE THE GIVEN URL
########################
def valid_url(url):
    try:
        pattern = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
        matches = pattern.findall(url)
        full_dom = ""
        for match in matches:
            if match:
                proto, dom, tld, v= match
                dom = dom.strip(r'www.')
                full_dom = f"{dom}.{tld}"
        return full_dom 
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

###################################
# DELETE THE VALID/INVALID DATABASE
###################################

try:
    client.drop_database("invalid_db")
    client.drop_database("valid_db")
except Exception as e:
    raise Exception("Not able to delete the existing valid/invalid db\n")

#############################
# CREATE THE INVALID DATABASE
#############################

try:
    # connecting or switching to the database
    db = client.invalid_db

    # creating or switching to demoCollection
    collection = db.demoCollection
    new_posts = []
    with open("malware_url.txt") as f:
        for line in f:
            full_dom = valid_url(line)
            n_posts = {
                "url": full_dom,
                "status": "malware"
            }
            new_posts.append(n_posts)
    collection.insert_many(new_posts)

    # Printing the data inserted
    cursor = collection.find()
    for record in cursor:
        print(record)

except Exception as e:
    raise Exception("Not able to create the invalid db with entries\n")

###########################
# CREATE THE VALID DATABASE
###########################

try:
    # connecting or switching to the database
    db = client.valid_db

    # creating or switching to demoCollection
    collection = db.demoCollection
    new_posts = []
    with open("clean_url.txt") as f:
        for line in f:
            full_dom = valid_url(line)
            n_posts = {
                "url": full_dom,
                "status": "clean"
            }
            new_posts.append(n_posts)
    collection.insert_many(new_posts)

    # Printing the data inserted
    cursor = collection.find()
    for record in cursor:
        print(record)

except Exception as e:
    raise Exception("Not able to create the invalid db with entries\n")
