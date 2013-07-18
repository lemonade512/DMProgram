#!/usr/bin/python

def readData(file_to_read):
	f = open(file_to_read, 'r')

	with f:
		data = f.read()
		return data
