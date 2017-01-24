#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

cwd = os.getcwd()

gameVerbs = ["drink", "drop", "eat", "help", "hit", "inventory", "loadgame", "look", "pull", "push",
"savegame", "take", "use", "wear", "wield"]

prepositions = ["above", "at", "behind", "into", "on", "under", "with" ]

gameObjects = [ "altar", "apple", "armor", "axe", "bearskin", "bed", "book", "books", "bones", "bottle", "chair", "chairs",
                 "chandelier", "cloak", "desk", "dinnerware", "gem", "hearth", "helmet", "key", "key-rung", "knife",
                 "lantern", "lever", "lockpick", "matches", "mattress", "mushrooms", "nightstand", "note",
	  			"painting", "paintings", "ring", "rocks", "rug", "runes", "safe", "scroll", "shelf", "shelves", "sign", "stool",
                 "stools", "sword", "table", "tables", "tapestries", "tools", "treasure", "tree", "trunk", "warhammer"]


verbPrepositionCombos = {'look':['at', 'under', 'above', 'into', 'behind'], 'take': [], 
						'help': [], 'inventory': [], 'use': ['on', 'with'], 'drop' : [], 'eat': [],
						'drink':[], 'pull': [], 'hit': [], 'put': [], 'hit': [], 'put': ['on', 'into', 'under', 'above', 'with'],
						'push': ['on'], 'wield': [], 'wear': [],}
synonymsDictionary = {}

'''

Definition:

'''

def buildSynonymDict():

	
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

'''



'''


def parseCommand(commandString):

	commandString = commandString.lower()
	commandString = commandString.split()
	for word in commandString:
		word = word.strip('.,!;')

	return commandString


'''

Definition: takes the command string entered by the user. It then tokenizes that input. Next, it performs
the processes that input: 

'''


def buildTuple(commandString):

	tupleReturned = ()


	#get tokens
	parsedCommand = parsedCommand(commandString)

	#perform analysis
	for word in parsedCommand:

	#get the verb, check to see if it exists in gameVerbs, if it doesn't look in synDic, If yes, match it, if no, exit
	#get the preposition, check to see if exists. if it doesn't look in synonyms, if it doesn't exit, if it does
	#look to see if the verb preposition combo is valid, if it is continue, if not return
	#get the object 
	#return tuple

	#if can't build 
	#return tuple


def main():
	
	buildSynonymDict()
	commandTuple = ()
	while not all(commandTuple):
		command = input("Your move: ")
		commandTuple = buildTuple(commandString)
	print commandTuple

	

if __name__ == '__main__':
	main()