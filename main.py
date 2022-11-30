

import json
import pymongo
from bson.objectid import ObjectId



myclient = pymongo.MongoClient("mongodb://localhost:27017/")       # connection
mydb = myclient["mydatabase"]       # create a database named "mydatabase":
customers = mydb["customers"]           # Create a collection called "customers":
#print(customers.find_one())
#print(customers.find_one({'_id': ObjectId('637a7c436b314b536ed05dcf')}))




def import_json_data():
    with open('my_json.json') as f:     # json data importing 
        file_data = json.load(f)        

    # if pymongo >= 3.0 use insert_many() for inserting many documents
    customers.insert_many(file_data)
    for i in file_data:
        print(i)

    myclient.close()    


#import_json_data()


