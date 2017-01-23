#!usr/bin/python
import os
import re



class commandNLP:


	'''
	class variables

	'''
	cwd = os.getcwd()
	gameVerbs = ["look", "take", "help", "inventory", "use", 
	"drop", "eat", "drink", "pull", "hit", "put", 
	"savegame", "loadgame", "push", "wield", "wear"]
	verbPrepositionCombos = {}
	synonymFile = cwd + "/synonymFile.txt"
	synonymsDictionary = {}


	'''

	Definition:

	'''

	def __init__(self, synonymFile):



	'''

	Definition:

	'''

	def parseCommand(commandString):
		foobar= 3






