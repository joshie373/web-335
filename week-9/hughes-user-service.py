# ============================================
# ; Title: Assignment 9.2
# ; Author: Joshua Hughes
# ; Date: 12 December 2019
# ; Modified By: Joshua Hughes
# ; Description: Querying and creating documents
# ;===========================================
from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {

    "first_name": "Chris",

    "last_name": "Christofferson",

    "email": "cchristoff@email.com",

    "employee_id": "1000005",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "1000005"}))
