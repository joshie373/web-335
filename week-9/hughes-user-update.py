# ============================================
# ; Title: Assignment 9.3
# ; Author: Joshua Hughes
# ; Date: 12 December 2019
# ; Modified By: Joshua Hughes
# ; Description: Updating and Deleting documents
# ;===========================================
from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(

    {"employee_id": "1000005"},

    {

        "$set": {

            "email": "joshughes@my365.bellevue.edu"

        }

    }

)

pprint.pprint(db.users.find_one({"employee_id": "1000005"},{"email": 1, "employee_id": 1, "first_name": 1, "last_name": 1}))
