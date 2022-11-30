

import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")       # connection
mydb = myclient["mydatabase"]   # create a database named "mydatabase":
mycol = mydb["customers"]               #  Create a collection called "customers":



print(myclient.list_database_names())       # Return a list of your system's databases
print(mydb.list_collection_names())     #  Return a list of all collections in your database:


#x = mycol.find_one()      #  Find the first document in the customers collection:
#print(x)


#for x in mycol.find():    #  Return all documents in the "customers" collection, and print each document:
  #print(x)


#for x in mycol.find({},{ "address": 0 }):   #  This example will exclude "address" from the result:
  #print(x)




def my_limit_func():
    myresult = mycol.find().limit(5)   #   Limit the result to only return 5 documents:

    #print the result:
    for x in myresult:
        print(x)


def my_del_func():
    myquery = { "address": "Mountain 21" }   # Delete the document with the address "Mountain 21":
    mycol.delete_one(myquery)


def my_del_func_2():
    myquery = { "address": {"$regex": "^S"} }   #   Delete all documents were the address starts with the letter S:
    x = mycol.delete_many(myquery)
    print(x.deleted_count, " documents deleted.")



def my_del_func_3():
    x = mycol.delete_many({})             #   Delete ""all"" documents in the "customers" collection:
    print(x.deleted_count, " documents deleted.")


def my_drop():
    mycol.drop()      #    Delete the "customers" collection:



def my_update_func():
    myquery = { "address": "Valley 345" }           #    Change the address from "Valley 345" to "Canyon 123"
    newvalues = { "$set": { "address": "Canyon 123" } }

    mycol.update_one(myquery, newvalues)

    #print "customers" after the update:
    for x in mycol.find():
        print(x)




def my_upd_func_2():
    myquery = { "address": { "$regex": "^S" } }     #    Update all documents where the address starts with the letter "S":
    newvalues = { "$set": { "name": "Minnie" } }

    x = mycol.update_many(myquery, newvalues)

    print(x.modified_count, "documents updated.")



def my_query_func():    
    myquery = { "address": "Park Lane 38" }   #  Find document with the address "Park Lane 38": 
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)


def my_query_func_2():
    #myquery = { "address": { "$gt": "S" } }     #  Find documents where the address starts with the letter "S" or higher:
    myquery = { "address": { "$regex": "^S" } }  #  Find documents where the address starts with the letter "S":

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)




def check_database():
    dblist = myclient.list_database_names()
    if "mydatabase" in dblist:
        print("The database exists.")


def check_collection():
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")






