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

# Deletes document based of predetermined query input
def delete_document(document):
	try:
		result=collection.delete_one(document)
		print("The Document you have selected has been Deleted succesfully!")
	except Exception as ve:
		abort(400, str(ve))
	return result

# Main function to run operations and call functions
def main():
	delete_info = input("Please enter a Document that you would like to DELETE: \n")
	delete_document(delete_info)

# Runs python script as a program
if __name__ == '__main__':
	main()