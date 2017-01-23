#!usr/bin/python
import os
import re



class commandNLP:




	'''

	Definition: This is the constuctor for the commandNLP 

	'''

	def __init__(self):

		self.cwd = os.getcwd()
		self.gameVerbs = ["look", "take", "help", "inventory", "use", 
		"drop", "eat", "drink", "pull", "hit", "put", 
		"savegame", "loadgame", "push", "wield", "wear"]
		self.verbPrepositionCombos = {}
		self.synonymsDictionary = {}


	'''

	Definition:

	'''

	def buildSynonymDict(self):

		synonymFilePath = cwd + "/synonymFile.txt" #file source: https://justenglish.me/2014/04/18/synonyms-for-the-96-most-commonly-used-words-in-english/

		with open(synonymFilePath) as f:
			for line in f:
				splitLine = line.split("—")
				verb, synonymList = splitLine
				parsedSynonyms = synonymList.split(",")
				for word in parsedSynonyms:
					self.synonyms




	'''

	Definition:

	'''

	def parseCommand(commandString):




def doNLP():
	potentialCommand = input("Your move: ")


if __name__ =='__main__':
	doNLP()


