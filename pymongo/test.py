import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

db=client.test

collection = db.students

student={
    'name':'董贺',
    'age':25,
}

reult = collection.insert_one(student)
print(reult)