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

# Create new document in data base
def create_document(document):
	try:
		result=collection.insert_one(document)
		print("The Document has been successfully created!\n")
	except Exception as ve:
		abort(400, str(ve))
	return result

# Main function to run opperations and call functions
def main():
	input_info = input("Please enter a Document that you would like to CREATE: \n")
	create_document(input_info)
	print("You have selected to exit the Service Program is, Thank you!   Goodbye! \n")

# Runs python script as a program
if __name__ == '__main__':
	main()
