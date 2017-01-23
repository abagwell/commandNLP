#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

cwd = os.getcwd()
gameVerbs = ["look", "take", "help", "inventory", "use", 
		"drop", "eat", "drink", "pull", "hit", "put", 
		"savegame", "loadgame", "push", "wield", "wear"]
verbPrepositionCombos = {}
synonymsDictionary = {}

'''

	Definition:

	'''

def buildSynonymDict():

	print "HELLO"

	synonymFilePath = cwd + "/synonymFile.txt" #file source: https://justenglish.me/2014/04/18/synonyms-for-the-96-most-commonly-used-words-in-english/
	

	with open(synonymFilePath, 'r') as f:
		for line in f:
			verb, synonymList= line.split('—', 2)
			verb = verb.lower()
			verb = verb.strip(' \t\n\r')
			parsedSynonyms = synonymList.split(",")
			for word in parsedSynonyms:
				word = word.strip(' \t\n\r')
				synonymsDictionary[word] = verb



def main():
	
	buildSynonymDict()

	print synonymsDictionary.keys()

if __name__ == '__main__':
	main()