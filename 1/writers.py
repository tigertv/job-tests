#!/usr/bin/python
import sys
import os
import re 
import requests
import logging as log

class CsvScreenWriter():
	def write(self, results):
		if results is None:
			return None

		keys = {}
		for item in results:
			if item: 
				for key in item['data']:
					keys[key] = 1

		# header
		content = 'Team'
		for item in results:
			if item:
				content += ','+item["name"]
		content += "\n"

		# data
		for key in keys:
			content += key
			for item in results:
				if item:
					if key in item["data"]:
						content += ','+item["data"][key] 
					else:
						content += ',-'

			content += '\n'

		# output in a file
		print content
		return content

class CsvFileWriter():
	fileName = 'results.csv'

	def __init__(self, fileName):
		if fileName:
			self.fileName = fileName

	def setFileName(self, fileName):
		self.fileName = fileName

	def write(self, results):
		if not results:
			return None
		keys = {}
		
		for item in results:
			if item:
				if 'data' in item:
					for key in item['data']:
						keys[key] = 1
		# header
		content = 'Team'
		for item in results:
			if item:
				if 'name' in item:
					content += ','+item["name"]
		content += "\n"

		# data
		for key in keys:
			content += key
			for item in results:
				if item:
					if item['data']:
						content += ','+item["data"][key] 
					else:
						content += ',-'

			content += '\n'

		# output in a file
		try:
			file = open(self.fileName, 'w') 
			file.write(content) 
			file.close()
		except IOError:
			print "Error: Can't open and read the file"
		return content
	
