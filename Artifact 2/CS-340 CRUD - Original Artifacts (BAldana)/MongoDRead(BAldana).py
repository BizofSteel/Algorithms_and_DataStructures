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

# Reads document based of predetermined query input
def read_document(query):
	try:
		result=collection.find_one(query)
		print(type(result))
		print(result)
	except Exception as ve:
		abort(400, str(ve))
	return result


# Main function to run opperations and call functions
def main():
	search_info = input("Please enter a Document that you would like to RETRIEVE: \n")
	read_document(search_info)


# Runs python script as a program
if __name__ == '__main__':
	main()
