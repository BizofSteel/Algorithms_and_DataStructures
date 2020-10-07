#!/usr/bin/python
import json
from bson import json_util
from pymongo import MongoClient
import pprint
import datetime

# Database connection and selection
connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# Updates document based of predetermined query input
def update_document(criteria, document):
	try:
		collection.update_one(criteria,{"$set" : document})
		result = collection.find(criteria)
		print("The Document has successfully updated with your update information!")
	except Exception as ve:
		abort(400, str(ve))
	return result 

# Main function to run opperations and call functions
def main():
	doc_info = input("Please enter Document you intend to UPDATE\n")
	criteria_info = input("Please enter criteria of Document that you would like to update\n")
	update_document(doc_info, criteria_info)
	print("Below is the document you have selected to UPDATE with new updates.\n")

# Runs python script as a program
if __name__ == '__main__':
	main()
